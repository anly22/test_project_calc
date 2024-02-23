exit = 0
def add_(x, y):
    print("\nadd of", x, "+", y, "=", x + y)
def sub_(x, y):
    print("\nsub of", x, "-", y, "=", x - y)
def div_(x, y):
    if y != 0:
        print("\ndiv of", x, "/", y, "=", x / y)
    else :
        print("not defined")   

while exit == 0:
    print(" \n ------- simple calculator ------- \n ")
    fun = int(input("Choose a function \n 1 : add \n 2 : sub \n 4 : div \n 0 : exit \n"))
    if fun == 0:
        break
    x = int(input("Enter 1st number"))
    y = int(input("Enter 2nd number"))
    if fun == 1:
        add_(x, y)
    elif fun == 2:
        sub_(x, y)
    elif fun == 4:
        div_(x, y)
    elif fun == 0:
        break
    else :
        print("Select a valid function")
