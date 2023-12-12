def hello():
    print("Hello World")


hello()


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        print("Error: Only numbers are allowed")
        return
    return num1 + num2


total = sum(10, 20)
print(total)
