import os, re
import jinja2
from jinja2 import Environment, FileSystemLoader, Template
from pprint import pprint

PATTERN1 = re.compile(r"""#\s?\[TITLE]:\w?(.*)""")
PATTERN2 = re.compile(r"""#\s?\[DESCRIPTION]:\w?(.*)""")

def extract_the_shit(lines):
   data_title = "this is the title"
   data_desc = "this is the description"

   for i in lines:
       title = PATTERN1.match(i)
       desc = PATTERN2.match(i)
       if title:
           data_title = title.groups(0)[0]
       if desc:
           data_desc = desc.groups(0)[0]
           # http://jinja.pocoo.org/docs/2.10/api/
   return {"data_desc": data_desc, "data_title": data_title}


def bundle_lister():

    data = []

    for root, dirs, files in os.walk("./bundles", topdown=False):
        for name in files:
            with open(os.path.join(root, name)) as file_obj:
                lines = file_obj.readlines()
                data.append(extract_the_shit(lines))

    pprint(data)
    loader = jinja2.FileSystemLoader(searchpath='./') # Directory where TEMPLATE is; to be changed to URL path
    env = jinja2.Environment(loader=loader)
    template = env.get_template('template.html')
    output = template.render(data=data)
    with open('bundles01.html', 'w') as file:
        file.write(output)

bundle_lister()
