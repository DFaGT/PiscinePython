#!/usr/bin/env python3

"""
Simple tester script for ft_tqdm in Loading.py
Compare output with tqdm for visual confirmation.
"""
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

def main():
    count = 333
    print("Testing ft_tqdm:")
    for _ in ft_tqdm(range(count)):
        sleep(0.005)
    print("\nTesting tqdm:")
    for _ in tqdm(range(count)):
        sleep(0.005)
    print()

if __name__ == "__main__":
    main()
