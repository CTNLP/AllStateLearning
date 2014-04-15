#!/usr/bin/env python
# encoding: utf-8
from string import letters
from dateutil import parser
import json


def decissioness(timeinminutes):
    if timeinminutes < 2:
        return 1
    elif timeinminutes < 5:
        return 2
    elif timeinminutes < 15:
        return 3
    elif timeinminutes < 60:
        return 4
    else:
        return 5

def value_changed_counter(user_vector, thisfieldvalue, field):
    if user_vector:
        if user_vector[-1][field]['value'] != thisfieldvalue:
            return user_vector[-1][field]['count'] + 1
        else:
            return user_vector[-1][field]['count']
    else:
        return 0


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



def get_field_and_value(data, fieldname, to=1, examples=5):
    # get position of the field and extract
    fromindex = data['vector_fields'].index(fieldname)
    info = {
        'fields': data['vector_fields'][fromindex:(fromindex+to)]
    }
    for userid in json.loads(data['user_ids_list'])[0:examples]:
        info[userid] = []
        for x in range(1, data['data'][userid]['step_count']):
            vector = json.loads(data['data'][userid][str(x)])
            info[userid].append(vector[fromindex:(fromindex+to)])
    return info




if __name__ == '__main__':
    print normalize_age(17)

    with open('the_data.json', 'r') as f:
           data = json.loads(f.read())   
    print get_field_and_value(data, 'time', to=2)
    # print get_field_and_value(data, 'C_previous', to=4, examples=1)



