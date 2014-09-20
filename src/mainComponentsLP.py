#!/usr/bin/env python
# coding = utf8
#
# Author: Archer Reilly
# Date: 21/Sep/2014
# File: mainComponentsLP.py
# Des: this file is used to find the solutions of the main
# components in many things by using Linear Programing method
# and pulp package of the python.
#
# Produced By CSRGXTU
from pulp import *
from numpy import *

# loadFile2List
# load plain text file into list
#
# @param file
# @return list
def loadFile2List(filePath):
  data = []
  with open(filePath, "r") as myFile:
    data = myFile.readlines()

  return data

# loadMatrix
# load matrix from file
#
# @param filePath
# @return 2d list
def loadMatrix(filePath):
  data = loadtxt(filePath, delimiter=",", dtype="float", unpack=True)
  return data
  

# main
# glue
def main():
  # load data from file
  fruite_quatity_file = "../data/Fruite-Quatities-2004.txt"
  age_quatity_file = "../data/Age-Quatities-2004.txt"
  fruite_nutrious_file = "../data/Fruite-Nutrious-2004.txt"
  age_nutrious_file = "../data/Age-Nutrious-2004.txt"

  fruite_quatities = loadFile2List(fruite_quatity_file)
  age_quatities = loadFile2List(age_quatity_file)
  fruite_nutrious = loadMatrix(fruite_nutrious_file)
  #age_nutrious_file = loadMatrix(age_nutrious_file)

  for item in fruite_quatities:
    tmps = item.split(",")
    print tmps[0], tmps[1]

  for item in age_quatities:
    tmps = item.split(",")
    print tmps[0], tmps[1]

  for item in fruite_nutrious:
    print item
    #tmps = item.split(",")
    #print tmps[0], " ", tmps[1], " ", tmps[2]
  


if __name__ == "__main__":
  main()
"""
prob = LpProblem("fruites", LpMinimize)

# Variables
# cat is for continious or discrete
X1 = LpVariable("X1", 0, 1, cat="Integer")

# Objective

# Constraints

# Invoke GNU GLPK package solve
GLPK().solve(prob)

# Solution
"""
