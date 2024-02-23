exit = 0
def add_(x, y):
    print("\nadd of", x, "+", y, "=", x + y)
def sub_(x, y):
    print("\nsub of", x, "-", y, "=", x - y)
def mul_(x, y):
    print("\nmull of", x, "*", y, "=", x * y)

while exit == 0:
    print(" \n ------- simple calculator ------- \n ")
    fun = int(input("Choose a function \n 1 : add \n 2 : sub  \n 3 : mul \n 0 : exit \n"))
    if fun == 0:
        break
    x = int(input("Enter 1st number"))
    y = int(input("Enter 2nd number"))
    if fun == 1:
        add_(x, y)
    elif fun == 2:
        sub_(x, y)
    elif fun == 3:
        mul_(x, y)
    elif fun == 0:
        break
    else :
        print("Select a valid function")
