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


def main():
    with open(sys.argv[1], "r") as fin:
        data = fin.readlines()
    data = [line.lstrip().rstrip() for line in data]
    data = [line for line in data if line]
    x = []
    for line in data:
        try:
            x.append(float(line))
        except:
            pass
    x = np.array(x)
    print x.shape
    x = x.reshape(x.shape[0] / 9, 9)
    df = pd.DataFrame(x)
    df.to_csv("table_2_9.csv", index=False, header=False)
    return

if __name__ == '__main__':
    main()
