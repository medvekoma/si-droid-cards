import csv
import codecs

def process(input_file_name, output_file_name):
  with open(input_file_name, 'rb') as inputFile:
    with codecs.open(output_file_name, "w", "utf-8-sig") as outputFile:
      reader = csv.reader(inputFile, delimiter=';')
      for row in reader:
        si = row[1]
        if si and si.isdigit():
          name = unicode(row[2]) + ' ' + unicode(row[3], 'utf-8')
          club = row[7]
          line = '%s,%s,%s' % (si, name, club)
          print line
          #outputFile.write('%s,%s,%s' % (si, name, club))

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
  csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
  for row in csv_reader:
    yield [unicode(cell, 'utf-8') for cell in row]

process('si_archivum.csv', 'si-droid-cards.csv')
