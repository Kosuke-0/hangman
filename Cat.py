from Animal import Animal
class Cat(Animal) :

    bell = None

    #Catクラスの初期化メソッド
    def __init__ (self,name,bell) :
        super().__init__("猫",name)
        self.bell = bell
    #Catクラス独自のひっかくメソッド
    def claw(self):
        print("{0}が鋭い爪でひっかいた".format(self.name))
