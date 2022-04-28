for _ in range(100):
    print("--------MyCalculator--------")
    num = input('Enter the number:  ')
    opr = input('{x}{%}{-}{+}{=} :  ')
    answer = float(num)
    for __ in range(100):
        while opr == "+":
            numb = input('Enter the number:  ')
            numb = float(numb)
            answer = answer + numb
            opr = input('{x}{%}{-}{+}{=} :  ')
        while opr == "-":
            numb = input('Enter the number:  ')
            numb = float(numb)
            answer = answer - numb
            opr = input('{x}{%}{-}{+}{=} :  ')
        while opr == "*":
            numb = input('Enter the number:  ')
            numb = float(numb)
            answer = answer * numb
            opr = input('{x}{%}{-}{+}{=} :  ')
        while opr == "/":
            numb = input('Enter the number:  ')
            numb = float(numb)
            answer = answer / numb
            opr = input('{x}{%}{-}{+}{=} :  ')

    if opr == "=":
        print("                   =",answer)
        print(" ")
    elif opr != ("=","+","-","*","/",):
        print(" ")
        print(' ....  Wrong Operator  ....')
        print('  ..     Try Again     ..')
        print(" ")
