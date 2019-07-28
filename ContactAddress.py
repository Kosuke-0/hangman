#クラス定義
class ContactAddress :
    #メンバ変数定義
    __address = None
    __email = None
    #初期化メソッド
    def __init__(self,address,email) :
        self.__address = address
        self.__email = email

    #addressのsettar
    def set_address(self,address):
        self.__address = address

    #emailのsetter
    def set_email(self,email):
        self.__email = email

    #addressのgetter
    def get_address(self):
        return self.__address

    #emailのgetter
    def get_email(self):
        return self.__email

    #ContactAddressクラスのdisplayメソッド
    def display(self):
        print('address : {0}'.format(self.__address))
        print('email : {0}'.format(self.__email))

    

