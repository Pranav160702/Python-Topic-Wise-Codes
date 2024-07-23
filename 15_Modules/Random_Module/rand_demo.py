import random 

random.seed(0)

# for _ in range(5):
#     print(random.random())

# print()
# random.seed(1)
# for _ in range(5):
#     print(random.random())

# print()
# random.seed(None)
# for _ in range(5):
#     print(random.random())



# # ===============================
# # random.randrange()
# # ===============================
# for _ in range(5):
#     print(random.randrange(10))
#     # print(random.randrange(1, 10))
#     # print(random.randrange(1, 10, 2))


# #==================================
# # random.randint()
# #==================================
# for _ in range(5):
#     # print(random.randint(1, 10))
#     print(random.randint(1,10))


# #==================================
# # random.choice()
# #==================================
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(random.choice(my_list))



# ==================================
# random.choices()
# ==================================
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choices(my_list, k=5))
print(random.choices(my_list, k=3))




#==================================
# random.sample()
#==================================
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(random.sample(my_list, 3))


# #==================================
# # random.shuffle()
# #==================================
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Before Shuffling:",my_list)
# random.shuffle(my_list)
# print("After Shuffling:",my_list)

