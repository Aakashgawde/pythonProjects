import random

#* Import special character

from string import punctuation

#* Create a list with all these special characters in 
special_char = list(punctuation)


print(len(special_char)) #* there are 32 elements in the list

#* Example - Random password genertator with special character
password = ''
for i in range(5):
    #* produces random uppercase letter
    a = chr(random.randint(65,90)) 
    #* produces random lowercase letter
    b = chr(random.randint(65,90)).lower() 
    #* produces a special character 
    c = special_char[random.randint(0,31)] 
    password = password + a + b + c

print(password)

#* Shuffle the password you have - doesn't  follow uppercase,lowercase,spc char structure.
print(''.join(random.sample(password,len(password))))



