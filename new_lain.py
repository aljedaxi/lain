#!/usr/bin/env python3
# LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!

import random
from subprocess import call


def cast_line(num):
    if num == 0:
        return ("0", "1")
    elif 0 < num < 4:
        return ("1", "0")
    elif 3 < num < 9:
        return ("1", "1")
    elif 8 < num < 16:
        return ("0", "0")
    else:
        raise Exception("Lain's fucking with you.")

def gen_grams(question):
    caster = (cast_line(random.randrange(15)) for line in range(6))

    # hexagram and changed hexagram
    gram = []
    cgram = []

    for line, cline in caster:
        gram.append(line)
        cgram.append(cline)

    gram = gram[::-1]
    cgram = cgram[::-1]

    return gram, cgram

def ichingfortune(number):
    ichingsite = ("https://ichingfortune.com/hexagrams/%s.php",)
    return ichingsite % number

def the_iching(number):
    ichingsite = "http://the-iching.com/hexagram_%s"
    s_number = str(number)
    # this site doesn't like trailing zeros
    if s_number[0] == "0":
        return ichingsite % s_number[1]
    else:
        return ichingsite % s_number

def main(
    question,
    yin="- -",
    yang="---",
    lain_csv="lain.csv",
    bagua_csv="bagua.2.csv",
    browsing=True,
    websitefun=the_iching,
    browser="qutebrowser",
):
    def print_gram(gram, cgram):
        def t(line):
            return {"0": yin, "1": yang}[line]

        return (
            f"{t(gram[0])}     {t(cgram[0])}\n"
            f"{t(gram[1])}     {t(cgram[1])}\n"
            f"{t(gram[2])} --\ {t(cgram[2])}\n"
            f"{t(gram[3])} --/ {t(cgram[3])}\n"
            f"{t(gram[4])}     {t(cgram[4])}\n"
            f"{t(gram[5])}     {t(cgram[5])}"
        )

    def search(gram):
        sgram = "".join(gram)
        searchfile = (line for line in open(lain_csv))

        for line in searchfile:
            if sgram in line:
                return str.split(line)[0]

    def browse_to(number):
        call((browser, websitefun(number)))

    gram, cgram = gen_grams(question)
    formatted_gram = print_gram(gram, cgram)

    if browsing:
        gram_number = search(gram)
        cgram_number = search(cgram)

        for number in (gram_number, cgram_number):
            browse_to(number)

    return formatted_gram

if __name__ == "__main__":
    YIN = "--  --"
    YANG = "------"
    BAGUA_CSV = "bagua.2.csv"
    LAIN_CSV = "lain.csv"
    DESCRIPTION = f"""
        Commune with the dark god of the internet, Lain!
        YIN  = {YIN}
        YANG = {YANG}
    """
    import argparse

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    ARGS = parser.parse_args()
    # TODO: ask if you browsing

    print("I love you lain!\n")  # LET'S ALL LOVE LAIN
    question = input(
        "what would you like to ask lain? "
    )  # i don't know if you need this, my darling lain.
    print("")

    print(main(question, yin=YIN, yang=YANG))
    print("LET'S ALL LOVE LAIN!")
