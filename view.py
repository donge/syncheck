import web
import db

t_globals = dict(
  datestr=web.datestr,
)
render = web.template.render('templates/', cache=False,
    globals=t_globals)
render._keywords['globals']['render'] = render

def listing(**k):
    l = {}
    return render.list(l)

def list_svns(name):
    l = db.svns(name)
    return render.svns(l)

def list_checks(name):
    l = db.checks(name)
    return render.checks(l)