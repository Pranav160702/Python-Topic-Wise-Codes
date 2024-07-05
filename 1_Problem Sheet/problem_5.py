# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
# For example, if the number is 1234, the reverse is 4321. 

# def reverse_num(num):
#     rev = 0
#     if(1000 <= num <= 9999):
#         original_num = num
#         while num > 0:
#             rev = rev * 10 + num % 10 
#             num //= 10
       
#         if(original_num == rev):
#             return("The reverse is true")
#         else:
#             return rev
#     else:
#         return("Invalid Number, please Enter Valid Number")
    
def reverse_num(num):
    if(1000 <= num <= 9999):
        rev = int(str(num)[::-1])

        if(num == rev):
            return("The reverse is true")
        else:
            return rev
    else:
        return("Invalid Number, please Enter Valid Number")
    
    
num = int(input("Enter The Number:"))
print("The Reverse Number Is: ",reverse_num(num))
