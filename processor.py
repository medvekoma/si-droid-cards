import csv
import codecs

def process(input_file_name):
  with open(input_file_name, 'rb') as inputFile:
    reader = csv.reader(inputFile, delimiter=';')
    for row in reader:
      si = row[1]
      if si.isdigit():
        name = row[2] + ' ' + row[3]
        club = row[7]
        line = '%s,%s,%s' % (si, name, club)
        print line

process('si_archivum.csv')
