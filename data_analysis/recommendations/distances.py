#!/usr/bin/env python
# encoding: utf-8

"""
    Implementation of distance calculations:
    Manhatten, Euclidean, Minkowski

    If your data is dense (almost all attributes have non-zero values) and the
    magnitude of the attribute value is important, use distance measures such
    as Euclidean or Manhatten.

    The input are ratings from two different user and both as a dic of the form:
    {'The Strokes': 3.0, 'Slightly Stoopid': 2.5 ...

    based on the book of http://guidetodatamining.com/ (see Readme)
"""
from math import sqrt


def manhattan_distance(rating1, rating2):
    """
    abs(x1-x2) + abs(y1-y2) + ...
    """
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance


def euclidean_distance(rating1, rating2):
    """
    sqrt((x1-x2)**2 + (y1-y2)**2 ...)
    """
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += (rating1[key] - rating2[key])**2
    return "%0.2f" % sqrt(distance)


def minkowski_distance(rating1, rating2, r):
    """
    generalization of manhatten and euclidean distance
    manhatten distance: r = 1
    euclidean distance: r = 2
    supremum or chebyshev distance: r = ∞

    The greater the r, the more a large difference in
    one dimension will influence the total difference.

    """
    xy = [x for x in rating1 if x in rating2]

    sum = 0
    for key in xy:
        sum += abs(rating1[key] - rating2[key]) ** r

    return "%.2f" % pow(sum, 1.0/float(r))


def main():
    """
        check out some examples and compare

    """
    import json
    # from data.user_data import users
    # for (x, y) in [('Angelica', 'Bill'), ('Hailey', 'Veronica'),
    #     ('Hailey', 'Jordyn'), ('Angelica', 'Jordyn'), ('Hailey', 'Bill')]:


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

        man = manhattan_distance(p(user_data[x][step]),  p(user_data[y][step]))
        euc = euclidean_distance(p(user_data[x][step]),  p(user_data[y][step]))
        min1 = minkowski_distance(p(user_data[x][step]), p(user_data[y][step]), 1)
        min2 = minkowski_distance(p(user_data[x][step]), p(user_data[y][step]), 2)
        # min5 = minkowski_distance(p(user_data[x][step]), p(user_data[y][step]), 105)

        print "manhattan:     %s %s  %s  <" % (x, y, man)
        print "euclidean:     %s %s  %s <<" % (x, y, euc)
        print "minkowski r1:  %s %s  %s <" % (x, y, min1)
        print "minkowski r2:  %s %s  %s <<" % (x, y, min2)
        # print "minkowski r5:  %s %s  %s" % (x, y, min5)
        print


if __name__ == '__main__':
    import os, sys
    path_to_project = '/'.join(os.path.realpath(__file__).split('/')[:-2])
    sys.path.append(path_to_project)
    main()
