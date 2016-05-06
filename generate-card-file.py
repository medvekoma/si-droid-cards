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

def get_card_list():
  input_file_name = get_archive()
  card_list = []
  with codecs.open(input_file_name, encoding='latin1') as input_file:
    for line in input_file:
      row = line.split(';')
      si = row[1]
      if si.isdigit():
        name = row[2] + ' ' + row[3]
        club = row[7]
        val = (name, si, club)
        card_list.append(val)
  return sorted(card_list)

def store_card_list(card_list):
  output_file_name = 'si-{0}.csv'.format(get_date_pattern())
  with codecs.open(output_file_name, mode='w', encoding='utf-8-sig') as output_file:
    for card in card_list:
      outputline = '%s,%s,%s\r\n' % (card[1], card[0], card[2])
      outputline = unicode(outputline) \
        .replace(u'û', u'ű') \
        .replace(u'õ', u'ő') \
        .replace(u'Õ', u'Ő') \
        .replace(u'Û', u'Ű')
      output_file.write(outputline)

def process():
  card_list = get_card_list()
  store_card_list(card_list)

if __name__ == '__main__':
  process()
