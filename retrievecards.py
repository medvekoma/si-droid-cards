import urllib2
import collections

def process():
  response = urllib2.urlopen('http://mtfsz.hu/megjelenites/si_archivum.php')
  dictionary = {}
  for line in response:
    row = line.split(';')
    si = row[1]
    if si.isdigit():
      name = '%s %s' % (row[2], row[3])
      club = row[7]
      dictionary[name] = (si, club)
  sdict = sorted(dictionary.items())
  for key, value in sdict:
    print '%s,%s,%s' % (value[0], key, value[1])

if __name__ == '__main__':
  process()
