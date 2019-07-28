from Animal import Animal

class Chicken(Animal) :
    #Catクラスの初期化メソッド
    def __init__(self,name):
        super().__init__("ニワトリ",name)
    #Catクラス独自のひっかくメソッド
    def attack(self):
        print("{0}は硬いくちばしで繰り返しつついた".format(self.name))

    #displayメソッドをオーバーライド
    def display(self):
        #スーパークラスのdisplay呼び出し
        super().display()

    #cryメソッドをオーバーライド    
    def cry(self):
        print("{0}はコケコッコーとけたたましく鳴いた".format(self.name))
