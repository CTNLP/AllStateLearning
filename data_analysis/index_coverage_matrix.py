#!/usr/bin/env python
# encoding: utf-8
from elasticsearch import Elasticsearch
from esquery import Item
from utils import timespan
"""
    index the data

"""
es = Elasticsearch()

def doc_indexing(doc, id=None):
    """ indexing the user document into elasticsearch """
    ES_INDEX, ES_TYPE = "matrix", "user-data"
    doc = {'index': ES_INDEX, 'doc_type': ES_TYPE, 'body': doc}
    if id:
        doc['id'] = id 
    es.index(**doc)


def value_changed_counter(user_vector, item, field):
    if user_vector:
        if user_vector[-1][field]['value'] != getattr(item,field):
            return user_vector[-1][field]['count'] + 1
        else:
            return user_vector[-1][field]['count']
    else:
        return 0


def process_user(id, userdata):
    # print id, userdata

    user_vector = []

    the_matrix = [] # leave out of changes matrix ['customer_ID', 'shopping_pt', 'record_type', 

    field_names = userdata[0].field_names
    field_names_matrix = [x for x in field_names if x not in ['customer_ID', 'shopping_pt', 'record_type']]
    this_step = None
    initial_time = None

    for item in userdata:

        step_data = {}
        matrix = []

        for field in field_names:
            
            field_value = getattr(item,field)

            # TIMESTAMP as minutes instead of HH:MM
            if field == 'time':
                if user_vector:
                    # print 'rock', timespan(user_vector[-1][field]['value'], getattr(item,field))
                    field_value = "%s %s " % (timespan(initial_time, getattr(item,field)), getattr(item,field))
                else:
                    # initially timestamp
                    field_value = "%s %s " % (0, getattr(item,field)) 
                    initial_time = getattr(item,field)


            step_data[field] = {
                'value': field_value,
                'count': value_changed_counter(user_vector, item, field)
            }

        # matrix = [[step_data[x]['value'], step_data[x]['count']] for x in field_names_matrix]
        matrix = ["%s %s" % (step_data[x]['value'], step_data[x]['count']) for x in field_names_matrix]
        the_matrix.append(matrix)
        user_vector.append(step_data)    


        # print item.key_values()
        # if this_step != item.step and this_step:
        #     # coverage changed
        #     print item.step, item.record_type
        # else:
        #     # get step_reduce_vector


        # this_step = item.step


    # print the keys
    print ''.join(["%s. %s, " % ((i+1),k) for i,k in enumerate(field_names_matrix)])
    print 

    # the values of the vector
    for i,m in enumerate(the_matrix):
        if i == len(the_matrix)-1:
            print '-'*89
        # print "%s. \t\t" % i, ''.join(["%s. %s, \t" % ((in+1),k) for in,k in enumerate(m)])
        print "%s. \t\t" % i, ''.join(["%s, \t" % k for k in m])
    print 
    print 





def read_and_index():
    """
        1. open unzipped csv data file ...train or test
        2. collect all steps for one user (userID) prepare stuff e.g NAs
        3. augment every step and index into elasticsearch

    """
    with open('train.csv', 'r') as f:

        lines = f.readlines()
        field_names = [x.strip() for x in lines[0][:-1].split(',')] + ['step']        
        field_data = lines[1:]        

        customer_steps = {}
        this_customer_ID = None

        for line in field_data[0:200]:            
            item = Item(line, field_names)
            data = customer_steps.get(item.customer_ID, [])            
            data.append(item)
            customer_steps[item.customer_ID] = data

            if this_customer_ID != item.customer_ID and this_customer_ID:
                # print "last:%s, next:%s" % (this_customer_ID, item.customer_ID)
                # process all steps for the user and index
                process_user(this_customer_ID, customer_steps[this_customer_ID])


            this_customer_ID = item.customer_ID

        # print customer_steps
        print 'cool'



if __name__ == '__main__':
    # index it
    read_and_index()
