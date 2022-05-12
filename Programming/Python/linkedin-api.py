# Linkedin API
# pip install linkedin-api

# DOC: linkedin-api.readthedocs.io/en/latest/api.html

import json
from linkedin_api import Linkedin
import os

cwd = os.getcwd()

email = '' # Enter your email here
password = '' # Enter your password here
user = '' # Enter your username here

api = Linkedin(email,password)

decision = input(' A) Get profile from username\n B) Search School\n C) Search for people\n D) Search for Company\n')

if decision == 'A' or decision == 'a':
    username = input('Username: ')
    username_data = api.get_profile(username)
    print('\n', username_data)

    save = input('\nSave data? (y/n) ')
    file_name = input('\nFile name: ')
    if save == 'y' or save == 'Y':
        with open(f'{file_name}.json', 'w', encoding='utf-8') as d:
          json.dump(username_data, d, ensure_ascii=False, indent=4)
          print("\nData saved in: {0}".format(cwd)+f"\{file_name}.json\n") 
    else:
        pass
 
elif decision == 'B' or decision == 'b':
    school_name = input('School name: ')
    school_data = api.search_school(school_name)
    print('\n', school_data)

    save = input('\nSave data? (y/n) ')
    file_name = input('\nFile name: ')
    if save == 'y' or save == 'Y':
        with open(f'{file_name}.json', 'w', encoding='utf-8') as d:
          json.dump(school_data, d, ensure_ascii=False, indent=4)
          print("\nData saved in: {0}".format(cwd)+f"\{file_name}.json\n") 
    else:
        pass

elif decision == 'C' or decision == 'c':
    people_name = input('People name: ')
    people_data = api.search_people(people_name)
    print('\n', people_data)

    save = input('\nSave data? (y/n) ')
    file_name = input('\nFile name: ')
    if save == 'y' or save == 'Y':
        with open(f'{file_name}.json', 'w', encoding='utf-8') as d:
          json.dump(people_data, d, ensure_ascii=False, indent=4)
          print("\nData saved in: {0}".format(cwd)+f"\{file_name}.json\n")  
    else:
        pass

elif decision == 'D' or decision == 'd':
    company_name = input('Company name: ')
    company_data = api.search_company(company_name)
    print('\n', company_data)
    
    save = input('\nSave data? (y/n) ')
    file_name = input('\nFile name: ')
    if save == 'y' or save == 'Y':
        with open(f'{file_name}.json', 'w', encoding='utf-8') as d:
          json.dump(company_data, d, ensure_ascii=False, indent=4)
          print("\nData saved in: {0}".format(cwd)+f"\{file_name}.json\n")  
    else:
        pass
else:
    print('Invalid option')