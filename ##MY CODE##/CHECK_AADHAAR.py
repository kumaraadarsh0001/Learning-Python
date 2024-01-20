# Number should be 12 chars
# Number should not start with 0 or 1
# It should not contain alphabets
num = input("Please enter a 12 digit Aadhar number: ")
# Check if number length is greater or less then 12
if len(num) > 12 or len(num) < 12:
    print("Aadhar number is not valid (Enter a 12 digit number)")
else:
    # Check if first number is 0 or 1
    if num[0] == '0' or num[0] == '1':
        print("Aadhar number is not valid (Aadhar card number cannot start with 0 or 1)")
    else:
        try:
            num = int(num)
            print("Aadhar number is valid")
        except:
            print('Aadhar number is not valid (Aadhar number should not contain any characters)')