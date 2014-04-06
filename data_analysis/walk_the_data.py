from elasticsearch import Elasticsearch
es = Elasticsearch()
from esquery import Query, QueryResponse



# initally get facets for all combinations
q = Query()
q.add_facet('step_0', '0')
response = es.search(index="matrix", body=q.the_query())
r = QueryResponse(response)








def get_data_for(step, terms):
    q = Query()

    bool_must = []
    for i,term in enumerate(terms):
        bool_must.append({'term': {i: term}})
    q.add_query({'bool': {'must': bool_must}})    
  
    next_step = step + 1
    next_step_key = 'step_%s' % next_step
    q.add_facet(next_step_key,  next_step, size=10)

    # print next_step_key, q.the_query()

    response = es.search(index="matrix", body=q.the_query())
    
    # print response

    r = QueryResponse(response)
    return r.get_facets(next_step_key)






for option in r.get_facets('step_0'):

    option_term = option['term']
    print 
    print option_term


    bool_must = []
    terms = [option_term]

    for step in range(0, 20):
        response_facets = get_data_for(step, terms)
        if response_facets:
            terms.append(response_facets[0]['term'])
            print response_facets
        else:
            continue



        print '\t'*(step+1), 'step:', step,', next term:', terms[-1]



























