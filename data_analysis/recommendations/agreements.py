#!/usr/bin/env python
# encoding: utf-8
"""
    based on the book of http://guidetodatamining.com/ (see Readme)

"""
from math import sqrt


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
    # from data.user_data import users
    # for (x, y) in [('Angelica', 'Bill'), ('Hailey', 'Veronica'),
    #     ('Hailey', 'Jordyn'), ('Angelica', 'Jordyn'), ('Hailey', 'Bill')]:

    users = {}
    import json
    with open('../data/user_queries.json', 'r') as f:
        users = json.loads(f.read())



    k = range(0, len(users))

    niceterms = []

    for x in k:
        for y in k:
            x = str(x)
            y = str(y)

            if x != y:
                # if pearson(users[x], users[y]) != 0:
                #     print 'pearson', x, y, pearson(users[x], users[y])
                try:
                    cos_sim_val = cosine_similarity(users[x]['qterms'], users[y]['qterms'])
                except:
                    cos_sim_val = 55

                if cos_sim_val > 0.98 and cos_sim_val < 1.0:
                    # print '------------------------------------------------'
                    # print 'cosin', x, y, cos_sim_val

                    for uxdq in users[x]['qdetails'].keys():
                        if uxdq in users[y]['qdetails']:

                            if uxdq not in niceterms:
                                niceterms.append(uxdq)

                            # print 'URL_DOMAIN'
                            # print users[x]['qdetails'][uxdq]['URL_DOMAIN']
                            # print users[y]['qdetails'][uxdq]['URL_DOMAIN']
                            # print

                            # print 'Clicks'
                            # print users[x]['qdetails'][uxdq]['Clicks']
                            # print users[y]['qdetails'][uxdq]['Clicks']

                    # print
            # print "pearson: %s %s %s" % (x, y, pearson(users[x], users[y]))
            # print "cosine:  %s %s %s" % (x, y, cosine_similarity(users[x], users[y]))
            # print
    yield niceterms


if __name__ == '__main__':
    import os, sys
    path_to_project = '/'.join(os.path.realpath(__file__).split('/')[:-2])
    sys.path.append(path_to_project)
    for x in main():
        print x
