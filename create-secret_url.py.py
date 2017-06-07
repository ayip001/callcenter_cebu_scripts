# creates an empty credentials.py if it doesn't exist
import os.path

if not(os.path.exists('credentials.py')):
    f = open('credentials.py', 'w')
    f.write('credentials = {\n    "API_USERNAME": \'replace_this\',\n    "API_PASSWORD": \'replace_this\'\n}')
