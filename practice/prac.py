# variables

print("Enter two values: ")
a = int(input())
b = int(input())

print("Choose operation \n1)add \n2)minus \n3)multiply \n4)divide")
option = int(input())

if option == 1:
    print(a+b)

elif option == 2:
    print(a-b)

elif option == 3:
    print(a*b)

elif option == 4:
    print(a // b)
