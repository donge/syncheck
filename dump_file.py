# -*- coding: utf-8 -*-


import json
from people import people
from pr import pr
from syncheck import Syncheck

PATH = "./static/db/"

def check(name):
    data_file = open(PATH+name+".json", "w+")
    try:
        data = json.load(data_file)
        return data["percent"]
    except:
        return 0
    data_file.close()
    return 0

def dump(name):
    print "DUMP" + name
    peo = people(name)
    pr_list = peo.prs()
    json_list = list()

    for pr_num in pr_list:
        i = pr(pr_num)
        print("-------Processing---------\r\n" + i.name())
        #get the first commit to check the result
        if i.commits():
            svn = i.commits()[0]
            s = Syncheck(svn)
            s.diff()
        else:
            continue

        post_pr = {
            'id': pr_num,
            'title': i.name(),
            'owner': name,
            'commit': svn,
            'checks': {
                'x44': s.check('x44'),
                'x46': s.check('x46'),
                'x47': s.check('x47'),
                'x48': s.check('x48'),
                'x49': s.check('x49'),
                'opt': s.check('opt'),
            }
        }

        print (post_pr)
        json_list.append(post_pr)
    #end for

    print json_list
    data = { "data": json_list }
    with open(PATH+name+".json", "w") as outfile:
        json.dump(data, outfile, indent=4)


if __name__ == '__main__':
    name = "dongdong"
    dump(name)

    '''
    delete()
    ids = post_people()
    post_works(ids)
    '''