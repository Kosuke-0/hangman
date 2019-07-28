import Cat,Dog,Chicken,Donkey
#animals_displayメソッド定義
def animals_display(animal) :
    animal.display()
    animal.cry()
    animal.attack()

def main():
    #Catクラスのインスタンス化
    tama = Cat.Cat("タマ",True)
    #Dogクラスのインスタンス化
    pochi = Dog.Dog("ポチ","ヒロシ")
    #Donkeyクラスのインスタンス化
    dondon = Donkey.Donkey("ドンドン")
    #Chickenクラスのインスタンス化
    hiyochan = Chicken.Chicken("ヒヨちゃん")
    #異なるオブジェクトをリストにまとめる
    bremen = [tama,pochi,dondon,hiyochan]
    for animal in bremen:
        animals_display(animal)
    

if __name__ == "__main__":
    main()