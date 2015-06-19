# -*- coding: utf-8 -*-
__author__ = 'z97'
import re
import os
import codecs
import sys
import json
import traceback
import MySQLdb

def Get_OrBlank(list,key):
    try:
        rt=list[key]
    except IndexError:
        rt=""
    return rt

class gldb():

    def __init__(self,user,passwd,dbname,host="localhost"):
        self.user=user
        self.passwd=passwd
        self.dbname=dbname
        self.host=host
        self.db_h=None

    def opendb(self):
        self.db_h=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.dbname,charset='utf8')
        return self.db_h.cursor()
    def closedb(self):
        if self.db_h:
            self.db_h.close()

    def make_defzh(self,wordjson):
        defzh=wordjson["def_zh"]
        build_str=""
        try:
            def_full_zh=wordjson["def_full_zh"]
            for key in def_full_zh:
                sublen = len(def_full_zh[key])
                count = 2 if sublen>2 else 1
                subwlist=[]
                for i in range(count):
                    submean= def_full_zh[key][i]["zh"]
                    if submean== defzh:
                        defzh=""
                    subwlist.append(submean)
                build_str+="[%s]: %s. "%(key,", ".join(subwlist))
            if defzh==True:
                build_str="%s ,%s"%( defzh,build_str)
        except Exception:
            build_str=""
            defzh=wordjson["def_zh"]
            try:
                def_more_zh=wordjson["def_more_zh"]
                sublen = len(def_more_zh)
                count= 3 if sublen>3 else sublen
                subwlist=[]
                for i in range(count):
                    submean=def_more_zh[i]["zh"]
                    if submean==defzh:
                        defzh=""
                    subwlist.append(submean)
                if defzh == True:
                    subwlist.append(defzh)
                build_str=", ".join(subwlist)
            except Exception:
                build_str=wordjson["def_zh"]
        return build_str

    def add_word_todb(self,src_file_f,db_cur):

        with codecs.open(src_file_f,mode="r",encoding="utf-8") as f:
            wordjson=json.load(f,encoding="utf-8")
        word=wordjson["word"]
        pron=wordjson["pron"] if wordjson["pron"]!=False else ""
        defsimp=self.make_defzh(wordjson)
        del wordjson["more_sen"]
        defmjson=json.dumps(wordjson,encoding="utf-8")

        sql_add_word=u'''INSERT INTO more (word,pron,defsimp,defmjson) VALUES ('%s','%s','%s','%s')'''%(word,pron,defsimp,defmjson)
        db_cur.execute(sql_add_word)

    def make_more_table(self,r_src_path):
        cur=self.opendb()
        cur.execute("set names utf8")
        sql_createtable='''
        CREATE TABLE `more`(
        `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `word` VARCHAR(56) NOT NULL DEFAULT '',
        `pron` VARCHAR(32) NOT NULL DEFAULT '',
        `defsimp` VARCHAR(128) NOT NULL DEFAULT '',
        `defmjson` VARCHAR(5120) NOT NULL DEFAULT '',
        PRIMARY KEY (`id`),
        UNIQUE KEY `word` (`word`)
        )ENGINE = MYISAM
'''

        cur.execute(sql_createtable)

        base_path=os.getcwd()
        src_path=os.path.join(base_path,r_src_path)
        self.src_path=src_path

        f_list = os.listdir(src_path)

        for wfile in f_list:
            try:
                if os.path.isfile(wfile) == True:
                    src_file_f=os.path.join(src_path,wfile)
                    self.add_word_todb(src_file_f,cur)

            except Exception:
                pass


    def add_simp_word(self,src_file_f,db_cur):
        with codecs.open(src_file_f,mode="r",encoding="utf-8") as f:
            wordjson=json.load(f,encoding="utf-8")
        word=wordjson["word"]
        pron=wordjson["pron"] if wordjson["pron"] else ""
        defsimp=self.make_defzh(wordjson)

        sql_add_word=u'''INSERT INTO simple (word,pron,defsimp) VALUES ('%s','%s','%s')'''%(word,pron,defsimp)
        print(sql_add_word)
        rt=db_cur.execute(sql_add_word)


    def make_simp_table(self,r_src_path):
        cur=self.opendb()

        sql_createtable='''
        CREATE TABLE `simple`(
        `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `word` VARCHAR(56) NOT NULL DEFAULT '',
        `pron` VARCHAR(32) CHARACTER SET utf8 NOT NULL DEFAULT '',
        `defsimp` VARCHAR(128) CHARACTER SET utf8 NOT NULL DEFAULT '',
        PRIMARY KEY (`id`),
        UNIQUE KEY `word` (`word`)
        )ENGINE = MYISAM
'''
        try:
            rt=cur.execute(sql_createtable)
            print(rt)
        except Exception:
            pass

        base_path=os.getcwd()
        src_path=os.path.join(base_path,r_src_path)
        self.src_path=src_path

        f_list = os.listdir(src_path)
        f_list.sort()
        for wfile in f_list:
            try:
                src_file_f=os.path.join(src_path,wfile)
                if os.path.isfile(src_file_f) == True:
                    self.add_simp_word(src_file_f,cur)

            except Exception as err:
                print(err)
                raise err


        self.closedb()

if __name__ == '__main__':
    gl=gldb("www-data","135790","gldic")

    r_src_path=sys.argv[1]
    gl.make_simp_table(r_src_path)