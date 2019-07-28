#親クラスAnimal
class Animal :
    
    #初期化メソッド
    def __init__ (self,type,name) :
        self.name = name
        self.type = type

    #名前と分類を表示するメソッド
    def display(self):
        print("{0}は{1}です。".format(self.name,self.type))

    def cry(self):
        print("動物の鳴き声を表示します。")