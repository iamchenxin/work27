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


def Get_OrNone(list,index):
    return None if len(list)<(index+1) else list[index]

def Get_OrExp(list,index):
    try:
        rt=list[index]
    except Exception as err:
        stk=traceback.format_stack()
        if len(stk)>2:
            str=stk[-3:-1]
        else:
            str=stk
        raise EXP_ODD_FILE("\n".join(str))
    return rt

class gldic():
    src_path=None
    dst_path=None

    def __init__(self,rel_src_path,rel_dst_path,rel_log_path):

        basedir=os.getcwd()
        self.src_path=os.path.join(basedir,rel_src_path)
        self.dst_path=os.path.join(basedir,rel_dst_path)
        self.log_path=os.path.join(basedir,rel_log_path)
        if os.path.exists(self.dst_path) !=True:
            os.mkdir(self.dst_path)
        if os.path.exists(self.log_path) !=True:
            os.mkdir(self.log_path)

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
            errstr=u"%s : %s  : def_zh=jg_word_def[0][0]"%(err,filename)
            raise EXP_NONE_WORD(errstr)

        word = Get_OrExp(Get_OrExp(jg_word_def,0),1)


        try:
            meaning = {}
            for subw in jg_en_meaning:
                pos = subw[0]
                sub_mean=[]
                for ms in subw[1]:
                    sub_mean.append({"mean":Get_OrExp(ms,0),"sen":Get_OrExp(ms,2)})
                meaning[pos]=sub_mean
            if meaning == {}:
                meaning=None
        except Exception as err:
            meaning=None


        try:
            en_sentence=[]
            for subs in jg_en_sentence[0]:
                en_sentence.append(Get_OrExp(subs,0))
        except Exception:
            en_sentence=None



        try:
            see_also=jg_seealso[0][:]
        except Exception:
            see_also=None

        try:
            more_zh=[]
            for subw in jg_more_zh_def[0][2]:
                more_zh.append({"zh":Get_OrExp(subw,0),"fre":Get_OrExp(subw,1)})
        except Exception as err:
            errstr=u"%s : %s  :  more_zh_def= index 5"%(err,filename)
            more_zh=None
            raise EXP_ODD_FILE(errstr)



        try:
            full_zh={}
            for subw in jg_full_zh_def:
                arr_zh_en=[]
                for zh_en_g in subw[2]:
 #                   arr_zh_en.append({"zh":zh_en_g[0],"en":zh_en_g[1][:]})
                    try:
                       zzen= zh_en_g[1][:]
                    except Exception:
                        zzen=None
                    arr_zh_en.append({"zh":Get_OrExp(zh_en_g,0),"en":zzen})

                full_zh[ subw[0]  ]=arr_zh_en
            if full_zh=={}:
                full_zh=None
        except IndexError as err:
            errstr=u"%s : %s  :  full_zh_def= index 1"%(err,filename)
            full_zh=None
            raise EXP_ODD_FILE(errstr)



        word_def={
            "word":word,
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

        log_list=[]
        log_none_wordlist=os.path.join(self.log_path,"none_wordlist.log")
        log_odd_wordlist=os.path.join(self.log_path,"odd_wordlist.log")
        log_bad_file=os.path.join(self.log_path,"bad_file.log")
        log_log=os.path.join(self.log_path,"log.log")

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
                print(u"-------odd word----- %s"%(src_file))
                odd_wordlist.append(src_file)
                log_list.append("%s-----------------\n"%(src_file))
                log_list.append(err.__str__())
            except EXP_BAD_FILE as err:
                print(u"~~~~~BAD FILE----- %s"%(err))
                bad_file_list.append(src_file)
            except Exception as err:
                traceback.print_exc()
                print(err)
                with codecs.open(log_none_wordlist,"w",encoding="utf-8") as nw_f:
                    nw_f.write("\n".join(none_wordlist))
                with codecs.open(log_odd_wordlist,"w",encoding="utf-8") as od_f:
                    od_f.write("\n".join(odd_wordlist))
                with codecs.open(log_bad_file,"w",encoding="utf-8") as bad_f:
                    bad_f.write("\n".join(bad_file_list))
                with codecs.open(log_log,"w",encoding="utf-8") as log_f:
                    log_f.write("\n\n".join(log_list))
                raise Exception("What's wrong?")
            finally:
                pass
        with codecs.open(log_none_wordlist,"w",encoding="utf-8") as nw_f:
            nw_f.write("\n".join(none_wordlist))
        with codecs.open(log_odd_wordlist,"w",encoding="utf-8") as od_f:
            od_f.write("\n".join(odd_wordlist))
        with codecs.open(log_bad_file,"w",encoding="utf-8") as bad_f:
            bad_f.write("\n".join(bad_file_list))
        with codecs.open(log_log,"w",encoding="utf-8") as log_f:
            log_f.write("\n\n".join(log_list))

    def mv_none_word(self):

        log_list=[]
        none_wordlist=[]
        new_wordlist=[]
        log_log=os.path.join(self.log_path,"log.log")
        log_none_wordlist=os.path.join(self.log_path,"none_wordlist.log")
        log_new_wordlist=os.path.join(self.log_path,"new_wordlist.log")

        src_list=os.listdir(self.src_path)
        for src_file in src_list:
            try:
                src_full_f =os.path.join(self.src_path,src_file)
                word=re.search(r"\b[\w]+\b",src_file).group()
                print(word)
                if os.path.isfile(src_full_f) == True:
                    with codecs.open(src_full_f,"r",encoding="utf-8") as src_f:
                        srcjson=json.load(src_f,encoding="utf-8")
                    if srcjson['def_zh']==word:  # this word is none
                        if srcjson['def_more_zh'][0]['zh']!=word:
                            srcjson['def_zh']=srcjson['def_more_zh'][0]['zh']
                        else:
                            for key in srcjson['def_full_zh']:
                                if srcjson['def_full_zh'][key][0]["zh"]!=word:
                                    srcjson['def_zh']=srcjson['def_full_zh'][key][0]["zh"]
                        if srcjson['def_zh']==word:

                            print("INININ NONE! : %s"%(word))
                            raise Exception("NONE WORD")
                        else:
                            with codecs.open(src_full_f,"w",encoding="utf-8") as back_f:
                                json.dump(srcjson,back_f)
                            new_wordlist.append(src_file)
            except Exception:
                print("OUT NONE~~ : %s"%(word))
                dst_full_f=os.path.join(self.dst_path,src_file)
                os.rename(src_full_f,dst_full_f)
                none_wordlist.append(src_file)

        with codecs.open(log_new_wordlist,"w",encoding="utf-8") as new_f:
            new_f.write("\n".join(new_wordlist))
        with codecs.open(log_none_wordlist,"w",encoding="utf-8") as none_f:
            none_f.write("\n".join(none_wordlist))
        with codecs.open(log_log,"w",encoding="utf-8") as log_f:
            log_f.write("\n\n".join(log_list))


if __name__ == '__main__':
    src_path=sys.argv[1]
    dst_path=sys.argv[2]
    log_path=sys.argv[3]
    gl=gldic(src_path,dst_path,log_path)
    #gl.extract("f12/electrolytes")
    #gl.extract("f12/aback.txt")
    gl.extract_batch()
#    gl.mv_none_word()