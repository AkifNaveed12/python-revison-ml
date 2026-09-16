# Try-except-finally
# risky code goes in try; expected errors are handled in except
try:
    number = int(input("Enter a no: "))
    result = 10/number
    print(result)
except ValueError:
    print("please enter a valid no")
except ZeroDivisionError:
    print("cannot divide by zero")

#else and finally
# else → runs if no exception occurred
# finally → runs regardless
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Invalid")

else:
    print("Success:", result)

finally:
    print("Execution finished")

# raise
def calculate_accuracy(correct, total):
    if total <= 0:
        raise ValueError("Total must be greater than zero")

    return correct / total