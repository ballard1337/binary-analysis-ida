#!/usr/bin/env python3
from functools import lru_cache

parts = [
    ("aadddbabaabdahaahaadadaadaabaa", 84),
    ("ddddddgudggdaddddaddddgdddggdd", 89),
    ("fffeecfcfeffffoffoffcfcffcffefc", 91),
]

def to_bits(n: int) -> str:
    if n <= 0:
        return ""
    return bin(n)[2:][::-1]

def build_expected() -> str:
    out = []
    for text, base in parts:
        key = base + 12
        for ch in text:
            out.append(to_bits(ord(ch) ^ key))
    return "".join(out)

def decode_input(target: str) -> str:
    enc = {i: to_bits(i) for i in range(1, 79)}

    @lru_cache(None)
    def go(pos: int, left: int):
        if pos == len(target):
            return "" if left == 0 else None
        if left == 0:
            return None

        for n in range(1, 79):
            bits = enc[n]
            if target.startswith(bits, pos):
                tail = go(pos + len(bits), left - 1)
                if tail is not None:
                    return chr(n + 48) + tail
        return None

    res = go(0, 26)
    if res is None:
        raise RuntimeError("kluchanetu")
    return res

if __name__ == "__main__":
    expected = build_expected()
    key = decode_input(expected)
    print(key)
