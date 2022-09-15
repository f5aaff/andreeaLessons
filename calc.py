

cont = 1
while cont == 1:
    print("what would you like to calculate?")

    firstval = int(input("first value: "))

    print('what operation would you like to perform?: ')

    operation = input("operation(*/-+): ")

    secondval = int(input('second value: '))


    if operation == '*':
        answer = firstval*secondval
    elif operation == '-':
        answer = firstval-secondval
    elif operation == '/':
        answer= firstval/secondval
    elif operation == '+':
        answer = firstval+secondval
    else:
        print('please enter a valid operator')
    print(answer)

    exit = input("perform another calculation?(y/n): ")
    if exit != 'y'|'Y':
        cont = 0
    

