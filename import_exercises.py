# Import Exercises 01-24
# Madeleine Capper
# 
# Create a file named import_exercises.py or a notebook named import_exercises.ipynb to do your work in.
# 
#     Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
# 
# see iPython sesh
# 
# Create a file named import_exericses.py. Within this file, 
# use from to import the calculate_tip function directly. 
# Call this function with values you choose and print the result.
from function_exercises import calculate_tip
print(f'Q: How much to tip on a bill of $100.00 if we want to tip 20%? A: {calculate_tip(0.2, 100.00)}')

#     Create a jupyter notebook named import_exercises.ipynb. 
# Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.
# 
# print(f'The grade of 87 is {####} in letter-grade format')


#     2. For this exercise, read about and use the itertools module
#       
    # How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools
print('Number of combinations in a,b,c to 1,2,3')
print(len(list(itertools.product('abc', '123'))))

    # How many different combinations are there of 2 letters from "abcd"?
len_combos = len(list(itertools.combinations('abcd', 2)))
print(f'There are {len_combos} ways to combine abcd in pairs')
    # How many different permutations are there of 2 letters from "abcd"?
len_perms = len(list(itertools.permutations('abcd', 2)))
print(f'There are {len_perms} ways to permute abcd in pairs')

# 3. Save this file as profiles.json inside of your exercises directory.
#    Use the load function from the json module to open this file,
#    it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
import json
with open('profiles.json', 'r') as f:
    profiles = json.load(f)
# 
numusers = len(profiles)
#         - Total number of users
print(f'Total number of users in profiles: {numusers}')
#         - Number of active users
active_accounts = [accnt for accnt in profiles if accnt['isActive']]
print(f'Total number of active users in profiles: {len(active_accounts)}')
#         - Number of inactive users
inactive_users = []
for accnt in profiles:
    if not accnt['isActive']:
        inactive_users.append(accnt)
print(f'Total number of inactive users in profiles: {len(inactive_users)}')
#         - Grand total of balances for all users
bal_list = []
for accnt in profiles:
    bal_list.append(float(accnt['balance'][1:].replace(',','')))
total_balances = sum(bal_list)
print(f'Total balance in users: ${total_balances}')
#         - Average balance per user
avg_balance = total_balances / numusers
print(f'Average balance in users: ${avg_balance:.6}')
#         - User with the lowest balance
for accnt in profiles:
    if float(accnt['balance'][1:].replace(',','')) == min(bal_list):
        min_bal_usr = accnt['name']
print('User with minimum balance: ', min_bal_usr)
# 
#         - User with the highest balance
# 
max_user = {}
for accnt in profiles:
    if float(accnt['balance'][1:].replace(',','')) == max(bal_list):
        max_user = accnt['name']
print(f'User with maximum account balance: {max_user}')
# 
#         - Most common favorite fruit
# 
all_fruits = [accnt['favoriteFruit'] for accnt in profiles]

def fruit_counts(fruitlist):
    '''
    counts the number of each item in a list of strings and 
    returns a dictionary of the counts of each item
    '''
    fruit_counts = {}
    for fruit in fruitlist:
        if fruit not in fruit_counts.keys():
            fruit_counts[fruit] = 1
        else:
            fruit_counts[fruit] = fruit_counts[fruit] + 1
    return fruit_counts

fruitcount_dict = fruit_counts(all_fruits)
fave_fruit = [fruit for fruit in fruitcount_dict \
    if fruitcount_dict[fruit] == max(fruitcount_dict.values())][0]
print(f'Most popular fruit: {fave_fruit}')
# 
#         - Least most common favorite fruit
# 
# without list comprehension:
# initialize least favorite fruit as an empty string
least_fave_fruit = ''
for k, v in fruitcount_dict.items():
    if v == min(fruitcount_dict.values()):
        print('least favorite fruit: ',k)

#         - Total number of unread messages for all users
list_comp_all_unreads = sum([int(''.join([val for val in accnt['greeting'] if val.isdigit()])) for accnt in profiles])
# 
# breaking it down:
# 
# single greeting value:
profiles[0]['greeting']
# pulling out the digits from that greeting into a list:
digit_list = []
for letter in profiles[0]['greeting']:
    if letter.isdigit():
        digit_list.append(letter)
# this gives us a digit list that looks like ['4'] or like ['1','9'] -- we want a single int.
# to join the list, we use the join string method
digit_as_string = ''.join(digit_list)
# finally we want to cast it to an integer data type
digit = int(digit_as_string)
# Now, we want to do this for every account in the profile
list_of_unread_messages = []
for accnt in profiles:
    # do everything we just did for every dictionary referenced here as accnt
    digit_list = []
    for letter in accnt['greeting']:
        if letter.isdigit():
            digit_list.append(letter)
    digit_as_string = ''.join(digit_list)
    digit = int(digit_as_string)
    list_of_unread_messages.append(digit)

# and to get all unread messages, just call sum()
all_unread_messages = sum(list_of_unread_messages)
print(f'Total unread messages: {all_unread_messages}')