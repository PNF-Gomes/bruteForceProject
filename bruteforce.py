import time
from getpass import getpass
print("Welcome to super safe application")

i = 0

user_name = input("Escolha o username\n")
password = getpass() + "\n"

print("A carregar lista de passwords...")
time.sleep(10)


pass_word = []
with open('pass.txt') as my_file:



    for line in my_file:
        pass_word.append(line)


while pass_word[i] != password:
    time.sleep(0.001)
    print("admin:"+ user_name)
    print('password:'+ pass_word[i-1])


    if pass_word[i] == '/0\n':
        print("password Not Found")
        break
        
    i = i + 1

if pass_word[i] == password:
    print("Found")
    find = pass_word[i]
    print("The password is " + pass_word[i])



