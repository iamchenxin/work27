# -*- coding: utf-8 -*-
__author__ = 'z97'
import requests
import re
import os
import codecs
import sys
import json
import threading
import time

loggg={"word_count":0,"current_word":None,"badword_list":[]}
badword_list=[]
def log_Badword(word):
    global badword_list
    badword_list.append(word)

def log_store():
    global loggg
    with open("diclog.txt","w") as logfile:
        logfile.write( json.dumps(loggg))

class GET_WORD_END(Exception):
    pass
class BLOCK_BY_GOOGLE(Exception):
    pass

class gget:
    save_fold=None
    url="https://translate.google.com/translate_a/single?client=t&sl=en&" \
            "tl=zh-CN&hl=en&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk=521792|908008&q={0}"
    headers2={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'PREF=ID=bd73ccb4f260a5a1:U=ff0c25fa0733c544:FF=0:LD=en:TM=1427923010:LM=1431090871:GM=1:SG=1:S=I5W9cIxvlLFN1Xk5; NID=67=XVMQmMvxkk8fej3KJnUOrFgUki-ri2VtflPvJfDakzwRl3CmmNuxQKTEObgL_05sEZXhccHC2yflJ_-K7bRMOZlZQK1Er-bTJWF-dOGG1LnhC6Q5InyFaqP471W5oE2Sjc5ABt3Lb4dnHJ9mgfcvfa7oBidnj1NipQxSrh6bA4l7_jsRevNMbAbouoWwcB_-kmeiMh8sXMjX_tapChbxv-fOZ3a_qhfSdxg_2w; OGPC=5061492-8:4061155-11:5061451-64:; SID=DQAAAPwAAADO4aOIytUBqSz81WOgKp6eax49RBT962wZaUy_mIsP-XLDzVQoPoI57J5gqepF0WQ25yPZ2maa372qWmMb0C_hBqoKjC0kEzUt_aYCPKTJ9p91ScJq2kVrpjgbHN65mrYHn_gFWWqGkkV1lEls1gYMqv3So_tqmUid7TqOhNxhc-9PvICv3Fe63T5lZlF-GeDXOxn4914-q_3o9Y6EFL6G8mX09r1XeIbUHQRtZQN5kQ09I2nVjs6PP-1mTsSfsdpHnQ7r0bKVSKUX1I9OMJ-1P-Tv30bJb6JTUWadgmMYy9B-1-FcSOpDR5-nk60TQDBMNRotygFh_Vd60jqILUEx; HSID=Ap7etleiFDdzjU2ce; SSID=AsjXVP4ErIYy6cKsG; APISID=95o28o1MCSfsgUWi/AGjOkSKYJW-0YnnhF; SAPISID=4sRUwa8uCdZZQQnz/AYOq5tSOY_0s6gHcD; OGP=-5061492:'
    }

    def __init__(self,outfold):
        basedir =os.getcwd()
        self.save_fold=os.path.join(basedir,outfold)
        if os.path.exists(self.save_fold) is not True:
            os.mkdir(self.save_fold)

    def fetch(self,word):
        dsturl = self.url.format(word)

        ss=re.sub(r"[ ]+","_",word)

        fname=os.path.join(self.save_fold, "{0}.txt".format(ss))
        r = requests.get(dsturl,headers=self.headers2)
        ck_boot = re.search(r"<!DOCTYPE",r.text[:20])
        if ck_boot :
            print(r.text[:20])
            print("we are blocked by google,sleep 10 min ")
            time.sleep(600)
            print("awake ")
            log_Badword("blockedByGoogle")
            log_store()
            raise BLOCK_BY_GOOGLE("blockedby google")
        with codecs.open(fname,"w","utf-8") as f:
            f.write(r.text)


def init_wordfile(filename):
    global word_file
    try:
        word_file=open(filename,"r")
    except Exception as err:
        print("Read word's file error,please check the file '{0}' exist".format(filename))
        raise
word_free=True
word_file=None
block_count=0
def fget_word():
    global word_free
    global word_file
    global block_count
    while True:
        if word_free==True:
            word_free=False
            str=word_file.readline()
            rt=re.search(r"[\w]+",str)
            if rt:
                str=rt.group()

            if str == False:
                raise GET_WORD_END
            word_free=True
            block_count=0
            return str
        else:
            print("WORD READ BLOCKED~~~~~")
            block_count+=1
            if block_count>50:
                raise GET_WORD_END

def close_wordfile():
    word_file.close()








q_status=False
class fetchWorker(threading.Thread):
    def __init__(self,outfold,fget_word,name):
        threading.Thread.__init__(self)
        self.outfold=outfold
        self.fget_word=fget_word
        self.name=name
        self.dicfetch=gget(outfold)
        self.retry_word=None


    def run(self):
        global loggg
        global q_status
        print("runrunrun")
        word=None
        while q_status==False:
            try:
                if self.retry_word!=None:
                    self.dicfetch.fetch(self.retry_word)
                    print("{0} retry [{1}] success".format(self.name,self.retry_word))
                    self.retry_word=None  # if process it ,set to None
                else:
                    word=self.fget_word()
                    if word:
                        word=word.strip()
                        loggg["word_count"] = loggg["word_count"]+1
                        loggg["current_word"]=word
                        print("{0} read word [{1}]".format(self.name,word))
                        self.dicfetch.fetch(word)
            except requests.Timeout as timeout:
                print(timeout)
                print("{0} time out ->{1},try again".format(self.name, word))
                self.retry_word=word
                continue
            except BLOCK_BY_GOOGLE as err:
                print(err)
                self.retry_word=word
                continue
            except GET_WORD_END:
                print("words end ,exit all worker")
                q_status=True
            except Exception as err:
                loggg["badword_list"].append(word)
                print(str(err))
                print("!!!{0} can read this word".format(self.name))
                print("but {0} still read next word".format(self.name))
                continue


def mainloop():
    worker_list=[]
    init_wordfile("ext_word.txt")
    global q_status
    try:
        while True:
            keyin =raw_input()
            if keyin =="q":
                q_status=True
                keyin=None
            if keyin =="ex":
                q_status=True
                time.sleep(10)
                keyin=None
                break
            if keyin =="s":
                log_store()
                keyin=None
            if keyin!=None:
                worker=fetchWorker("ext",fget_word,keyin)
                worker_list.append(worker)
                worker.start()
    except Exception as err:
        log_store()
        print(err)
        raise
    finally:
        close_wordfile()




if __name__ == '__main__':
    mainloop()
