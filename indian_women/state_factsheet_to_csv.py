#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@newton>
#
# Distributed under terms of the MIT license.

"""

"""
import sys
import numpy as np
import pandas as pd
import ast

spurious_chars = "≥"


def main():
    with open(sys.argv[1], "r") as fin:
        data = fin.readlines()
    state_name = data[0].replace("Key Indicators for ", "").rstrip()
    data = [line.lstrip().rstrip() for line in data if line]
    data = [line for line in data if line]
    numbers = []
    for n in data:
        for char in spurious_chars:
            n = n.replace(char, "")
        if n in ("na", "*", "nc"):
            numbers.append("na")
        else:
            try:
                x = ast.literal_eval(n)
                if isinstance(x, (float, int)):
                    numbers.append(x)
            except:
                pass
    if len(numbers) == 477:
        x = np.array(numbers).reshape(477 / 9, 9, order='F')
        pd.DataFrame(x).to_csv("%s.csv" % state_name, index=False, header=False)
    else:
        print len(numbers), state_name

if __name__ == '__main__':
    main()
