#!/usr/bin/env python
# coding = utf8
#
# Author: Archer Reilly
# Date: 21/Sep/2014
# File: plotTuta.py
# Des: show Python plot usage
#
# Produced By CSRGXTU
import pylab as pl

#X = [0, 1, 2, 3]
X = [1991, 1992, 1993, 1994]
Y = [0, 1, 2, 3]

pl.plot(X, Y)

pl.xlim(1991, 1994)
pl.xticks([1991, 1992, 1993, 1994])

pl.show()
