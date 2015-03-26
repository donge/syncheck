from pr import pr
from syncheck import Syncheck
'''
def listing(**k):
    return config.DB.select('items', **k)
'''

def svns(name):
	a = pr(name)
	return a.commits()

def checks(name):
	a = Syncheck(name)
	return "hello"