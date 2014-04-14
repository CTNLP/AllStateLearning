

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









