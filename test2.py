import sys

def Ins(data1,data2):
    try:
        if int(data1) and int(data2):
            num1 = int(data1)
            num2 = int(data2)
            sum = num1 + num2
            print('sys.argv1 + sys.srgv2 = {0}'.format(sum))
        else:
            pass
    except ValueError:
        print("invalid literal for int() with base {0}: '{1}'".format(data1,data2))

Ins(sys.argv[1],sys.argv[2])