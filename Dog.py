from Animal import Animal
#Dogクラス定義
class Dog(Animal):

    owner = None
    
    #Dogクラスの初期化メソッド
    def __init__ (self,name,owner):
        #スーパークラスの初期化メソッドを利用する
        super().__init__("犬",name)
        #飼い主属性を初期化
        self.owner = owner

    #Dogクラス独自の噛みつくメソッド
    def bite(self):
        print("{0}は激しくかみついた".format(self.name))
