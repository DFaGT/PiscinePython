#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ft_filter import ft_filter


def run_test(function, iterable):
    expected = list(filter(function, iterable))
    result = ft_filter(function, iterable)
    assert result == expected, (
        f"FAIL: filter({function}, {iterable}) -> {expected}, but ft_filter -> {result}"
    )


def main():
    # 偶数フィルタ
    run_test(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
    # 真値テスト
    run_test(None, ["a", "", None, "b", 0, 5])
    # 文字列の長さフィルタ
    run_test(lambda s: len(s) > 3, ["dog", "elephant", "cat", "giraffe"])
    # 空のイテラブル
    run_test(lambda x: True, [])
    run_test(None, [])
    # タプル
    run_test(lambda x: x > 0, (-2, -1, 0, 1, 2))
    # 文字列（イテレータ）
    run_test(lambda c: c in "aeiou", "abcdefg")

    print("All tests passed!")


if __name__ == "__main__":
    main()
