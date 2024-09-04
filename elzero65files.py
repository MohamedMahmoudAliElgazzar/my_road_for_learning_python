# # # #######################
# # # #######video 65########
# # # #######################
# # # # import os

# # # # print(os.getcwd())
# # # # #change current working dir
# # # # os.chdir(os.path.dirname(os.path.abspath(__file__)))
# # # # print(os.path.dirname(os.path.abspath(__file__)))

# # # file = open('osama.txt')
# # # # # #######################
# # # # # #######video 66########
# # # # # #######################
# # myfile=open('osama.txt')

# # # print(myfile)
# # # print(myfile.read())

# # # print(myfile.readline())

# # # print(myfile.readlines())

# # for line in myfile:
# #     print(line)
# #     if line.startswith('07'):
# #         break
# # #close the file
# # myfile.close()
# # # #######################
# # # #######video 67########
# # # #######################
# # myfile.write('hello from python file with love \n')
# # myfile.write('this is the second line \n')
# # myfile.write('elzero web school \n '*100)
# mylist=['2','34','5','6','7','7','8']
# myfile=open('mohamed.txt','w')

# myfile.writelines(mylist)
# myfile.write('\n hi \n my name is mohamed\n I love programming\n and hacking \n this is so fun')
# #######################
# #######video 68########
# #######################
# myfile=open('mohamed.txt','a')
# myfile.truncate(5)
# myfile=open('mohamed.txt','r')
# # print(myfile.tell())
# myfile.seek(11)
# print(myfile.read())
#_____________________________________

import os
os.remove('osama.txt')
