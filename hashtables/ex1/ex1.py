#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    print(ht)
    # insert the weights of each item into ht where index is value
    for i in range(0, len(weights)):
        hash_table_insert(ht, weights[i], i)
        
    for i in range(0, len(weights)):
        query = limit - weights[i]
        # search in ht to find entries for `limit - weight` 
        answer_index = hash_table_retrieve(ht, query)
        if answer_index != None:
            answer_tuple = (max(i, answer_index), min(i, answer_index))
            return answer_tuple

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
