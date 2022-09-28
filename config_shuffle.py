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

def modify_v2fly():
    file='v2fly/config.json'
    with open(file, "r", encoding="utf-8") as jsonfile:
        data=json.load(jsonfile)

    data['inbounds'][0]['port']=random.randint(10012,65100)
    data["inbounds"][0]['settings']['clients'][0]['id']= str(uuid.uuid4())
    data["inbounds"][0]['streamSettings']['wsSettings']['path']='/'+uuid.uuid4().hex[-1:20:-1]+'-vless'

    with open(file, "w", encoding="utf-8") as jsonfile:
        json.dump(data,jsonfile,ensure_ascii=False,indent=4)

def modify_frps():
    template='frps/template.ini'
    final='frps/frps.ini'
    token = uuid.uuid4().hex
    with open(template, "r", encoding="utf-8") as f1,open(final+'.temp', "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(re.sub(r'\$my_token',token,line))

    try:
        os.remove(final)
    except:
        pass
    os.rename(final+'.temp',final)

if __name__ == '__main__':
    modify_searxng()
    modify_v2fly()
    modify_frps()




