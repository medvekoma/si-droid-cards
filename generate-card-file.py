# coding: utf-8

import urllib2
import codecs
import os.path
from datetime import datetime

def get_date_pattern():
  pattern = '{0:%Y-%m-%d}'.format(datetime.now())
  return pattern

def get_archive():
  filename = 'mtfsz-{0}.csv'.format(get_date_pattern())
  if not os.path.isfile(filename):
    response = urllib2.urlopen('http://mtfsz.hu/megjelenites/si_archivum.php')
    with codecs.open(filename, mode='w') as file:
      file.write(response.read())
  return filename

def process():
  input_file_name = get_archive()
  output_file_name = 'si-{0}.csv'.format(get_date_pattern())
  with codecs.open(input_file_name) as input_file:
    with codecs.open(output_file_name, mode='w', encoding='utf-8-sig') as output_file:
      for line in input_file:
        row = line.split(';')
        si = row[1]
        if si.isdigit():
          lastname = row[2]
          firstname = row[3]
          club = row[7]
          outputline = '%s,%s %s,%s\r\n' % (si, lastname, firstname, club)
          outputline = unicode(outputline.decode('latin1'))
          outputline = outputline\
            .replace(u'û', u'ű')\
            .replace(u'õ', u'ő')\
            .replace(u'Õ', u'Ő')\
            .replace(u'Û', u'Ű')
          output_file.write(outputline)

if __name__ == '__main__':
  process()
