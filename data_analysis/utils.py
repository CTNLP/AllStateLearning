#!/usr/bin/env python
# encoding: utf-8
from string import letters
from dateutil import parser


def normalize_people_age(age):
    """
        add age into a slice of ages to reduce amount of different values
        may better by hand [21, 31, 51, 71, 100] ...we will see
    """
    # for g in range(16, 100, 20):
    age = int(age)
    for g in [25, 40, 60, 100]:
        if age < g:
            return g    


def normalize_car_age(age):
    """
    """
    age = int(age)
    for g in [2, 4, 8, 16, 32, 64, 128]:
        if age < g:
            return g    


def step_reduce(counter, steps, step):
    # reduce the steps to real changes, but count            
    if steps:
        if steps[-1] != step:
            steps.append(step)
    else:
        steps.append(step)
    return counter + 1, steps


NAN_VALUES = {
    'C_previous': 5,
    'duration_previous': 16,
    'risk_factor': 5,
    'car_value': 'z',
    'location': 55555
    }

def nan(value, name):
    try:
        value = int(value)
    except:
        if value == '' or value == 'NA':
            value = NAN_VALUES[name]                
    return value


def l2n(value):
    number = ''.join([str(letters.index(l)) for l in list(value)])   
    return number


def timespan(first, second):
    time1 = parser.parse(first)
    time2 = parser.parse(second)
    return (time2-time1).seconds/60 


def print_facets(field, response, tab=1):    
    data = ["%s%s:%s" % ("\t"*tab, field, ' '*(16-len(field)))]
    list_of_facetterms2 = response['facets'][str(field)]['terms']
    for x in list_of_facetterms2:
        data.append(" %s: %s," % (x['term'], x['count']))
    return ''.join(data)[:-1]


if __name__ == '__main__':
    print normalize_age(17)