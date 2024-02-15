print(input("please input a number:"))

while True:
    try:
        x, y = map(int, input("please input two number:").split(' '))
        print(x + y)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")