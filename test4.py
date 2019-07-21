import sys

emp = {'001':['Yamada','090-xxxx-xxx']}

def Search(data1):
    try:
        if int(data1):
            print('Emplyee Name : {}'.format(emp[data1][0]))
            print('Emplyee Tell : {}'.format(emp[data1][1]))
        else:
            pass
    except ValueError:
        print('数値を入力してください')
    except KeyError:
        print('該当する key はありません')

Search(sys.argv[1])