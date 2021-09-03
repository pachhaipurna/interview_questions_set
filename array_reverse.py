#Program to reverse the array in python 

#using while loop\
given_array =['12','23','4','6','67','98','34','11','125','16']


print("Originalgiven array items are = ", given_array)

j = len(given_array) - 1
i = 0

while(i < j):
    temp = given_array[i]
    given_array[i] = given_array[j]
    given_array[j] = temp
    i += 1
    j -= 1

print("After Reversing Array = ", given_array)


#using for loop

