# Importing the relevant modules
import random
from random import randint
# # All uppercase password
# password = ""
# for i in range(10):
#     i = chr(random.randint(65,90))
#     password = password + i
# print(password)

#------------------------------------------------------------------------------------------------------------------------
# Upper and lowercase password
password = ""
for i in range(8):
    #* produces random uppercase letter
    i = chr(random.randint(65, 90))
    #* produces random lowercase letter
    j = chr(random.randint(65, 90)).lower()
    password = str(password) + i + j
print(password)

#! randint()--> The randint() method returns an integer number selected element from the specified range.s