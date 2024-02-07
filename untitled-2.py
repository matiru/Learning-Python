from random import randint ,choice

password = 'HUNTING'
size = 20
fill = '!@#$%*&()-+=~[]{}^'
embedding =''
embedding2 = ''
password_size = len(password)
split_index =  randint(0,size-password_size)
for index in range(0,split_index): 
    embedding =  embedding + choice(fill)
password = str(embedding)+str(password) 

for index in range(0,size-len(password)):
    embedding2 =  embedding2 + choice(fill)
print(embedding2)
password =str(password) +str(embedding2)
print(password)