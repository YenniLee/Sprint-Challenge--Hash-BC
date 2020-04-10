#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length -1)

    # insert ticket info into ht
    for i in range(0, len(tickets)):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    source = 'NONE'

    for i in range(len(route)):
        source = hash_table_retrieve(hashtable, source)
        if source != 'NONE':
            route[i] = source

    return route