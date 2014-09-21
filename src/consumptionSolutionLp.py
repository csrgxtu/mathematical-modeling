#!/usr/bin/env python
# coding = utf8
#
# Author: Archer Reilly
# Date: 22/Sep/2014
# File: consumptionSolution.py
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
  return data.tolist()
  

# main
# glue
def main():
  # load data from file
  fruites_prices_file = "../data/Fruite-Vegetable-Price.txt"
  fruites_nutrious_file = "../data/Fruite-Vegetable-Nutrious-ug-10.txt"
  nutrious_boundry_file = "../data/Nutrious-Boundry-mg-10.txt"

  fruites_prices = loadFile2List(fruites_prices_file)
  fruites_nutrious = loadMatrix(fruites_nutrious_file)
  nutrious_boundries = loadMatrix(nutrious_boundry_file)

  """
  for item in nutrious_boundries:
    print item
  """

  prob = LpProblem("fruites-vegetables", LpMinimize)

  # Variables
  X0 = LpVariable("X0")
  X1 = LpVariable("X1")
  X2 = LpVariable("X2")
  X3 = LpVariable("X3")
  X4 = LpVariable("X4")
  X5 = LpVariable("X5")
  X6 = LpVariable("X6")
  X7 = LpVariable("X7")
  X8 = LpVariable("X8")
  X9 = LpVariable("X9")
  X10 = LpVariable("X10")
  X11 = LpVariable("X11")
  X12 = LpVariable("X12")
  X13 = LpVariable("X13")
  X14 = LpVariable("X14")
  X15 = LpVariable("X15")

  # Objective
  # get prices
  prices = []
  for item in fruites_prices:
    prices.append(float(item.split(",")[1].rstrip("\n")))
  
  prob += X0 * prices[0] + X1 * prices[1] + X2 * prices[2] + X3 * prices[3] + X4 * prices[4] + X5 * prices[5] + X6 * prices[6] + X7 * prices[7] + X8 * prices[8] + X9 * prices[9] + X10 * prices[10] + X11 * prices[11] + X12 * prices[12] + X13 * prices[13] + X14 * prices[14] + X15 * prices[15]

  # Constraints
  for i in range(len(nutrious_boundries)):
    boundries = nutrious_boundries[i]
    nutrious = [item / 1000 for item in fruites_nutrious[i]]
    print nutrious
    print boundries
    # XI is KG unit
    #prob += X0 * 10 * nutrious[0] + X1 * 10 * nutrious[1] + X2 * 10 * nutrious[2] + X3 * 10 * nutrious[3] + X4 * 10 * nutrious[4] + X5 * 10 * nutrious[5] + X6 * 10 * nutrious[6] + X7 * 10 * nutrious[7] + X8 * 10 * nutrious[8] + X9 * 10 * nutrious[9] + X10 * 10 * nutrious[10] + X11 * 10 * nutrious[11] + X12 * 10 * nutrious[12] + X13 * 10 * nutrious[13] + X14 * 10 * nutrious[14] + X15 * 10 * nutrious[15] <= boundries[0] * 365
    prob += X0 * 10 * nutrious[0] + X1 * 10 * nutrious[1] + X2 * 10 * nutrious[2] + X3 * 10 * nutrious[3] + X4 * 10 * nutrious[4] + X5 * 10 * nutrious[5] + X6 * 10 * nutrious[6] + X7 * 10 * nutrious[7] + X8 * 10 * nutrious[8] + X9 * 10 * nutrious[9] + X10 * 10 * nutrious[10] + X11 * 10 * nutrious[11] + X12 * 10 * nutrious[12] + X13 * 10 * nutrious[13] + X14 * 10 * nutrious[14] + X15 * 10 * nutrious[15] >= boundries[1] * 365

  prob += X0 >= 0
  prob += X1 >= 0
  prob += X2 >= 0
  prob += X3 >= 0
  prob += X4 >= 0
  prob += X5 >= 0
  prob += X6 >= 0
  prob += X7 >= 0
  prob += X8 >= 0
  prob += X9 >= 0
  prob += X10 >= 0
  prob += X11 >= 0
  prob += X12 >= 0
  prob += X13 >= 0
  prob += X14 >= 0
  prob += X15 >= 0

  GLPK().solve(prob)

  # Solution
  for v in prob.variables():
    print v.name, "=", v.varValue

  print "objective=", value(prob.objective)



if __name__ == "__main__":
  main()
