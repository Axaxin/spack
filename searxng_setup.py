import uuid
import random
import os
import re
import json


def modify_searxng():
    template='searxng/settings_template.yml'
    final='searxng/settings.yml'
    secretkey = uuid.uuid4().hex
    with open(template, "r", encoding="utf-8") as f1,open(final+'.temp', "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(re.sub(r'\$ultrasecretkey',secretkey,line))

    try:
        os.remove(final)
    except:
        pass
    os.rename(final+'.temp',final)

if __name__ == '__main__':
    modify_searxng()