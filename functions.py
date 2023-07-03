def mitmorn():
    print("This is MIT morning")


mitmorn()


def calculate():
    x = 7
    y = 10
    print(x * y)
    print(x + y)
    print(y - x)
    print(y / x)


def mitmorn():
    print("This is MIT morning")


mitmorn()


def calculate():
    x = 7
    y = 10
    print(x * y)
    print(x + y)
    print(y - x)
    print(y / x)


calculate()


def majina(myfirstname, mylastname, age):
    print("My Name is", myfirstname + " " + mylastname + " I am ", age, "years old")


majina("Ronny", "Kioko", 18)
majina("Adelaide", "Pendo", 15)
majina("Sydney", "Shy", 16)
majina("Joyce", "Maringa", 18)


def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


data = (3, 6, 8, 9, 2, 1, 8)
result = calculate_average(data)
print("The average is", result)
