#ProcessData.py
#Name: Jenna Kramer
#Date: 3/31
#Assignment: Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  # line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]
  

    student_ID = makeID(first, last, idNum)
    majorYear = makeDegree(major,year)

    output = last + "," + first + "," + student_ID + "," + majorYear + "\n"
    outFile.write(output)
    print(output)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  # print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "x"

  id = first[0] + last + idNum[idLen - 3: ]
  # print(id)
  return id 

def makeDegree(major, year):
  # print(first, last, idNum) 
  # need to print data[5] and data[6+]
  abbrMajor = major[:3]
  
  if year == "Senior":
    abbrYear = "SR" 
  elif year == "Junior":
    abbrYear = "JR"
  elif year == "Sophomore":
    abbrYear = "SO"
  else: 
    abbrYear = "FR"

  return (abbrMajor + "-" + abbrYear)

if __name__ == '__main__':
  main()
