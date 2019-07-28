from ContactAddress import ContactAddress
class User :
    #メンバ変数定義
    __name = None
    __age = None
    __gender = None
    #ContactAddressを格納するためのメンバ変数
    __contact_address = None


    #初期化メソッド定義
    def __init__(self, name,age,gender,address,email):
        self.__name = name
        self.__age = age
        self.__gender = gender 
        #初期化メソッド内でContactAddressのインスタンス化
        self.__contact_address = ContactAddress(address,email)

    #displayメソッド定義
    def display(self):
        print("name : {name}".format(name=self.__name))
        print("age : {age}".format(age = self.__age))
        print("gender : {gender}".format(gender = self.__gender))
        #メンバ変数__contact_addressに代入されているインスタンスのdisplayメソッドを利用する
        self.__contact_address.display()
        print("-"*20)
    #setnameメソッド定義
    def setname(self,name) :
        self.__name = name
    #setageメソッド定義
    def setage(self,age) :
        self.__age = age
    #setgenderメソッド定義
    def setgender(self,gender) :
        self.__gender = gender
    #getnameメソッド定義    
    def getname(self) :
        return self.__name
    #getageメソッド定義
    def getage(self) :
        return self.__age
    #getgenderメソッド定義
    def getgender(self) :
        return self.__gender
