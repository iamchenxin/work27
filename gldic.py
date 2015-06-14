# -*- coding: utf-8 -*-
__author__ = 'z97'
import re
import os
import codecs
import sys
import json
import traceback


class EXP_GLDIC(Exception):
    pass

class EXP_NONE_WORD(EXP_GLDIC):
    pass

class EXP_ODD_FILE(EXP_GLDIC):
    pass

class EXP_BAD_FILE(EXP_GLDIC):
    pass

class gldic():
    src_path=None
    dst_path=None

    def __init__(self,rel_src_path,rel_dst_path):

        basedir=os.getcwd()
        self.src_path=os.path.join(basedir,rel_src_path)
        self.dst_path=os.path.join(basedir,rel_dst_path)
        if os.path.exists(self.dst_path) !=True:
            os.mkdir(self.dst_path)

    def extract(self,filename):
        src_txt=None
        with codecs.open(filename,"r",encoding="utf-8") as src_file:
            src_txt=src_file.read()
        tmp=re.sub(r"\[,",'["",',src_txt)
        tmp=re.sub(r",,",',"",',tmp)
        tmp=re.sub(r",,",',"",',tmp)
        tmp=re.sub(r",,",',"",',tmp)


        try:
            jg=json.loads(tmp,encoding="utf-8")
        except ValueError as err:
            errstr=u"%s : %s  :  %s"%(err,filename,tmp)
            raise EXP_BAD_FILE(errstr)

        json_len=len(jg)
        print(json_len)
        jg_word_def=jg[0] # pron and def
        jg_full_zh_def=jg[1] #full zh meaning with en words
        jg_more_zh_def=jg[5] # more zh meaning
        jg_en_meaning = [] if json_len<13 else jg[12]  # en meaning
        jg_en_sentence= [] if json_len<14 else jg[13] # example sentence
        jg_seealso=[] if json_len<15 else jg[14] # see also


        #
        # word_def={
        #     "pron":" ",
        #     "meaning":{
        #         "verb":[{"m":" ","s":" "}, ],
        #         "noun":[{"m":" ","s":" "}, ],
        #     },
        #     "more_sen":[],
        #     "see_also":[],
        #     "def_zh":"",
        #     "def_more_zh":[{"zh":" ","fre":" "}, ],
        #     "def_full_zh":{
        #         "verb":[{"zh":" ","en":[]}, ],
        #         "noun":[{"zh":" ","en":" "}, ],
        #     }
        # }

        try:
            pron=jg_word_def[1][3]
        except Exception as err:
            pron=None

        try:
            def_zh=jg_word_def[0][0]
        except Exception as err:
            def_zh=None
            errstr=u"%s : %s  :  %s"%(err,filename,tmp)
            raise EXP_NONE_WORD(errstr)


        try:
            meaning = {}
            for subw in jg_en_meaning:
                pos = subw[0]
                sub_mean=[]
                for ms in subw[1]:
                    sub_mean.append({"mean":ms[0],"sen":ms[2]})
                meaning[pos]=sub_mean
            if meaning == {}:
                meaning=None
        except Exception as err:
            meaning=None


        try:
            en_sentence=[]
            for subs in jg_en_sentence[0]:
                en_sentence.append(subs[0])
        except Exception:
            en_sentence=None



        try:
            see_also=jg_seealso[0][:]
        except Exception:
            see_also=None

        try:
            more_zh=[]
            for subw in jg_more_zh_def[0][2]:
                more_zh.append({"zh":subw[0],"fre":subw[1]})
        except Exception as err:
            errstr=u"%s : %s  :  %s"%(err,filename,tmp)
            more_zh=None
            raise EXP_ODD_FILE(errstr)



        try:
            full_zh={}
            for subw in jg_full_zh_def:
                arr_zh_en=[]
                for zh_en_g in subw[2]:
                    arr_zh_en.append({"zh":zh_en_g[0],"en":zh_en_g[1][:]})

                full_zh[ subw[0]  ]=arr_zh_en
            if full_zh=={}:
                full_zh=None
        except Exception as err:
            errstr=u"%s : %s  :  %s"%(err,filename,tmp)
            full_zh=None
            raise EXP_ODD_FILE(errstr)



        word_def={
            "pron":pron,
            "meaning":meaning,
            "more_sen":en_sentence,
            "see_also":see_also,
            "def_zh":def_zh,
            "def_more_zh":more_zh,
            "def_full_zh":full_zh
        }
        return word_def


    def extract_batch(self):


        none_wordlist=[]
        odd_wordlist=[]

        src_list=os.listdir(self.src_path)
        bad_file_list=[]
        for src_file in src_list:
            try:
                src_full_f = os.path.join(self.src_path,src_file)
                if os.path.isfile(src_full_f) == True:
                    dst_full_f =os.path.join(self.dst_path,"%s.json"%(src_file.split(".")[0]))
                    word_json=self.extract(src_full_f)
                    with codecs.open(dst_full_f,"w",encoding="utf-8") as dst_f:
                        dst_f.write(json.dumps(word_json))
            except EXP_NONE_WORD as err:
                print(u" !!!!none word!! %s"%(err))
                none_wordlist.append(src_file)
            except EXP_ODD_FILE as err:
                print(u"-------odd word----- %s"%(err))
                odd_wordlist.append(src_file)
            except EXP_BAD_FILE as err:
                print(u"~~~~~BAD FILE----- %s"%(err))
                bad_file_list.append(src_file)
            except Exception as err:
                traceback.print_exc()
                print(err)
                raise Exception("What's wrong?")
            finally:
                if os.path.exists("./log") !=True:
                    os.mkdir("./log")
                with codecs.open("./log/none_wordlist.log","w",encoding="utf-8") as nw_f:
                    nw_f.write("\n".join(none_wordlist))
                with codecs.open("./log/odd_wordlist.log","w",encoding="utf-8") as od_f:
                    od_f.write("\n".join(odd_wordlist))
                with codecs.open("./log/bad_file.log","w",encoding="utf-8") as bad_f:
                    bad_f.write("\n".join(bad_file_list))



gl=gldic("f13","json13")
#gl.extract("f12/electrolytes")
#gl.extract("f12/aback.txt")
gl.extract_batch()
