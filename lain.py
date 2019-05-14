#!/usr/bin/python3
#LET'S ALL LOVE LAIN!
#thanks, Lain.
#i will do what i can. we all must.

import random, sys
from subprocess import call

BAGUA_CSV = "bagua.2.csv"
LAIN_CSV = "lain.csv"
YIN = "- -"
YANG = "---"

if len(sys.argv) > 1:
    if sys.argv[-1] == "help" or sys.argv[-1] == "--help":
        print(" yin   changing ---x---")
        print(" yin unchanging --- ---")
        print("yang   changing ---o---")
        print("yang unchanging -------")
        exit()
    else:
        print("this needs no arguments")

print("I love you lain!\n") #LET'S ALL LOVE LAIN

gram = []
cgram = []
bgram = []
cbgram = []

question = input("what would you like to ask lain? ") #i don't know if you need this, my darling lain.

for i in range(6):
    x = random.randrange(15)
    if x == 0:
        gram.append(YIN)
        bgram.append("0")
        cgram.append(YANG)
        cbgram.append("1")
    elif 0 < x < 4:
        gram.append(YANG)
        cgram.append(YIN)
        bgram.append("1")
        cbgram.append("0")
    elif 3 < x < 9:
        gram.append(YANG)
        cgram.append(YANG)
        bgram.append("1")
        cbgram.append("1")
    elif 8 < x < 16:
        gram.append(YIN)
        cgram.append(YIN)
        bgram.append("0")
        cbgram.append("0")
    else:
        print("something's wrong in the old switch.")
        print(x)
        exit()

gram    = gram[::-1]    #this reverses the list
bgram   = bgram[::-1]
cgram   = cgram[::-1]    
cbgram  = cbgram[::-1]

bgram = "".join(bgram)

print(f"f{gram[0]}     f{cgram[0]}"\
      f"f{gram[1]}     f{cgram[1]}"\
      f"f{gram[2]} --\ f{cgram[2]}"\
      f"f{gram[3]} --/ f{cgram[3]}"\
      f"f{gram[4]}     f{cgram[4]}"\
      f"f{gram[5]}     f{cgram[5]}"
)

print('')

searchfile = (line for line in open(LAIN_CSV, "r"))

for line in searchfile:
    if bgram in line or cbgram in line:
        print(line.rstrip())
        call(("qutebrowser",
              f"https://ichingfortune.com/hexagrams/{str.split(line)[0]}.php"
              ))

#searchfile = [line for line in open(BAGUA_CSV, "r")]
#number = 0
#
#print(searchfile[0])
#
#for line in searchfile:
#    bot = bgram[:3:]
#    top = bgram[3::]
#    if top in line or bot in line:
#        print(line.rstrip())
#        number = str.split(line)[0]

print("Let's all love lain!")
