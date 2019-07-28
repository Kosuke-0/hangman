from Cat import Cat
from Dog import Dog

def main():
    #Catクラスのインスタンス化
    tama = Cat("タマ",True)
    #Animalクラスで定義したdisplayメソッド呼び出し
    tama.display()
    #スーパークラスで定義した変数とサブクラスで定義した変数へのアクセス
    print("{0}は鈴をつけているか : {1}".format(tama.name,tama.bell))
    #Catクラスで定義したClawメソッド呼び出し
    tama.claw()
    #2匹目のCatインスタンスの生成
    mike = Cat("ミケ",False)
    mike.display()
    print("{0}は鈴をつけているか : {1}".format(mike.name,mike.bell))
    mike.claw()
    #仕切り線
    print("-"*20)
    #Dogクラスのインスタンス化
    pochi = Dog("ポチ","ヒロシ")
    #Animalクラスで定義したdisplayメソッド呼び出し
    pochi.display()
    #スーパークラスで定義した変数とサブクラスで定義した変数へのアクセス
    print("{0}の飼い主は{1}さんです。".format(pochi.name,pochi.owner))
    #Dogクラスで定義したbiteメソッド呼び出し
    pochi.bite()
    #2匹目のDogインスタンスの生成
    shiro = Dog("シロ","タカハシ")
    shiro.display()
    print("{0}の飼い主は{1}さんです。".format(shiro.name,shiro.owner))
    shiro.bite()

if __name__ == "__main__":
    main()    

