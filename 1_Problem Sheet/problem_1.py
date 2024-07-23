# User will input (3ages).Find the oldest one

# Taking inputs for user
person_one = int(input("Enter Age of First Person: "))  
person_two = int(input("Enter Age of Second Person: "))
person_three = int(input("Enter Age of Third Person: "))


# # 
# # First Approach(Nested If-Else Statements)
# # =============================================
# # Time & space Complexity --> O(1)
# # 

# if(person_one > person_two):
#     if(person_one > person_three):
#         print("Oldest Person is First Person")
#     else:
#         print("Oldest Person is Third Person")
# elif(person_two > person_three):
#     print("Oldest Person is Second Person")
# else:
#     print("Oldest Person is Third Person")



# # 
# # Second Approach(Using max function and If-Else Statements)
# # ==============================================
# # Time & space Complexity --> O(1)
# # 

# oldest_person = max(person_one,person_two, person_three)

# if(oldest_person == person_one):
#     print("Oldest Person is First Person")
# elif(oldest_person == person_two):
#     print("Oldest Person is Second Person")
# else:
#     print("Oldest Person is Third Person")



# # 
# # Third Approach(Using max function and Dictionary)
# # ==============================================
# # Time & space Complexity --> O(1)
# # 

ages = {"First":person_one, "Second":person_two,"Third":person_three}

oldest_person = max(ages, key = ages.get)

print(f"Oldest person is {oldest_person} Person ")
