import uuid
import random
import os
import re
import json

def modify_v2fly(vport,vid,vpath):
    file='v2fly/config.json'
    with open(file, "r", encoding="utf-8") as jsonfile:
        data=json.load(jsonfile)

    data['inbounds'][0]['port']=vport
    data["inbounds"][0]['settings']['clients'][0]['id']= vid
    data["inbounds"][0]['streamSettings']['wsSettings']['path']=vpath

    with open(file, "w", encoding="utf-8") as jsonfile:
        json.dump(data,jsonfile,ensure_ascii=False,indent=4)



if __name__ == '__main__':
    vport = random.randint(10012,65100)
    vid = str(uuid.uuid4())
    vpath = '/'+uuid.uuid4().hex[-1:20:-1]+'-vless'

    modify_v2fly(vport,vid,vpath)

    resfile = 'info.json'
    # res = {
    #     'port':vport,
    #     'id':vid,
    #     'path':vpath
    # }
    with open(resfile,'r',encoding='utf-8') as jsonfile:
        data=json.load(jsonfile)

    data['v2fly']['port']=vport
    data['v2fly']['id']=vid
    data['v2fly']['path']=vpath

    with open(resfile,'w',encoding='utf-8') as jsonfile:
        json.dump(data,jsonfile,indent=4)







