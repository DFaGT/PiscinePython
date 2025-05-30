#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ft_filter(function, iterable):
    # 関数が None の場合は真値テスト、それ以外は関数の戻り値でフィルタ
    if function is None:
        return [x for x in iterable if x]
    return [x for x in iterable if function(x)]

# 組み込み filter と同じドキュメント文字列を設定
ft_filter.__doc__ = filter.__doc__
