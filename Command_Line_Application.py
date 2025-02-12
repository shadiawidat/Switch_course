def Palindrome_check(str1):
    output = True
    for i in range(len(str1)):
        if str1[i] != str1[len(str1)-i-1]:
            output=False
    return output
def Lower(str1):
    output = str1.islower()
    return output
def Digit(str1):
    return str1.isdigit()
def Long(str1):
    if len(str1)>15:
        return True
    return False
def Empty(str1):
    if str1=="":
        return True
    return False

print("the available options are:")
print("1 - Palindrome: Check if the input is palindrome")
print("2 - Lower: Check if all the characters in the input are lowercase")
print("3 - Digit: Check if all the characters in the input are digits")
print("4 - Long: Check if all the input length is longer than 15")
print("5 - Empty: Check if the input is empty")
print("6 - Exit: Exit successfully from the application")

operations = [Palindrome_check,Lower,Digit,Long,Empty]
while True:
    while True:
        try:
            operation = int(input("Please enter the number of the operation you choose: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    if operation == 6:
        print("Enter an input: ")
        print("Exit successfully")
        break
    str1 = input("Enter an input: ")

    print("The answer is: ",operations[operation-1](str1))

