#!/usr/bin/env python3
import sys

def main():
    # 引数チェック: 文字列1つのみ
    assert len(sys.argv) == 2, "the arguments are bad"
    text = sys.argv[1]

    # Morseコード辞書
    MORSE = {
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
        "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
        "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
        "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
        "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
        "Y": "-.--",  "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",
        " ": "/"  # スペースはスラッシュで表現
    }

    codes = []
    for ch in text:
        key = ch.upper()
        if key not in MORSE:
            raise AssertionError("the arguments are bad")
        codes.append(MORSE[key])

    # 各コードを半角スペース区切りで結合して出力
    print(" ".join(codes))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        # Traceback なしでエラーメッセージだけ出す
        print(f"AssertionError: {e}")
        sys.exit(1)
