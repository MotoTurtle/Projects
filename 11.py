Age = input()
try:
    if int(Age) > 18:
        print("Beer")
except ValueError:
    print("Введите число, а не символ")