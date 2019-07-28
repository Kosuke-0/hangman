#親クラスAnimal
class Animal :
    
    #初期化メソッド
    def __init__ (self,type,name) :
        self.type = type
        self.name = name
    #鳴き声メソッド
    def cry(self) :
        print("動物の鳴き声を画面に表示します。")
    #名前と分類を表示するメソッド
    def display(self):
        print("{0}は{1}です。".format(self.name,self.type))

        


