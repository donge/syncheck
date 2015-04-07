
# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

X_DOMAINS = '*'
X_ALLOW_CREDENTIALS = True
X_HEADERS = 'Access-Control-Allow-Origin'
X_EXPOSE_HEADERS = 'Access-Control-Allow-Origin'

people = {
    'additional_lookup':{
        'url': 'regex("[\w]+")',
        'field': 'alias'
    },
    'schema': {
        'alias': {
            'type': 'string',
            'minlength' : 1,
            'maxlength' : 20,
            'required': True,
            'unique': True,
        },
    }
}

pr = {
    'additional_lookup':{
        'url': 'regex("[\w]+")',
        'field': 'owner'
    },
    'schema': {
        'id': {
            'type': 'string',
            'minlength' : 5,
            'maxlength' : 10,
            'required': True,
            'unique': True,
        },  
        'title': {
            'type': 'string',
            'required': True,
        },
        'owner': {
            'type': 'string',
            'required': True,
            #'data_relation': {
            #    'resource': 'people',
            #    'embeddable': True,
            #},
        },
        'arrival-date': {
            'type': 'datetime',
        },
        'commits': {
            'type': 'list',
        }
    }
}
            

commit = {
    'additional_lookup':{
        'url': 'regex("[\w]+")',
        'field': 'svn_id'
    },
    'schema': {
        'svn_id': {
            'type': 'string',
            'required': True,
        },
        'checks': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'version': {'type': 'string'},
                    'result': {'type': 'boolean', 'default': False},
                },
            },
        },
    }
}




DOMAIN = {
    'people': people,
    'pr': pr,
    'commit': commit,
}

