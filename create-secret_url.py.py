# creates an empty credentials.py if it doesn't exist
import os.path

if not(os.path.exists('secret_url.py')):
    f = open('secret_url.py', 'w')
    f.write('secret_url = {\n    "URL": \'https://replace_this\'\n}')
