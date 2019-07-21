import sys

def Cal(data1,data2,data3):
    try:
        num1 = int(data1)
        num2 = int(data3)
        x = data2
        if x == '+':
            ans1 = num1 + num2
            print('{0} + {1} = {2}'.format(num1,num2,ans1))
        elif x == '-':
            ans2= num1 - num2
            print('{0} - {1} = {2}'.format(num1,num2,ans2))
        elif x == '*':
            ans3 = num1 * num2
            print('{0} * {1} = {2}'.format(num1,num2,ans3))
        elif x == '/':
            ans4 = num1 / num2
            print('{0} / {1} = {2}'.format(num1,num2,ans4))
        else:
            print('演算子を入力してください')

    except ValueError:
        print('数値を入力してください')

Cal(sys.argv[1],sys.argv[2],sys.argv[3])
