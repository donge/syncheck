"""Naval Fate.

Usage:
  people.py <num>...
  people.py (-h | --help)
  people.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt
from BeautifulSoup import BeautifulSoup
import requests
import re

svn_re = re.compile(r'\/web\/default\/(\d+)')

class people:
    def __init__(self, name):
      r = requests.get('https://gnats.juniper.net/web/default/dwim?s=responsible+%3D%3D+%22'+name+'%22+%7C+dev-owner+%3D%3D+%22'+name+'%22', auth=('dongdong', 'Kongting2015!'))
      self.soup = BeautifulSoup(r.text)
      self.raw = r.text
      self.name = name

    def alias(self):
      return self.name

    def prs(self):
      commits = self.soup.find(id="table_body")
      return list(set(svn_re.findall(self.raw)))

if __name__ == '__main__':
    args = docopt(__doc__, version='Naval Fate 2.0')
    name = args['<num>'][0]
    if (name):
        print(name)

    '''for test'''
    a = people(name)

    '''PR name'''
    print('People: ' + a.alias())
    print('PRs: ')
    print(a.prs())

    print(args)