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
  return data.tolist()
  

# main
# glue
def main():
  # load data from file
  fruite_quatity_file = "../data/Fruite-Quatities-2004.txt"
  age_quatity_file = "../data/Age-Quatities-2004.txt"
  fruite_nutrious_file = "../data/Fruite-Nutrious-2004.txt"
  nutrious_age_file = "../data/Nutrious-Age-2004.txt"

  fruite_quatities = loadFile2List(fruite_quatity_file)
  age_quatities = loadFile2List(age_quatity_file)
  fruite_nutrious = loadMatrix(fruite_nutrious_file)
  nutrious_ages = loadMatrix(nutrious_age_file)

  """
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
  """

  prob = LpProblem("fruites", LpMinimize)

  # Variables
  X0 = LpVariable("X0", 0, 1, cat="Integer")
  X1 = LpVariable("X1", 0, 1, cat="Integer")
  X2 = LpVariable("X2", 0, 1, cat="Integer")
  X3 = LpVariable("X3", 0, 1, cat="Integer")
  X4 = LpVariable("X4", 0, 1, cat="Integer")
  X5 = LpVariable("X5", 0, 1, cat="Integer")
  X6 = LpVariable("X6", 0, 1, cat="Integer")
  X7 = LpVariable("X7", 0, 1, cat="Integer")
  X8 = LpVariable("X8", 0, 1, cat="Integer")
  X9 = LpVariable("X9", 0, 1, cat="Integer")
  X10 = LpVariable("X10", 0, 1, cat="Integer")
  X11 = LpVariable("X11", 0, 1, cat="Integer")
  X12 = LpVariable("X12", 0, 1, cat="Integer")

  # Objective
  prob += X0 + X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 + X9 + X10 + X11 + X11 + X12

  # Constraints
  # get fruite quatities
  quatities = []
  for item in fruite_quatities:
    tmps = item.split(",")
    quatities.append(int((tmps[1]).rstrip("\n")))

  prob += X0 * quatities[0] + X1 * quatities[1] + X2 * quatities[2] + X3 * quatities[3] + X4 * quatities[4] + X5 * quatities[5] + X6 * quatities[6] + X7 * quatities[7] + X8 * quatities[8] + X9 * quatities[9] + X10 * quatities[10] + X11 * quatities[11] + X12 * quatities[12] >= (quatities[0] + quatities[1] + quatities[2] + quatities[3] + quatities[4] + quatities[5] + quatities[6] + quatities[7] + quatities[8] + quatities[9] + quatities[10] + quatities[11] + quatities[12]) * 0.9

  # get age quatities
  ageQuatities = []
  for item in age_quatities:
    tmps = item.split(",")
    ageQuatities.append(int(tmps[1].rstrip("\n")))

  # VA constraints
  """
  vaNutriousQuatities = fruite_nutrious[0]
  vaAgeQuatities = array(nutrious_ages)[:, 0]
  prob += X0 * vaNutriousQuatities[0] * quatities[0] + X1 * vaNutriousQuatities[1] * quatities[1] + X2 * vaNutriousQuatities[2] * quatities[2] + X3 * vaNutriousQuatities[3] * quatities[3] + X4 * vaNutriousQuatities[4] * quatities[4] + X5 * vaNutriousQuatities[5] * quatities[5] + X6 * vaNutriousQuatities[6] * quatities[6] + X7 * vaNutriousQuatities[7] * quatities[7] + X8 * vaNutriousQuatities[8] * quatities[8] + X9 * vaNutriousQuatities[9] * quatities[9] + X10 * vaNutriousQuatities[10] * quatities[10] + X11 * vaNutriousQuatities[11] * quatities[11] + X12 * vaNutriousQuatities[12] * quatities[12] >= ageQuatities[0] * vaAgeQuatities[0] * 365 + ageQuatities[1] * vaAgeQuatities[1] * 365 + ageQuatities[2] * vaAgeQuatities[2] * 365 + ageQuatities[3] * vaAgeQuatities[3] * 365 + ageQuatities[4] * vaAgeQuatities[4] * 365 + ageQuatities[5] * vaAgeQuatities[5] * 365
  """

 
  for i in range(len(fruite_nutrious)):
    vaNutriousQuatities = fruite_nutrious[i]
    vaAgeQuatities = array(nutrious_ages)[:, i]
    prob += X0 * vaNutriousQuatities[0] * quatities[0] + X1 * vaNutriousQuatities[1] * quatities[1] + X2 * vaNutriousQuatities[2] * quatities[2] + X3 * vaNutriousQuatities[3] * quatities[3] + X4 * vaNutriousQuatities[4] * quatities[4] + X5 * vaNutriousQuatities[5] * quatities[5] + X6 * vaNutriousQuatities[6] * quatities[6] + X7 * vaNutriousQuatities[7] * quatities[7] + X8 * vaNutriousQuatities[8] * quatities[8] + X9 * vaNutriousQuatities[9] * quatities[9] + X10 * vaNutriousQuatities[10] * quatities[10] + X11 * vaNutriousQuatities[11] * quatities[11] + X12 * vaNutriousQuatities[12] * quatities[12] >= ageQuatities[0] * vaAgeQuatities[0] * 365 + ageQuatities[1] * vaAgeQuatities[1] * 365 + ageQuatities[2] * vaAgeQuatities[2] * 365 + ageQuatities[3] * vaAgeQuatities[3] * 365 + ageQuatities[4] * vaAgeQuatities[4] * 365 + ageQuatities[5] * vaAgeQuatities[5] * 365

  #prob += X0 + X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 + X9 + X10 + X11 + X11 + X12 <= len(fruite_quatities)

  GLPK().solve(prob)


if __name__ == "__main__":
  main()
