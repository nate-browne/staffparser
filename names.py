#!/usr/local/bin/python3

import csv
from sys import argv, exit

if __name__ == '__main__':

  try:
    filename = argv[1]
  except IndexError:
    print("Please provide a filename.")
    exit(1)

  if '.tsv' not in filename:
    filename += '.tsv'

  with open(filename, 'r') as infile:
    reader = csv.reader(infile, delimiter='\t')

    for ind in range(2):
      next(reader)

    names = []
    for row in reader:
      names.append(row[3])

  with open("tutors.out", 'w') as outfile:
    for name in names:
      outfile.write("{}\n".format(name))

