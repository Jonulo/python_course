firstNumber = input('type a number: ')

try:
    firstNumber = int(firstNumber)
except:
    firstNumber = False

if firstNumber == False:
    print('Invalid type of input')
    exit()

secondNumber = input('Enter a number: ')

try:
    secondNumber = int(secondNumber)
except:
    secondNumber = False

if secondNumber == False:
    print('Invalid type of input')
    exit()

operator = input('Which kind of operation do you want to do?: ')

if operator == '+':
    print('result: ', firstNumber + secondNumber)
elif operator == '-':
    print('result: ', firstNumber - secondNumber)
elif operator == '*':
    print('result: ', firstNumber * secondNumber)
elif operator == '/':
    print('result: ', firstNumber / secondNumber)
else:
    print('invalid operation')
