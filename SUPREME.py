#!/usr/bin/python
# -*- encoding: utf-8 -*-
import requests
import json
import sys
from termcolor import colored
from Supreme_Profiles import *

print(' ------------------------------')
print('|                              |')
print('|                              |')
print(colored('|'),colored('         NoobPreme','red',attrs=['bold','blink']), ('          |'))
print('|                              |')
print(colored('|'),colored('        Created By:','red'), ('         |'))
print(colored('|      '),colored('Oswaldo Argueta','red', attrs=['underline']), ('       |'))
print('|                              |')
print('|                              |')
print('|                              |')
print('|                              |')
print('|                              |')
print('|                              |')
print(' ------------------------------')

try:
    r = requests.get('https://www.supremenewyork.com/')
    print(colored('Connected To Supreme Succesful', 'green', attrs=['bold']))

except:

    print(colored('Cant Connect To Supreme', 'red',attrs=['bold']))


# Checking website response(current statues)-
#print(r.status_code) #>>200
#print(r.status_code == requests.codes.ok) #>> True
#print(requests.codes['temporary_redirect'])#>> 307
#print(requests.codes.teapot)#>> 418
#print(requests.codes['\o/']) #>>200
#print (r.text)

class main:
    def menu():

        while True:
            print('\n')
            print('Please enter the number that correspondes to the option you want.')
            print('(1)Tasks')
            print('(2)Create Tasks')
            print('(3)Profiles')
            print('(4)EXIT')

            choice = input()
            choice = int(choice)


            if choice == 1:
                print('You have decided to go to Tasks')

            elif choice == 2:
                print('You have decided to go to Create Tasks')

            elif choice == 3:
                #print('You have decided to go to Profiles')
                profiles.prompt()

            elif choice ==4:
                print('\n')
                print(colored('Termanating Supreme Bot...','red',attrs=['bold']))
                sys.exit()
            break
main.menu()
