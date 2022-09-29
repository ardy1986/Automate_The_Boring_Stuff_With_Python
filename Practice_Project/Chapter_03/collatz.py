def collatz(number):
    if int(number) % 2 == 0:
        print(int(number) // 2)
        return int(number) // 2
    elif int(number) % 2 == 1:
        print(3 * int(number) + 1)
        return 3 * int(number) + 1


# print("Enter number :")
num = input("Enter number : \n")

try:
    while int(num) != 1:
        num = collatz(num)
except ValueError:
    print("Please enter a valid INTEGER.")
