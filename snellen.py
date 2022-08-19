# -*- coding: utf-8 -*-

import math, random, sys
from string import ascii_uppercase, Template

# 1 meter in inches.
meter = 39.37008

# Now convert to points (using 1 in = 72 pt).
meter *= 72

# 5 arc minutes in radians.
theta = (2 * math.pi / 360 / 60) * 5

# Standard distances (in m).
distances = [60, 36, 30, 24, 18, 12, 6, 5, 4]

# Optotypes to use.
# optotypes = list(ascii_uppercase)
optotypes = set("CDEFHKLNOPRTUVZ") # standard Snellen optotypes

# Number of optotypes for each distance.
num_optotypes = [1, 2, 3, 4, 5, 8, 12, 14, 15]

# TeX code templates.
t1 = Template(r"\deflen{$name}{$length$unit} % $dist m")
t2 = Template(r"\acuity{6/$dist}{20/$feet} & \optotype{\factor\$name}{$string} \\")

def randstring(length=1, previous=None):
    """Return a random string of given length with no repeated letters."""
    if length > len(optotypes):
        raise ValueError("Length of string must be less than total optotypes.")

    if previous:
        pool = optotypes - set(previous)
        if len(pool) < length:
            pool = list(pool) + random.sample(list(optotypes - pool), length - len(pool))
    else:
        pool = optotypes

    pool = list(pool)
    return "".join(random.sample(pool, length))

if len(sys.argv) > 1:
    if sys.argv[1] == "--defs":
        print("\n% Length definitions")
        for i, d in enumerate(distances):
            print(
                t1.substitute(name="Set" + ascii_uppercase[i],
                              length=round(2 * d * math.tan(theta / 2) * meter, 3),
                              unit="pt",
                              dist=d))
    else:
        try:
            num = int(sys.argv[1])
            print("\n% Tables\n")
            for n in range(num):
                print(r"\pagebreak",
                      r"\begin{center}",
                      r"\renewcommand*{\arraystretch}{3.5}",
                      r"\begin{longtable}{rc}",
                      sep="\n")
                previous = None
                for i, d in enumerate(distances):
                    line = randstring(num_optotypes[i], previous)
                    print(
                        t2.substitute(
                            dist=d,
                            feet=int(d / 6 * 20),
                            name="Set" + ascii_uppercase[i],
                            string=line,
                        ))
                    previous = line
                    if i == 4:
                        print(r"& \colorrule{cyan}{0.65cm} \\")
                    elif i == 6:
                        print(r"& \colorrule{red}{0.65cm} \\")
                print(r"\end{longtable}", "\end{center}", "", sep="\n")
        except ValueError:
            sys.exit(print("usage: snellen.py <num>\n       snellen.py --defs"))
else:
    sys.exit(print("usage: snellen.py <num>\n       snellen.py --defs"))
