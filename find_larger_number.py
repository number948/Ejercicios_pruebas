# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def find_number(name):
    myArray = [5, 20, 89, 30, 60]
    mayor = myArray[0]

    for element in range(1, len(myArray)):
        if myArray[element] > mayor:
            mayor = myArray[element]
    print(mayor)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_number('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
