import json
import random


with open('the_data.json', 'r') as f:
    data = json.loads(f.read())
    user_ids_list = json.loads(data['user_ids_list'])

    for_testing = len(user_ids_list) / 100 * 30
    test_ids = random.sample(user_ids_list, for_testing)
    train_ids = list(set(user_ids_list) - set(test_ids))

    print len(test_ids), len(train_ids)

    # create test and train data
    # remove the shopping (last) step at test set
    