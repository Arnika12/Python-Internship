# 3. Task: String Reversal
# Write a Python function to reverse a string without using any built-in reverse functions.
# Solution: Create a function that iterates through the string in reverse order and builds a new string.

str1 = input("Enter a String : ")

def reversestring(str1):
    if(len(str1)==0):
        print("String is Empty")
    else:
        reverse_str1 = ""
        for i in range( len(str1)-1 , -1 , -1 ):     # start , end , step value(value decrement by 1)
            reverse_str1 += str1[i]
        return reverse_str1

reversed_str = reversestring(str1)
print("Original String:", str1)
print("Reversed String:", reversed_str)