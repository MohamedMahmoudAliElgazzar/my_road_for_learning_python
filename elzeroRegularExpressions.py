# ################
# ######96########
# ################
# #regular Expressions
# """
# this is the code that you find how to handle with regular expressions
# """
# #https://pythex.org/
# #https://www.w3schools.com/python/python_regex.asp
# #\d degit 
# ################
# ######97########
# ################
# #regex101.com
# ################
# ######98########
# ################
# ################
# ######99########
# ################
# # | or 
# # \ escape
# #() groups
# #(\d-|\d\)|\d\>)(\w+)
# ################
# ######100#######
# ################
# # ---------------------------------------------------------
# # -- Regular Expressions => Re Module Search And FindAll --
# # ---------------------------------------------------------
# # search()  => Search A String For A Match And Return A First Match Only
# # findall() => Returns A List Of All Matches and Empty List if No Match
# # ---------------------------------------------------------------------
# # Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# # ----------------------------------------------------------

# import re

# my_search = re.search(r"[A-Z]{2}", "OOsamaEElzero")

# print(my_search)
# print(my_search.span())
# print(my_search.string)
# print(my_search.group())

# is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@osama.com")

# if is_email:

#   print("This is A Valid Email")

#   print(is_email.span())
#   print(is_email.string)
#   print(is_email.group())

# else:

#   print("This is Not A Valid Email")

# email_input = input("Please Write Your Email: ")

# search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

# empty_list = []

# if search != []:

#   empty_list.append(search)

#   print("Email Added")

# else:

#   print("Invalid Email")

# for email in empty_list:

#   print(email)
import re
sting_one="I Love Python"
search_one= re.split(r"\s",sting_one, 1)
print(search_one)
print('#'*55)
string_two="how-To_Write_a_Very-Good-Article"
search_two=re.split(r"-|_",string_two)
print(search_two)
print('#'*55)
for counter, word in enumerate(search_two,1):
    if len(word)==1:
        continue
    print(f'Word Number: {counter} => {word.lower()}')
    
print('#'*55)

print(re.sub(r'\s',"-","I love python"))
