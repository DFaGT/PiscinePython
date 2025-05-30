def all_thing_is_obj(obj: any) -> int:
    """
    与えられたオブジェクトの型に応じたメッセージを出力し、最終的に42を返す関数
    """
    if type(obj) is list:
        print("List : ", type(obj))
    elif type(obj) is tuple:
        print("Tuple : ", type(obj))
    elif type(obj) is set:
        print("Set : ", type(obj))
    elif type(obj) is dict:
        print("Dict : ", type(obj))
    elif type(obj) is str:
        # 文字列の場合は、文字列の内容を出力メッセージに組み込む
        print(f"{obj} is in the kitchen : {type(obj)}")
    else:
        print("Type not found")
    return 42
