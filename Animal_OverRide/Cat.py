from Animal import Animal
class Cat(Animal) :
    #Catクラスの初期化メソッド
    def __init__ (self,name,bell) :
        super().__init__("猫",name)
        self.bell = bell
    #Catクラス独自のひっかくメソッド
    def claw(self):
        print("{0}が鋭い爪でひっかいた".format(self.name))

    #displayメソッドをオーバーライド
    def display(self):
        #スーパークラスのdisplay呼び出し
        super().display()
        #Catの鈴がついているかいないかを検証
        if self.bell == True:
            #猫が鈴をつけていれば
            print("{0}は鈴をつけている".format(self.name))
        else:
            #猫が鈴をつけていなければ
            print("{0}は鈴をつけていない".format(self.name))

    def cry(self):
        print("{0}はニャーと鳴いた".format(self.name))



