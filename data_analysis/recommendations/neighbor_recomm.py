#!/usr/bin/env python
# encoding: utf-8
from distances import manhattan_distance
from distances import euclidean_distance
from distances import minkowski_distance
import json

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
                                     distance_algorithm='minkowski')

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

    return i, 'No recommendations'


def main():
    """
        check out some examples and compare

    """

    # from data.user_data import users
    # users = {
    #     "Angelica": {
    #         "Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5,
    #         "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5,
    #         "Vampire Weekend": 2.0},
    #     "Bill": {
    #         "Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0,
    #         "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},

    # for x in ['Hailey', 'Chan', 'Sam', 'Dan', 'Jordyn', 'Bill', 'Angelica']:
    #     print "recommends for %s: \t\t%s  %s" % (x, "%s %s" % recommend(x, users), users[x])
    users = {}

    with open('../the_data.json', 'r') as f:
        the_data = json.loads(f.read())

    user_data = the_data['data']
    the_users = json.loads(the_data['user_ids_list'])
    
    def p(vector):
        vector = json.loads(vector)
        return {field: vector[i] for i,field in enumerate(the_data['vector_fields'])}

    step = '1'
    users = {u: p(user_data[u][step]) for u in the_users}

    for user_id in the_users:        
        print user_id, recommend(user_id, users)        

    print 'what do expect to be recommended here?! ...but nice interface to the distances'


if __name__ == '__main__':
    import os, sys
    path_to_project = '/'.join(os.path.realpath(__file__).split('/')[:-2])
    sys.path.append(path_to_project)
    main()
