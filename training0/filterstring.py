#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    # 引数個数チェック
    assert len(sys.argv) == 3, "the arguments are bad"

    S = sys.argv[1]
    # N を整数に変換できるか確認
    try:
        N = int(sys.argv[2])
    except ValueError:
        assert False, "the arguments are bad"

    # ラムダ式で長さチェック関数を定義
    longer_than = lambda word: len(word) > N

    # リスト内包表記でフィルタリング
    result = [w for w in S.split(" ") if longer_than(w)]

    # 結果を出力
    print(result)

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
