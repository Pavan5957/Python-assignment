try:
    num = float(input("enter a number: "))
    if num == 0:
        raise ZeroDivisionError("cannot divide by zero please enter a non zero number ")

    division_result = 10/num
    print(f"the result is : {division_result}")


except ZeroDivisionError as ze:
    print(f"error: {ze}")

