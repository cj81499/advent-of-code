from __future__ import annotations

import re

TEXT_IN_BRACKET_REGEX = re.compile(r"\[(\w+)\]")
TEXT_REGEX = re.compile(r"(\w+)")


def parta(txt: str):
    return sum(supports_tls(line) for line in txt.splitlines())


def partb(txt: str):
    return sum(supports_ssl(line) for line in txt.splitlines())


def supports_tls(ip: str):
    return not any(has_aba_or_abba(s) for s in hypernet_sequences(ip)) and any(
        has_aba_or_abba(s) for s in supernet_sequences(ip)
    )


def is_aba_or_abba(s: str):
    return s[0] != s[1] and is_palendrome(s)


def has_aba_or_abba(s: str):
    return any(is_aba_or_abba(sub) for sub in subs_of_length(s, 4))


def supports_ssl(ip: str):
    sn_seqs = supernet_sequences(ip)
    for hn_seq in hypernet_sequences(ip):
        for aba in subs_of_length(hn_seq, 3):
            if is_aba_or_abba(aba):
                bab = f"{aba[1]}{aba[:2]}"
                if any(bab in sn_seq for sn_seq in sn_seqs):
                    return True
    return False


def hypernet_sequences(ip: str):
    """text inside of brackets"""
    return set(TEXT_IN_BRACKET_REGEX.findall(ip))


def supernet_sequences(ip: str):
    """text outside of brackets"""
    return set(TEXT_REGEX.findall(ip)) - hypernet_sequences(ip)


def subs_of_length(s: str, length: int):
    assert length > 0
    yield from (s[i : i + length] for i in range(len(s) - (length - 1)))


def is_palendrome(s: str):
    length = len(s)
    return all(s[i] == s[length - 1 - i] for i in range(length // 2))


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
