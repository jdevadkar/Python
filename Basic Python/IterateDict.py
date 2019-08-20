dict ={ 'id' :01 , 'name' :'Ram', 'department' : 'IT' }

#Iterate over a key
for key in dict:
    print(key)

#Iterate through all values
for values in dict.values():
    print(values)
    
# Iterate through all key, value pairs
for keys, values in dict.items():
    print(keys, ':' ,values)
