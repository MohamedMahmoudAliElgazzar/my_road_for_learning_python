N=[1,2,3,4,5,6,7,8,9]
for num in N:
    if num ==6:
        print(f'the {num} is exists')
        continue
    print(num)
print('#'*50)
for num in N:
    if num ==6:
        print(f'the {num} is exists')
        break
    print(num)
print('#'*50)
for num in N:
    if num ==6:
        print(f'the {num} is exists')
        pass
    print(num)

