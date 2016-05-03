import urllib2

def process():
  response = urllib2.urlopen('http://mtfsz.hu/megjelenites/si_archivum.php')
  for line in response:
    row = line.split(';')
    si = row[1]
    if si.isdigit():
      name = row[2] + ' ' + row[3]
      club = row[7]
      line = '%s,%s,%s' % (si, name, club)
      print line

if __name__ == '__main__':
  process()
