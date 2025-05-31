"""
ft_package
~~~~~~~~~~

シンプルな Python パッケージの例です。リスト内で指定アイテムが
何回出現するかを数える関数を提供します。
"""

__version__ = "0.0.1"

def count_in_list(lst, item):
    """
    リスト lst の中で、item が出現する回数を返す

    Parameters:
        lst (list): 要素を数えたいリスト
        item (any): カウント対象の要素

    Returns:
        int: lst 内で item が現れる回数
    """
    return lst.count(item)
