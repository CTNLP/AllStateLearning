#!/usr/bin/env python
# encoding: utf-8
from elasticsearch import Elasticsearch
from utils import normalize_people_age
from utils import normalize_car_age
from utils import step_reduce
"""
    index the data

"""
# replace NAN or '' values with the highest value in this field + 1
# or a dummy as for car_value and location
NAN_VALUES = {
    'C_previous': 5,
    'duration_previous': 16,
    'risk_factor': 5,
    'car_value': 'z',
    'location': 55555
    }
COVERAGE_OPTIONS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

es = Elasticsearch()


def doc_indexing(doc, id=None, reformat=False):    
    """ indexing the user document into elasticsearch 
    """
    ES_INDEX = "matrix"
    ES_TYPE = "user-data"
    if reformat:
        if id:
            doc = {'index': ES_INDEX, 'id': id, 'doc_type': ES_TYPE, 'body': doc}
        else:
            doc = {'index': ES_INDEX, 'doc_type': ES_TYPE, 'body': doc}
    es.index(**doc)


def read_and_index():
    """
        1. open unzipped csv data file ...train or test
        2. collect all steps for one user (userID) prepare stuff e.g NAs
        3. augment every step and index into elasticsearch

    """
    with open('train.csv', 'r') as f:
        lines = f.readlines()

        field_names = [x.strip() for x in lines[0][:-1].split(',')]        
        field_data = lines[1:]        
        steps, counter, coverage_opts, some_values = [], 0, {}, {}

        for i,line in enumerate(field_data):

            step_values = line[:-1].split(',')

            for (name, value) in zip(field_names, step_values):

                # change values to int or replace the unknowns to an extra
                # category e.g. 'risk_factor' values from 1-4 and if unknown 5
                try:
                    value = int(value)
                except:
                    if value == '' or value == 'NA':
                        value = NAN_VALUES[name]                

                # reduce to groups of range or prettify some values
                # e.g. range of age (car|youngest..)  



                if name == 'age_youngest' or name == 'age_oldest':
                    if name not in some_values:
                        some_values[name] = normalize_people_age(value)

                if name == 'group_size':
                    some_values[name] = value 

                if name == 'married_couple':
                    some_values[name] = value 

                if name == 'state':
                    some_values[name] = value 




                # collect values of the coverage options A, B, C, D ...
                if name in COVERAGE_OPTIONS:
                    coverage_opts[name] = value



            step = ''.join([str(coverage_opts[x]) for x in COVERAGE_OPTIONS])

            if step_values[2] == '1':
                # step_values[2] shopping_pt = 1 this point is not available
                # in the testdata!

                # print some_values
                item = {k:v for k, v in some_values.iteritems()}

                counter, steps = step_reduce(counter, steps, step)
                item['steps'] = counter
                # item = {'steps': counter + 1} do not count the shopping_pt
                # in respect to the testdata, but index it
                item['shopping_pt_step'] = counter + 1

                for i, val in enumerate(steps):
                    item[i] = val
                doc_indexing(item, id=step_values[0], reformat=True)
                steps, coverage_opts, counter, some_values = [], {}, 0, {}

            else:
                counter, steps = step_reduce(counter, steps, step)
                coverage_opts = {}
            

if __name__ == '__main__':
    # index it
    read_and_index()
