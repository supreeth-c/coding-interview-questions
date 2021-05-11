"""
Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. 
That makes accessing the data faster as the index value behaves as a key for the data value. In other words Hash table stores key-value pairs but the key is generated through a hashing function.

So the search and insertion function of a data element becomes much faster as the key values themselves become the index of the array which stores the data.

In Python, the Dictionary data types represent the implementation of hash tables. The Keys in the dictionary satisfy the following requirements.

The keys of the dictionary are hashable i.e. the are generated by hashing function which generates unique result for each unique value supplied to the hash function.

The order of data elements in a dictionary is not fixed

"""

def accessing_dict(dict):
    """
    access name and age
    """
    print("Name: ", dict['Name'], "Age: ", dict['Age'])
    
def updating_dict(dict):
    pass

def deleting_dict(dict):
    pass

def iterate_keys(dict):
    pass

def iterate_items(dict):
    pass

def iterate_values(dict):
    pass

def modifying_values_keys(dict):
    pass

if __name__ == '__main__':
    dict = {'Name': 'sumayann', 'Age': 17, 'Class': 'Second Year'}
    print(dict)
    accessing_dict(dict)
    

    