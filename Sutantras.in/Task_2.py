# 2. Task: List Manipulation
# Given a list of integers, write a function to return the sum of all even numbers in the list.
# Solution: Write a function that iterates through the list, checks if each element is even, and accumulates the sum of even numbers.

list1=[1,2,3,4,5,6,7]
print("Given list is : " , end=" ")
for i in list1:
    print(i,end=" ")

# function for sum of all even numbers
total = 0
def sum(l1):
    global total
    for i in list1 :
        if(i % 2 == 0):
            total+= i
    return total


addition=sum(list1)
print(f" \nSum of all even number from list is : {addition}")
