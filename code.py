import web
import view
from view import render
import json
from syncheck import Syncheck
import dump_file
from multiprocessing import Pool

urls = (
    '/', 'index',
    '/pr/(\d+)', 'pr',
    '/svn/(\d+)', 'svn',
    '/report/(\w+)', 'report',
)

class index:
    def GET(self):
        return render.base(view.listing())

class pr:
    def GET(self, name):
        return render.base(view.list_svns(name))

class report:
    def GET(self, name):
        percent = dump_file.check(name)
        if (percent == 0):
            # Async call to dump the files
            #pool = Pool(processes=1)
            #pool.apply_async(dump_file.dump, [name], None)
            dump_file.dump(name)

        data = {
            'progress': percent,
        }

        return json.dumps(data)

class svn:
    def GET(self, name):
        if not name:
            data = {
             'error': 'Please input a SVN number',
            }

        a = Syncheck(name)
        a.diff()

        data = {
            'commit': name,
            'checks': {
                'x44': a.check('x44'),
                'x46': a.check('x46'),
                'x47': a.check('x47'),
                'x48': a.check('x48'),
                'x49': a.check('x49'),
                'opt': a.check('opt'),
            }
        }

        return json.dumps(data)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
