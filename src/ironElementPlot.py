#!/usr/bin/env python
# coding = utf8
#
# Author: Archer Reilly
# Date: 22/Sep/2014
# File: ironElementPlot.py
# Des: show Python plot usage
#
# Produced By CSRGXTU
import pylab as pl
import numpy as np


# Build (X, C) (X, S)
#X = [age + 1 for age in range(13)]
X = range(17)
Y = [12,12,12,12,12,12,12,12,12,12,16,16,20,20,375,350,350,350,350]
Y = [9.0,9.0,9.0,12.0,12.0,12.0,13.5,13.5,13.5,13.5,18.0,18.0,18.0,18.0,16.0,15.0,15.0]
# Plot cosine with a blue continuous line of width 1 (pixels)
pl.plot(X, Y, color="blue", linewidth=1.0, linestyle="-")


# Set x limits
pl.xlim(0, 80)

# Set x ticks
#pl.xticks(np.linspace(0, 80, 20, endpoint=True))
pl.xticks(np.arange(1, 82, 2))

# Set y limits
#pl.ylim(1.0, 1.0)

# Set y ticks
#pl.yticks(np.linspace(-1, 1, 5, endpoint=True))

# Save figure using 72 dots per inch
# savefig("exercice_2.png", dpi=72)

# Show result on screen
pl.show()
