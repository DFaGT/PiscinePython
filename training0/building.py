#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import string

def count_text(text: str) -> tuple[int, int, int, int, int, int]:
    """
    テキスト中の文字を分類してカウントする。

    Returns:
        total: 全文字数
        upper: 大文字の数
        lower: 小文字の数
        punctuation: 句読点の数
        spaces: 空白文字の数
        digits: 数字の数
    """
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    punctuation = sum(1 for c in text if c in string.punctuation)
    total = len(text)
    return total, upper, lower, punctuation, spaces, digits

def main() -> None:
    """
    コマンドライン引数または標準入力から文字列を受け取り、
    各種文字カウントを出力する。
    """
    args = sys.argv[1:]
    # 引数が2つ以上ならエラー表示して終了
    if len(args) > 1:
        print("AssertionError")
        return

    # 引数が1つあればそれをテキストとして使用
    if len(args) == 1:
        text = args[0]
    else:
        # 引数なし→プロンプトを表示して入力を受け付け
        text = input("What is the text to count?\n")

    total, upper, lower, punctuation, spaces, digits = count_text(text)

    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")

if __name__ == "__main__":
    main()
