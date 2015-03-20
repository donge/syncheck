"""Naval Fate.

Usage:
  pr.py <num>...
  pr.py ship <name> move <x> <y> [--speed=<kn>]
  pr.py ship shoot <x> <y>
  pr.py mine (set|remove) <x> <y> [--moored | --drifting]
  pr.py (-h | --help)
  pr.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""
from docopt import docopt
from BeautifulSoup import BeautifulSoup
import requests
import re

svn_re = re.compile(r'Revision:     (\d+)')

class pr:
    def __init__(self, name):
      r = requests.get('https://gnats.juniper.net/web/default/' + name, auth=('dongdong', 'Kongting2015!'))
      self.soup = BeautifulSoup(r.text)

    def name(self):
      return self.soup.title.string;

    def commits(self):
      commits = self.soup.find(id="cm-events-table")
      return svn_re.findall(commits.tbody.text)

if __name__ == '__main__':
    args = docopt(__doc__, version='Naval Fate 2.0')
    num = args['<num>'][0]
    if (num):
        print(num)

    '''for test'''
    a = pr('1067985')

    '''PR name'''
    print('PR: ' + a.name())
    print('Commits: ')
    print(a.commits())
    '''PR scope
    start = 1
    scope = soup.find(id="div_planned-release_" + str(start))

    while scope:
      print(scope.span.text)
      start = start + 1
      scope = soup.find(id="div_planned-release_" + str(start))
    '''

    print(args)