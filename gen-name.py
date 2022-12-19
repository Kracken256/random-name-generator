#!/usr/bin/python3
import random
import sys

if "-h" in sys.argv or "--help" in sys.argv:
    print("Use -n [int] to generate n number of names. Example: ./gen-name.py -n 10.")
    exit(0)

with open("first-names.txt", "r") as fnames:
    with open("last-names.txt", "r") as lnames:
        fnames_contents = fnames.readlines()
        lnames_contents = lnames.readlines()
        if len(sys.argv) == 1:
            print(random.choice(fnames_contents).strip().lower().capitalize(
            ) + " " + random.choice(lnames_contents).strip().lower().capitalize())
        elif "-n" in sys.argv:
            n = int(sys.argv[int(sys.argv.index("-n"))+1])
            for _ in range(n):
                print(random.choice(fnames_contents).strip().lower().capitalize(
                ) + " " + random.choice(lnames_contents).strip().lower().capitalize())
