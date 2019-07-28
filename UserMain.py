from User import User
def main() :
    #1人目のUserのインスタンス化
    usr = User("takahashi",20,"male","神奈川県","設定なし")

    #2人目Userのインスタンス化 キーワード引数での呼び出し
    usr2 = User(gender="male", name="inagawa", age=26,address="愛知県",email="sample@example.com")

    # #3人目Userのインスタンス化
    usr3 = User("yamazaki", 29, "female","東京都","example@something.com")

    #3人分の情報をdisplayメソッドで表示
    usr.display()
    usr2.display()
    usr3.display()

#-- Main function Define--#
if __name__ == '__main__':
    main()