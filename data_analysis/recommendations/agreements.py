#!/usr/bin/env python
# encoding: utf-8
"""
    based on the book of http://guidetodatamining.com/ (see Readme)

"""
from math import sqrt
import json


def pearson(rating1, rating2):
    # print rating1, rating2
    """
        Find similiar persons based on their ratings.

        If the data is subject to grade-inﬂation (different users
        may be using different scales) use Pearson.
        It ranges between -1 and 1 inclusive. 1 indicates perfect agreement.
        -1 indicates perfect disagreement.
    """
    # get all keys which are in both ratings
    keys = [key for key in rating1 if key in rating2]

    n = len(keys)
    rat1 = []
    rat2 = []

    for key in keys:
        rat1.append(rating1[key])
        rat2.append(rating2[key])

    sum_x = sum(rat1)
    sum_x2 = sum([x**2 for x in rat1])
    sum_y = sum(rat2)
    sum_y2 = sum([y**2 for y in rat2])

    if sum_x == 0:
        return 0
    else:
        denominator = sqrt(sum_x2 - (sum_x**2) / n) * sqrt(sum_y2 - (sum_y**2) / n)

        if denominator == 0:
            return 0
        else:
            sum_xy = sum([a*b for a,b in zip(rat1,rat2)])
            return (sum_xy - (sum_x * sum_y) / n) / denominator


def cos_of(vec_x, vec_y):
    card_x = sqrt(sum([x**2 for x in vec_x]))
    card_y = sqrt(sum([y**2 for y in vec_y]))
    product = sum([a*b for a,b in zip(vec_x,vec_y)])
    return product / (card_x * card_y)


def cosine_similarity(rating1, rating2):
    """
        The cosine similarity rating ranges from 1 indicated perfect
        similarity to -1 indicate perfect negative similarity.

        If the data is sparse consider using Cosine Similarity.
    """

    r1 = rating1.keys()
    r2 = rating2.keys()

    allkeys = list(set(r1 + r2))
    n = len(allkeys)

    # create the vectors
    rv1 = [0]*n
    rv2 = [0]*n
    for i, k in enumerate(allkeys):
        if k in rating1: rv1[i] = rating1[k]
        if k in rating2: rv2[i] = rating2[k]

    # return the cosine sim value
    return cos_of(rv1, rv2)


def main():
    """
        check out some examples and compare

    """
    with open('../the_data.json', 'r') as f:
        the_data = json.loads(f.read())

    user_data = the_data['data']
    the_users = json.loads(the_data['user_ids_list'])
    some = [(the_users[0], other) for other in the_users] 

    def p(vector):
        vector = json.loads(vector)
        return {field: vector[i] for i,field in enumerate(the_data['vector_fields'])}

    step = '1'

    for (x, y) in some:
        print "pearson: %s %s %s" % (x, y, pearson(p(user_data[x][step]), p(user_data[y][step])))
        print "cosine:  %s %s %s" % (x, y, cosine_similarity(p(user_data[x][step]), p(user_data[y][step])))



if __name__ == '__main__':
    import os, sys
    path_to_project = '/'.join(os.path.realpath(__file__).split('/')[:-2])
    sys.path.append(path_to_project)
    main()
