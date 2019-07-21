import sys

def Tax(data1,data2):
    try:
        if int(data1) and float(data2):
            num1 = int(data1)
            num2 = float(data2)
            sum = num1 + (num1 * num2)
            print('Price : {}'.format(num1))
            print('Tax : {}'.format(num2))
            print('Total Fee : {}'.format(sum))
        else:
            pass
    except ValueError:
        print('数値を入力してください')

Tax(sys.argv[1],sys.argv[2])
