# Created List
list = [1,4,3,2,78,9,5,6,7]

# iterate list using for loop
print("**********using for loop************")
for i in list:
    print(i)

# For loop and range method
print("********* For loop and range method*************")
length =len(list)
for i in range(length):
    print(list[i])

# Using while loop
print("**********Using while loop************")
i =0
while i < length:
    print(list[i])
    i +=1

# Using list comprehension
print("********Using list comprehension**********")
#[print(i) for i in list]

# using enumarate method
print("*******using enumerate method*************")
for i, val in enumerate(list):
    print(i,"," ,val)