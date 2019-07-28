from Animal import Animal

class Donkey(Animal):
    #Catクラスの初期化メソッド
    def __init__(self,name):
        super().__init__("ロバ",name)
    #Catクラス独自のひっかくメソッド
    def attack(self):
        print("{0}は後ろ足で強かに蹴り上げた".format(self.name))

    #displayメソッドをオーバーライド
    def display(self):
        #スーパークラスのdisplay呼び出し
        super().display()

    #cryメソッドをオーバーライド    
    def cry(self):
        print("{0}はイアーイアーと鳴き声を上げた".format(self.name))
