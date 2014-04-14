#!/usr/bin/env python
# encoding: utf-8
from distances import manhattan_distance
from distances import euclidean_distance
from distances import minkowski_distance


def computeNearestNeighbor(username, users, distance_algorithm='euclidean'):
    """
    creates a sorted list of users based on their distance to username

    """
    distances = []
    for user in users:
        if user != username:

            if distance_algorithm == 'manhatten':
                distance = manhattan_distance(users[user], users[username])

            elif  distance_algorithm == 'euclidean':
                distance = euclidean_distance(users[user], users[username])

            elif  distance_algorithm == 'minkowski':
                distance = minkowski_distance(users[user], users[username], 5)

            distances.append((distance, user))

    # sort based on distance -- closest first!
    distances.sort()
    return distances


def recommend(username, users):
    """
    Give list of recommendations
    """

    # first find nearest neighbor
    nearest = computeNearestNeighbor(username,
                                     users,
                                     distance_algorithm='euclidean')

    for i in range(len(nearest)):

        the_nearest = nearest[i][1]

        recommendations = []
        # now find bands nearest neighbor rated that user didn't and recommend
        neighborRatings = users[the_nearest]
        userRatings = users[username]

        for artist in neighborRatings:
            if not artist in userRatings:
                recommendations.append((artist, neighborRatings[artist]))

        if recommendations:
            # using the fn sorted for variety - sort is more efficient
            return i, sorted(recommendations, key=lambda artistTuple: artistTuple[1],
                reverse = True)

    return i, None


def main():
    """
        check out some examples and compare

    """
    from data.user_data import users

    for x in ['Hailey', 'Chan', 'Sam', 'Dan', 'Jordyn', 'Bill', 'Angelica']:
        print "recommends for %s: \t\t%s  %s" % (x, "%s %s" % recommend(x, users), users[x])


if __name__ == '__main__':
    import os, sys
    path_to_project = '/'.join(os.path.realpath(__file__).split('/')[:-2])
    sys.path.append(path_to_project)
    main()
