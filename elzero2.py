# name ="mohamed"
# print("s"in name)

print("#" * 50)


friends= [ "ahmed" , "mahmoud" , "sayed" ]
print("mahmoud" not in friends )
print("ahmed" in friends )
print('#'*50)


contries1= ['egypt', 'ksa', 'kuwait']
contriesDiscount=80
contries2=['italy','usa']
contriesDiscount2=50
mycontry='italy'
if mycontry in contries1:
    print(f" hello you're have a discount = {contriesDiscount}")
elif mycontry in contries2:
    print(f" hello you're have a discount = {contriesDiscount2}")
else :
    print("you have no discount")  