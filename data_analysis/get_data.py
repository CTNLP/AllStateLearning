#!/usr/bin/env python
# encoding: utf-8
from models import Item
from utils import timespan, value_changed_counter, decissioness
import json


ALL_DATA = {
    'info': 'some info',
    'vector_fields': [],
    'user_ids_list': [],
    'data': {}
}


def update_all_data(userid, userdata):
    ALL_DATA['data'][userid] = userdata
    ALL_DATA['user_ids_list'].append(userid)


def process_user(id, userdata):
    user_vector = []
    the_matrix = [] # leave out of changes matrix ['customer_ID', 'shopping_pt', 'record_type', 
    field_names = userdata[0].field_names
    field_names_matrix = [x for x in field_names if x not in ['customer_ID', 'shopping_pt', 'record_type']]

    if not ALL_DATA['vector_fields']:
        for f in field_names_matrix:
            ALL_DATA['vector_fields'].append(f)
            ALL_DATA['vector_fields'].append("%s_chngd" % f)

    initial_time = None
    last_time = None
    for item in userdata:
        step_data = {}
        matrix = []
        for field in field_names:
            field_value = getattr(item,field)
            # TIMESTAMP as minutes instead of HH:MM
            if field == 'time':
                # use time passed from step to step or from point zero
                # and normalize to groups
                if user_vector:
                    # field_value = "%s" % (timespan(initial_time, getattr(item,field)))
                    field_value = "%s" % decissioness(timespan(last_time, getattr(item,field)))
                    last_time = getattr(item,field)
                else:
                    # initially timestamp
                    # field_value = "%s" % 0 
                    field_value = "%s" % decissioness(0) 
                    initial_time = getattr(item,field)
                    last_time = initial_time

            step_data[field] = {
                'value': field_value,
                'count': value_changed_counter(user_vector, field_value, field)
            }

        matrix = [(step_data[x]['value'], step_data[x]['count']) for x in field_names_matrix]
        the_matrix.append(matrix)
        user_vector.append(step_data)    


    user = {}
    for i, item in enumerate(userdata):
        vector = []
        for (value, changed) in the_matrix[i]:    
            try:
                value = int(value)
            except:
                pass
            vector.append(value)
            vector.append(changed)

        user[i+1] = json.dumps(vector)

    user['step_count'] = len(userdata)
    return (item.customer_ID, user) 


def read_and_index():
    """
        1. open unzipped csv data file ...train or test
        2. collect all steps for one user (userID) prepare stuff e.g NAs
        3. augment every step and index into elasticsearch

    """
    with open('../train.csv', 'r') as f:

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
                userid, userdata = process_user(this_customer_ID, customer_steps[this_customer_ID])                
                update_all_data(userid, userdata)                

            this_customer_ID = item.customer_ID
        
        # or the last line .. reached the end!
        userid, userdata = process_user(this_customer_ID, customer_steps[this_customer_ID])
        update_all_data(userid, userdata)
        

        ALL_DATA['user_ids_list'] = json.dumps(ALL_DATA['user_ids_list'])
        with open('the_data.json', 'w') as f:
            f.write(json.dumps(ALL_DATA, indent=4))

        # print customer_steps
        print 'cool'



if __name__ == '__main__':
    # index it
    read_and_index()