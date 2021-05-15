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
    print("Accessing a dict ","Name: ", dict['Name'], "Age: ", dict['Age'])
    
def updating_dict(dict):
    """
    Updating a dict by adding additional keys and values
    """
    dict['income_status'] = 'High'
    dict['Gender'] = 'Male'
    print("Updated the dict ",dict)
    

def get_keys_value_dict(dict):
    """
    Get keys and values of a dict
    """
    print("Fetching all the keys within a dict",dict.keys(),"\n")
    print("Fetching all the values within a dict", dict.values(),"\n")

def iterate_keys(dict):
    """
    Iterating through keys in a dict
    """
    for key in dict:
        print("Iterating all the keys within a dict",dict[key], "\n")
    

def iterate_items(dict):
    """Iterate over both key and values of a dict"""
    for key, value in dict.items():
        print("Key:", key,"-","Value:", value)

def iterate_values(dict):
    """iterate through list of values in a dict"""
    value = []
    for key in dict:
        value.append(dict[key])
    print("list of values in a dict", value)

def pop_item(dict):
    """deleting items from the dict"""
    dict.pop('Age')
    print(dict)


def delete_key(dict):
    """
    deleteing a key within a dict and poping out the last item
    """
    del dict['Gender']
    print(dict)
    
    print("deleted the last inserted item", dict.popitem())
    
    

def deleting_dict(dict):
    """
    Delete the entire dict
    """
    dict.clear()  
    print(dict)  


if __name__ == '__main__':
    dict = {'Name': 'Tom', 'Age': 17, 'Class': 'Second Year'}
    
    #Calling a list of functions using list comprehension
    functions = [accessing_dict,updating_dict,get_keys_value_dict,iterate_keys,iterate_items,iterate_values, pop_item, delete_key,deleting_dict]
    [function(dict) for function in functions]

   

    