#!/usr/bin/env python
# encoding: utf-8
from utils import normalize_people_age, normalize_car_age
from utils import nan, l2n




class Query(object):

    query = {"size": 0}
    # no query given is like default {"match_all" : {}}

    def add_facet(self, key, field, size=10):
        self.query["facets"] = {key: {"terms": {"field": field, "size": size}}}



    # def add_aggs(self, key, field):
    #     self.query["aggregations"] = item['{key: {"sum": {"field": option}}}

    def add_query(self, a_query):
        self.query["query"] = a_query

    def reset_query(self):
        self.query = {"size": 0}

    def the_query(self):
        return self.query


class QueryResponse(object):

    def __init__(self, arg):        
        self.response = arg

    def get_facets(self, key):
        return self.response["facets"][key]["terms"]

        
class Item(object):
    def __init__(self, line, field_names):

        step_values = line[:-1].split(',')
        item = {name: value for (name, value) in zip(field_names, step_values)}

        # A unique identifier for the customer
        self.customer_ID = item['customer_ID']

        # Unique identifier for the shopping point of a given customer
        self.shopping_pt = item['shopping_pt']

        # 0=shopping point, 1=purchase point
        self.record_type = item['record_type']

        # Day of the week (0-6, 0=Monday)
        self.day = item['day']

        # Time of day (HH:MM)
        self.time = item['time']

        # State where shopping point occurred
        self.state = l2n(item['state'])

        # Location ID where shopping point occurred
        self.location = nan(item['location'], 'location')

        # How many people will be covered under the policy (1, 2, 3 or 4)
        self.group_size = item['group_size']

        # Whether the customer owns a home or not (0=no, 1=yes)
        self.homeowner = item['homeowner']

        # Age of the customer’s car
        self.car_age = normalize_car_age(item['car_age'])

        # How valuable was the customer’s car when new
        self.car_value = l2n(nan(item['car_value'], 'car_value'))

        # An ordinal assessment of how risky the customer is (1, 2, 3, 4)
        self.risk_factor = nan(item['risk_factor'], 'risk_factor')

        # Age of the oldest person in customer's group
        self.age_oldest = normalize_people_age(item['age_oldest'])

        # Age of the youngest person in customer’s group
        self.age_youngest = normalize_people_age(item['age_youngest'])

        # Does the customer group contain a married couple (0=no, 1=yes)
        self.married_couple = item['married_couple']

        # What the customer formerly had or currently has for product option C (0=nothing, 1, 2, 3,4)
        self.C_previous = nan(item['C_previous'], 'C_previous')

        # how long (in years) the customer was covered by their previous issuer
        self.duration_previous = nan(item['duration_previous'], 'duration_previous')

        # the coverage options
        self.A = item['A'].strip()
        self.B = item['B'].strip()
        self.C = item['C'].strip()
        self.D = item['D'].strip()
        self.E = item['E'].strip()
        self.F = item['F'].strip()
        self.G = item['G'].strip()

        # cost of the quoted coverage options
        self.cost = item['cost']

        self.field_names = field_names

        # extra data, different format
        options = [self.A, self.B, self.C, self.D, self.E, self.F, self.G] 

        self.step = ''.join([str(x) for x in options])

        # item['step'] = self.step

    # def keys(self):
    #     return [x for x in self.field_names]

    def keys(self):
        return [getattr(self,x) for x in self.field_names]

    def key_values(self):
        return {x:getattr(self,x) for x in self.field_names}

    def compact(self):
        return {self.customer_ID: {self.shopping_pt: self.key_values()}}


class User(object):
    def __init__(self, user_id, items):
        self.user_id = user_id
        ## process all steps: the list of items
        # for item in items: 

        # check the 'coverage options', check if user switch his data around
        # and what in each step
        # represent the reduced steps ...short path kind of 









