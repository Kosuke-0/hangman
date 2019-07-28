import Cat,Dog

def main() :
    #Catクラスのインスタンス化
    tama = Cat.Cat("タマ",True)
    #Catクラスでオーバーライドしたdisplayメソッド呼び出し
    tama.display()
    tama.cry()
    #2匹目のCatインスタンスの生成
    mike = Cat.Cat("ミケ",False)
    mike.display()
    mike.cry()
    #仕切り線
    print("-"*20)

    #Dogクラスのインスタンス化
    pochi = Dog.Dog("ポチ","ヒロシ")
    #Dogクラスでオーバーライドしたdisplayメソッド呼び出し
    pochi.display()
    pochi.cry()
    #2匹目のDogインスタンスの生成
    shiro = Dog.Dog("シロ","タカシ")
    shiro.display()
    shiro.cry()

if __name__ == "__main__":
    main()    

