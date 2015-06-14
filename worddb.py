__author__ = 'z97'
import MySQLdb
import re
import json

def getword(wd):
    rep_word =re.compile(r"\b[\w]+\b")
    rt = rep_word.search(wd)
    if rt:
        return rt.group()
    else:
        raise RuntimeError("wrong word [%s]"%(wd))



def mread(filename):
    mf = open(filename,"r")
    hw=[
        ['head',['r','w']],
        ['head2',[]],
    ]
    headwords=[]
    rwords=[]
    words=mf.readlines()

    rep_word =re.compile(r"\b[\w]+\b")



    i=0
    pre_headword=''
    rank_level=0
    whole_l=len(words)
    while i<whole_l:
        wd = words[i]


        if wd[0]==' ': # relatedword
            rlist=wd.split(",")
            if pre_headword=='':
                raise RuntimeError("wrong in relate [%s],%d"%(wd,i))
            for rwd in rlist:
                rwords.append([getword(rwd),pre_headword,i-1]) # word , headword,headwordid->rank
            pre_headword=''


        elif wd[0]=='-':
            rt=re.search(r"\d+",wd)
            print(wd)
            if rt:
                rank_level=rt.group()

            else:
                raise RuntimeError("wrong in rank_level [%s],%d"%(wd,i))
        else: #headword
            pre_headword=getword(wd)
            rl_words=''
            if i+1<whole_l and words[i+1][0]==' ':
                rl_words=words[i+1]
                tmp=re.findall(r"\b[\w]+\b",rl_words)
                tmp2=list(set(tmp))
                rl_words=",".join(tmp2)
            headwords.append([pre_headword,rank_level,rl_words])
        i+=1

    to_single=[]
    for w_list in rwords:
        to_single.append(w_list[0])
    r_set=set(to_single)

    single_rwords=[]
    for w_list in rwords:
        if w_list[0] in r_set:
            single_rwords.append(w_list)
            r_set.remove(w_list[0])


    print(len(headwords))
    print(len(rwords))
    print(len(single_rwords))
    print(len(words))
    print(single_rwords[300:320])
    print(rwords[300:320])
    mf.close()


def store_to_dict(single_rwords,headwords):
    h_dict={}
    for w_list in headwords:
        h_dict[w_list[0]]=w_list[1:]

    with open("hw_dic.json","w") as mf:
        mf.write(json.dumps(h_dict))
    print("h_dict = %d"%(len(h_dict)))

    r_dict={}
    for w_list in single_rwords:
        r_dict[w_list[0]]=w_list[1]
    print("r_dict = %d"%(len(r_dict)))

    with open("rw_dic.json","w") as mf:
        mf.write(json.dumps(r_dict))

def db_headwords(headwords):
    db=MySQLdb.connect(host="localhost",user="www-data",passwd="135790",db="wordlist")
    cur=db.cursor()
    i=0
    for hwd in headwords:
        if hwd[2]:
            sql_add_head='''INSERT INTO headwords (word,rank,rankRange,relatedwords) VALUES ('%s','%d','%s','%s')'''%(hwd[0],i,hwd[1],hwd[2])
        else:
            sql_add_head='''INSERT INTO headwords (word,rank,rankRange) VALUES ('%s','%d','%s')'''%(hwd[0],i,hwd[1])
        print(sql_add_head)
        cur.execute(sql_add_head)
        i+=1

    db.close()

def db_rwords(rwords):
    db=MySQLdb.connect(host="localhost",user="www-data",passwd="135790",db="wordlist")
    cur=db.cursor()
    for w_list in rwords:
        sql_add_r='''INSERT INTO rwords (word,headword,headwordId) VALUES ('%s','%s','%d')'''%(w_list[0],w_list[1],w_list[2])
        cur.execute(sql_add_r)
    db.close()

def db_extwords(extwords):
    db=MySQLdb.connect(host="localhost",user="www-data",passwd="135790",db="wordlist")
    cur=db.cursor()
    for w_list in extwords:
        sql_add_r='''INSERT INTO extwords (word) VALUES ('%s')'''%(w_list)
        cur.execute(sql_add_r)
    db.close()

def testread(name):

    rep_ts=re.compile(r"\b[\w]+-[\w]+\b")
#    rep_ts=re.compile(r"[^\->\w, \n\r]")


    with open(name,"r") as mf:
        content=mf.read()
        rt = rep_ts.findall(content)
        print(len(rt))
        print(len(content))
        print(rt[0:200])

def testrp():
#    rep_ts=re.compile(r'(\b[\w]+-[^>]+?\b).+(\b[\w]+-[^>]+?\b)')
    rep_ts=re.compile(r'\b[\w]+\b')
    str = '''
      ->  be
    am, are -> [are], art -> [art], been, bei-ng -> [being], is, wa-ss, wast, were
in
    ins
    art -> [art], been, be-ing -> [
    '''
    str2="am, are -> [are], art -> [art], be-en, being -> [being], i-s, was,"
    rt = rep_ts.search(str)
    print (rt.group())

def extract(save_f="ext_word.txt",sub_f="2of12inf.txt",ext_1="5desk.txt",ext_2="6of12.txt"):
    sub_wf=[]
    ext_w1=[]
    ext_w2=[]
    rep_unword=re.compile(r"[^\w\n\r]")
    with open(sub_f,"r") as f1:
        sub_wf=f1.readlines()

    with open(ext_1,"r") as f2:
        for line in f2:
            if rep_unword.search(line) is None:
                ext_w1.append(line.lower())

    with open(ext_2,"r") as f3:
        for line in f3:
            if rep_unword.search(line) is None:
                ext_w2.append(line.lower())


    ext_all =ext_w1+ext_w2

    ext_set=set(ext_all)
    ext_list=list(ext_set)
    sub_set=set(sub_wf)

    remain_w=[]
    for word in ext_list:
        if word not in sub_set:
            remain_w.append(word)
    remain_w.sort()

    with open(save_f,"w") as sf:
        for w in remain_w:
            sf.write(w)

def insert_extword(ext_f="ext_word.txt"):
    rep_word=re.compile(r"\b[\w]+\b")
    ext_arr=[]
    with open(ext_f,"r") as ef:
        for line in ef:
            ext_arr.append(getword(line))
    db_extwords(ext_arr)

#mread('2+2gfreq.txt')
#testrp()
insert_extword()