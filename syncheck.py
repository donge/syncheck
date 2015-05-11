
import ssh

sandboxes = {
    "x44": '/homes/slt-builder/sandboxes/DEV_X_121_X44_BRANCH/current/src',
    "x46": '/homes/slt-builder/sandboxes/DEV_X_121_X46_BRANCH/current/src',
    "x47": '/homes/slt-builder/sandboxes/DEV_X_121_X47_BRANCH/current/src',
    "x48": '/homes/slt-builder/sandboxes/DEV_X_123_X48_BRANCH/current/src',
    "x49": '/homes/slt-builder/sandboxes/DEV_X_12Q3_SRX_BRANCH/current/src',
    "opt": '/homes/slt-builder/sandboxes/DEV_S3_SRX_R2T_BRANCH/current/src'
}

class Syncheck:
    def __init__(self, name):
        self.s = ssh.Connection('eng-shell4.juniper.net', 'regress', password = 'MaRtInI')
        self.pr = name
        self.tmp = '~/temp_' + name
        print('Init ' + name)
        return

    def diff(self):
        self.s.execute('svn diff -c ' + self.pr + ' https://svl-svn.juniper.net/svn/junos-2009 > '+ self.tmp)
        return

    def check(self, name):
        sb = sandboxes[name]
        out = self.s.execute('cd ' + sb +';patch -p2 -C -R -f < ' + self.tmp)
        print(out)
        if any('ignore' in w for w in out):
            return False
        elif any('failed' in w for w in out):
            return False
        else:
            return True

    def __del__(self):
        print('del ')
        self.s.execute('rm -f ' + self.tmp)
        self.s.close()

'''
telnet API
s.put('/home/warrior/hello.txt', '/home/zombie/textfiles/report.txt')
s.get('/var/log/strange.log', '/home/warrior/serverlog.txt')
'''
if __name__ == '__main__':
    a = Syncheck('609996')
    a.diff()
    if (a.check('opt')):
        print("Commit is already there")
    else:
        print("Commit maybe not there")
