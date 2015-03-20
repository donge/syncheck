import web
from syncheck import Syncheck

urls = (
    '/svn/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
        	return 'Please input a SVN number' + name
        a = Syncheck(name)
        a.diff()
        ret_val = '<html>Hello, The commit of SVN: ' + name + '<br>'
        if(a.check('x44')):
        	ret_val = ret_val + ' maybe not in X44!<br>'
        else:
        	ret_val = ret_val + ' is already in X44!<br>'
        if(a.check('x46')):
        	ret_val = ret_val + ' maybe not in X46!<br>'
        else:
        	ret_val = ret_val + ' is already in X46!<br>'
        if(a.check('x47')):
        	ret_val = ret_val + ' maybe not in X47!<br>'
        else:
        	ret_val = ret_val + ' is already in X47!<br>'
        if(a.check('x48')):
        	ret_val = ret_val + ' maybe not in X48!<br>'
        else:
        	ret_val = ret_val + ' is already in X48!<br>'
        if(a.check('x49')):
        	ret_val = ret_val + ' maybe not in X49!<br>'
        else:
        	ret_val = ret_val + ' is already in X49!<br>'
        if(a.check('opt')):
        	ret_val = ret_val + ' maybe not in OPT!<br>'
        else:
        	ret_val = ret_val + ' is already in OPT!<br>'

		ret_val = ret_val + '</html>'
        return ret_val


if __name__ == "__main__":
    app.run()