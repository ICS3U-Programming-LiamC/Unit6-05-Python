#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: June 15, 2021
# This program gets a bunch of numbers from the
# user then finds their average


# greets the user
def Greeting():
    print("Welcome, this program will ask for numbers")
    print("between 0 and 100, it will then calcualte the average")
    print("The program will only stop asking for numbers if you type '-1'")


# calculates the average
def Average(list_nums):
    total = 0
    for each in list_nums:
        total = total + each

    average = total / len(list_nums)
    return average


# main function
def main():
    # gets the initial number and initialises the vars
    user_num = input("What is the number: ")
    nums_list = []
    num_too_big = False
    num_too_small = False
    decimal = False

    # make sure the users num can be an integer
    try:
        user_num = float(user_num)
        # check that its bigger than 0 and less than 100
        # and that its not a decimal
        if (user_num > 100):
            print("Number can not be more than 100")
            num_too_big = True

        elif (user_num < 0 and user_num != -1):
            print("Number can not be less then 0")
            num_too_small = True

        elif (user_num % 1 != 0):
            print("Number can't be a decimal")
            decimal = True

        # as long as the number is not -1 keep asking for the users input
        while (user_num != -1):
            # if all conditions are met add the number to the list
            if ((num_too_small is False) and (num_too_big is False)
                    and (decimal is False)):
                nums_list.append(user_num)

            # same as before
            user_num = input("What is the number: ")
            num_too_big = False
            num_too_small = False
            decimal = False
            try:
                user_num = float(user_num)
                if (user_num > 100):
                    print("Number can not be more than 100")
                    num_too_big = True

                elif (user_num < 0 and user_num != -1):
                    print("Number can not be less then 0")
                    num_too_small = True

                elif (user_num % 1 != 0):
                    print("Number can't be a decimal")
                    decimal = True

            # if error
            except ValueError:
                print("Not valid input")
                break

        # call the function with the list
        # then print the results
        average = Average(nums_list)
        print(nums_list)
        print(average)

    # if error
    except ValueError:
        print("Not valid input")


# start the program
if __name__ == "__main__":
    Greeting()
    main()
