import urllib2
import collections

def process():
  response = urllib2.urlopen('http://mtfsz.hu/megjelenites/si_archivum.php')
  dictionary = {}
  for line in response:
    row = line.split(';')
    si = row[1]
    if si.isdigit():
      name = row[2] + ' ' + row[3]
      club = row[7]
      dictionary[int(si)] = (name, club)
  sdict = sorted(dictionary.items())
  for key, value in sdict:
    print '%s,%s,%s' % (key, value[0], value[1])

if __name__ == '__main__':
  process()
