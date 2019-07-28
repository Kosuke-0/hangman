from Animal import Animal
#Dogクラス定義
class Dog(Animal) :
    
    #Dogクラスの初期化メソッド
    def __init__ (self,name,owner) :
        #スーパークラスの初期化メソッドを利用する
        super().__init__("犬",name)
        #飼い主属性を初期化
        self.owner = owner

    #Dogクラス独自の噛みつくメソッド
    def attack(self) :
        print("{0}は激しくかみついた".format(self.name))
    #displayメソッドをオーバーライド
    def display(self) :
        #スーパークラスのdisplayメソッドを呼び出す
        super().display()
        print("{0}の飼い主は{1}さんです".format(self.name, self.owner))

    #cryメソッドをオーバーライド    
    def cry(self) :
        print("{0}はワンワン吠えた".format(self.name))
