# -*- coding: utf-8 -*-
__author__ = 'z97'
import re
import os
import codecs
import sys
import json
from pymongo import MongoClient

def Get_OrBlank(list,key):
    try:
        rt=list[key]
    except IndexError:
        rt=""
    return rt

class Gl_mg():
    def __init__(self):
        pass



    def make_defzh(self,wordjson):
        simple_zh=wordjson["def_zh"]
        newzh={}

        try:
            def_full_zh=wordjson["def_full_zh"]
            for key in def_full_zh:
                sublen=len(def_full_zh[key])
                count=2 if sublen>=2 else 1
                subwlist=[]
                for i in range(count):
                    submean= def_full_zh[key][i]["zh"]
                    if submean== simple_zh:
                        simple_zh=""
                    subwlist.append(submean)
                newzh[key]=", ".join(subwlist)
            if simple_zh:
                newzh["unknown"]=simple_zh
        except Exception:
            newzh={}
            simple_zh=wordjson["def_zh"]
            try:
                def_more_zh=wordjson["def_more_zh"]
                sublen = len(def_more_zh)
                count= 3 if sublen>3 else sublen
                subwlist=[]
                for i in range(count):
                    submean=def_more_zh[i]["zh"]
                    if submean==simple_zh:
                        simple_zh=""
                    subwlist.append(submean)
                if simple_zh :
                    subwlist.append(simple_zh)

                newzh["unknown"]=", ".join(subwlist)

            except Exception:
                newzh["unknown"]=simple_zh

        return newzh

    def Build_more(self,src_file_f):

        with codecs.open(src_file_f,mode="r",encoding="utf-8") as f:
            wordjson=json.load(f,encoding="utf-8")

        newdef={}
        newdef["word"]=wordjson["word"]
        newdef["pron"]=wordjson["pron"] if wordjson["pron"] else ""
        newdef["zh"]=self.make_defzh(wordjson)
        newdef["en"]=wordjson["meaning"]

        return newdef

    def insert_tables_more(self,r_src_path):
        client = MongoClient()
        more_col=client.gldic.more

        base_path=os.getcwd()
        src_path=os.path.join(base_path,r_src_path)
        self.src_path=src_path

        f_list = os.listdir(src_path)
        f_list.sort()
        count=0
        for wfile in f_list:
            try:
                src_file_f=os.path.join(src_path,wfile)
                if os.path.isfile(src_file_f) == True:
                    newdef=self.Build_more(src_file_f)
                    rt=more_col.insert(newdef)
                    print(" %s ,"%(wfile),rt)
                    count+=1

            except Exception as err:
                print(err)
                raise err
        print(count)

def main():
    r_src_path=sys.argv[1]
    gl=Gl_mg()
    gl.insert_tables_more(r_src_path)

def test():
    gl=Gl_mg()
    rt=gl.Build_more("test/json12/elusive.json")
    print(rt)

if __name__ == '__main__':

    main()



