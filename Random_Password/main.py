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
for i in range(5):
    i = chr(random.randint(65, 90))
    j = chr(random.randint(65, 90)).lower()
    password = str(password) + i + j
print(password)

