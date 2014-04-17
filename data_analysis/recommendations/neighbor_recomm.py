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



def main():
    """
        check out some examples and compare

    """
    users = {}

    with open('../the_data.json', 'r') as f:
        the_data = json.loads(f.read())

    user_data = the_data['data']
    the_user_ids = json.loads(the_data['user_ids_list'])
    
    def p(vector):
        vector = json.loads(vector)
        return {field: vector[i] for i,field in enumerate(the_data['vector_fields'])}

    result = {}
    for step in range(1, 20):
        step = str(step)

        users = {}
        the_user_ids_for_this_step = []
        for uid in the_user_ids:
            try:
                users[uid] = p(user_data[uid][step])
                the_user_ids_for_this_step.append(uid)                
            except:
                pass

        for user_id in the_user_ids_for_this_step:        
            nearest = computeNearestNeighbor(user_id,
                                             users,
                                             distance_algorithm='minkowski')
            # print user_id
            if user_id not in result:
                result[user_id] = {}

            result[user_id][step] = nearest[:3]



    # print result

    for u in result.keys():
        woha = []
        print '%s, step_count: %s' % (u, user_data[u]['step_count'])
        ls = result[u].keys()
        ls.sort()
        for s in ls: 
            print s
            for near in result[u][s]:
                if near[1] in woha:
                    ulala = '>'*woha.count(near[1])
                else:
                    ulala = ''
                woha.append(near[1])
                print '\t'*int(s), '%s %s, %s, step_count: %s' % (ulala, near[1], near[0], user_data[near[1]]['step_count'])

        print


if __name__ == '__main__':
    import os, sys
    path_to_project = '/'.join(os.path.realpath(__file__).split('/')[:-2])
    sys.path.append(path_to_project)
    main()
