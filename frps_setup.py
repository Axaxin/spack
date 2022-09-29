import uuid
import random
import os
import re
import json

def modify_frps(token):
    template='frps/template.ini'
    final='frps/frps.ini'
    with open(template, "r", encoding="utf-8") as f1,open(final+'.temp', "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(re.sub(r'\$my_token',token,line))

    try:
        os.remove(final)
    except:
        pass
    os.rename(final+'.temp',final)

if __name__ == '__main__':
    token = uuid.uuid4().hex
    modify_frps(token)

    resfile = 'info.json'
    with open(resfile,'r',encoding='utf-8') as jsonfile:
        data=json.load(jsonfile)

    data['frps']['token']=token
    with open(resfile,'w',encoding='utf-8') as jsonfile:
        json.dump(data,jsonfile,indent=4)