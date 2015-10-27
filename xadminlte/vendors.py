'''
Created on Oct 20, 2015

@author: jrm
'''
from xadmin import vendors

# Update 
vendors.vendors.update({
    'bootstrap':{
        'js': {
            'dev': 'xadminlte/bootstrap/js/bootstrap.js',
            'production': 'xadminlte/bootstrap/js/bootstrap.min.js',
            'cdn': 'http://netdna.bootstrapcdn.com/twitter-bootstrap/3.2.2/js/bootstrap.min.js'
        },
        'css': {
            'dev': 'xadminlte/bootstrap/css/bootstrap.css',
            'production': 'xadminlte/bootstrap/css/bootstrap.css',
            'cdn': 'http://netdna.bootstrapcdn.com/twitter-bootstrap/3.2.2/css/bootstrap-combined.min.css'
        },
        'responsive': {'css':{
                'dev': 'xadminlte/bootstrap/bootstrap-responsive.css',
                'production': 'xadminlte/bootstrap/bootstrap-responsive.css'
            }
        }
    },
    'bootstrap-wysihtml5': {
        'js': {
            'dev':'xadminlte/plugins/bootstrap-wysihtml5/bootstrap3-wysihtml5.all.js',
            'production':'xadminlte/plugins/bootstrap-wysihtml5/bootstrap3-wysihtml5.all.min.js',
        },
        'css': {
            'dev':'xadminlte/plugins/bootstrap-wysihtml5/bootstrap3-wysihtml5.all.css',
            'production':'xadminlte/plugins/bootstrap-wysihtml5/bootstrap3-wysihtml5.all.min.css',
        }
    },
   "bootstrap-wysiwyg": {
        "css": {
            'dev': 'xadminlte/plugins/bootstrap-wysiwyg/bootstrap-wysiwyg.css',
        },                    
        "js": {
            'dev': ['xadminlte/plugins/bootstrap-wysiwyg/bootstrap-wysiwyg.js',
                    'xadminlte/plugins/bootstrap-wysiwyg/external/jquery.hotkeys.js',
                    'xadminlte/plugins/bootstrap-wysiwyg/external/google-code-prettify/prettify.js'
                    ],
        }
    },
    #"select": {
    #    "css": {
    #        'dev': ['xadminlte/plugins/select2/select2.css', 'xadmin/vendor/selectize/selectize.css', 'xadmin/vendor/selectize/selectize.bootstrap3.css'],
    #    },
    #    "js": {
    #        'dev': ['xadmin/vendor/selectize/selectize.js', 'xadminlte/plugins/select2/select2.js', 'xadminlte/plugins/select2/i18n/%(lang)s.js'],
    #        'production': ['xadmin/vendor/selectize/selectize.min.js', 'xadminlte/plugins/select2/select2.min.js', 'xadminlte/plugins/select2/i18n/%(lang)s.js']
    #    }
    #},
    "font-awesome": {"css":{'dev':'xadminlte/plugins/font-awesome-4.4.0/css/font-awesome.css',
                            'production':'xadminlte/plugins/font-awesome-4.4.0/css/font-awesome.css',
                            'cdn':'https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css'}},
})