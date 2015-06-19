# -*- coding: utf-8 -*-
__author__ = 'z97'
import requests
import re
import json
import os

def test1(word):

    url="https://translate.google.com/translate_a/single?client=t&sl=en&" \
        "tl=zh-CN&hl=en&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk=521792|908008&q={0}"
    headers2={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Cookie': 'PREF=ID=bd73ccb4f260a5a1:U=ff0c25fa0733c544:FF=0:LD=en:TM=1427923010:LM=1431090871:GM=1:SG=1:S=I5W9cIxvlLFN1Xk5; NID=67=XVMQmMvxkk8fej3KJnUOrFgUki-ri2VtflPvJfDakzwRl3CmmNuxQKTEObgL_05sEZXhccHC2yflJ_-K7bRMOZlZQK1Er-bTJWF-dOGG1LnhC6Q5InyFaqP471W5oE2Sjc5ABt3Lb4dnHJ9mgfcvfa7oBidnj1NipQxSrh6bA4l7_jsRevNMbAbouoWwcB_-kmeiMh8sXMjX_tapChbxv-fOZ3a_qhfSdxg_2w; OGPC=5061492-8:4061155-11:5061451-64:; SID=DQAAAPwAAADO4aOIytUBqSz81WOgKp6eax49RBT962wZaUy_mIsP-XLDzVQoPoI57J5gqepF0WQ25yPZ2maa372qWmMb0C_hBqoKjC0kEzUt_aYCPKTJ9p91ScJq2kVrpjgbHN65mrYHn_gFWWqGkkV1lEls1gYMqv3So_tqmUid7TqOhNxhc-9PvICv3Fe63T5lZlF-GeDXOxn4914-q_3o9Y6EFL6G8mX09r1XeIbUHQRtZQN5kQ09I2nVjs6PP-1mTsSfsdpHnQ7r0bKVSKUX1I9OMJ-1P-Tv30bJb6JTUWadgmMYy9B-1-FcSOpDR5-nk60TQDBMNRotygFh_Vd60jqILUEx; HSID=Ap7etleiFDdzjU2ce; SSID=AsjXVP4ErIYy6cKsG; APISID=95o28o1MCSfsgUWi/AGjOkSKYJW-0YnnhF; SAPISID=4sRUwa8uCdZZQQnz/AYOq5tSOY_0s6gHcD; OGP=-5061492:'
}
    dsturl = url.format(word)
    try:
        r = requests.get(dsturl,headers=headers2)
    except Exception as err:
        print("open --{0}-- err".format(dsturl),err)
    else:
        print (r.encoding)
        print(r.text)
        tmp=re.sub(r"\[,",'["",',r.text)
        tmp=re.sub(r",,",',"",',tmp)
        tmp=re.sub(r",,",',"",',tmp)
        tmp=re.sub(r",,",',"",',tmp)
        print(tmp)


def test2():
    str='''
    [[["放弃","abandon"],[,,"Fàngqì","əˈbandən"]],[["verb",["放弃","抛弃","弃","舍弃","背弃","摈弃","屏","屏弃","丢弃","废弃","罢休","抛","撇弃","朅","扔下","舍","捐"],
    [["放弃",["give up","abandon","abdicate","abnegate","back out","cede"],,0.44374731],["抛弃",["abandon","discard","cast aside","cast away","cast off","desert"],,0.13533528],
    ["弃",["abandon","discard","relinquish","throw away"],,0.1157584],["舍弃",["give up","abandon","abnegate","fail","abort"],,0.029268308],["背弃",["abandon","desert","renounce"]],
    ["摈弃",["abandon","discard","cast away"]],["屏",["abandon","reject","shield"]],["屏弃",["reject","abandon","discard"]],["丢弃",["discard","abandon","dice","fall away"]],
    ["废弃",["discard","idle","antiquate","cast aside","cast away","abandon"]],["罢休",["give up","abandon","forsake","give over","leave","let it go"]],
    ["抛",["throw","cast","toss","abandon","cast off","fling"]],["撇弃",["abandon","cast away","discard"]],["朅",["abandon","leave"]],
    ["扔下",["abandon","fling off"]],["舍",["give alms","give up","abandon"]],["捐",["donate","abandon","contribute","subscribe","tax"]]],"abandon",2]],
    "en",,,[["abandon",1,[["放弃",745,false,false],["抛弃",191,false,false],["弃",53,false,false],["舍弃",10,false,false],
    ["摒弃",0,false,false]],[[0,7]],"abandon",0,1]],0.86868685,,[["en"],,[0.86868685]],,,
    [["verb",[[["renounce","relinquish","dispense with","disclaim","forgo","disown","disavow","discard","wash one's hands of","give up","withdraw","drop","jettison","do away with","ax","ditch","dump","scrap","scrub","junk","deep-six","forswear","abjure"],"m_en_us1219230.001"],[["give up","stop","cease","drop","forgo","desist from","dispense with","have done with","abstain from","discontinue","break off","refrain from","set aside","cut out","kick","pack in","quit"],"m_en_us1219230.001"],
    [["desert","leave","leave high and dry","turn one's back on","cast aside","break (up) with","jilt","strand","leave stranded","leave in the lurch","throw over","walk out on","run out on","dump","ditch","forsake"],"m_en_us1219230.003"],[["vacate","leave","depart from","withdraw from","quit","evacuate"],"m_en_us1219230.009"],[["relinquish","surrender","give up","cede","yield","leave"],"m_en_us1219230.006"],[["indulge in","give way to","give oneself up to","yield to","lose oneself to/in"],"m_en_us1219230.007"],
    [["give up"],""],[["empty","vacate"],""],[["desert","forsake","desolate"],""]],"abandon"],["noun",[[["uninhibitedness","recklessness","lack of restraint","lack of inhibition","wildness","impulsiveness","impetuosity","immoderation","wantonness"],"m_en_us1219230.008"],[["wildness"],""],[["unconstraint","wantonness"],""]],"abandon"]],[["verb",[["give up completely (a course of action, a practice, or a way of thinking).","m_en_us1219230.001","he had clearly abandoned all pretense of trying to succeed"],
    ["cease to support or look after (someone); desert.","m_en_us1219230.003","her natural mother had abandoned her at an early age"],["allow oneself to indulge in (a desire or impulse).","m_en_us1219230.007","abandoning herself to moony fantasies"]],"abandon"],["noun",[["complete lack of inhibition or restraint.","m_en_us1219230.008","she sings and sways with total abandon"]],"abandon"]],[[["However, as a result of strong winds and driving rain, the team eventually decided to \u003cb\u003eabandon\u003c/b\u003e the session.",,,,3,"m_en_us1219230.002"],["In such circumstances sailors who do not have to go to sea do not go to sea and at half past ten on Sunday morning the decision was taken to \u003cb\u003eabandon\u003c/b\u003e racing.",,,,3,"m_en_us1219230.002"],["When they abandon their fields to seek new ones, they also \u003cb\u003eabandon\u003c/b\u003e their village sites.",,,,3,"m_en_us1219230.004"],["We can't go wild and start attacking with total \u003cb\u003eabandon\u003c/b\u003e .",,,,3,"m_en_us1219230.008"],["House builders have warned that Bradford workers could \u003cb\u003eabandon\u003c/b\u003e the district because of a huge shortfall in the number of homes built in the next decade.",,,,3,"m_en_us1219230.004"],["But mothers who \u003cb\u003eabandon\u003c/b\u003e their babies anonymously have no easy way to learn of the child's status or prove their maternity in time to appear and contest the adoption.",,,,3,"m_en_us1219230.003"],["France were much quicker in setting up scoring chances but they squandered them with the reckless \u003cb\u003eabandon\u003c/b\u003e of a gambler, certain the luck would hold all night.",,,,3,"m_en_us1219230.008"],["Three days of fog finally forced PGA officials to \u003cb\u003eabandon\u003c/b\u003e the tournament.",,,,3,"m_en_us1219230.002"],["This time around, reckless \u003cb\u003eabandon\u003c/b\u003e has given way to cautious and deliberate strokes.",,,,3,"m_en_us1219230.008"],["However, the company doesn't want to \u003cb\u003eabandon\u003c/b\u003e the practice, and hopes new technology will improve the return on investment.",,,,3,"m_en_us1219230.001"],["I drove recklessly and with total \u003cb\u003eabandon\u003c/b\u003e as I sped as fast as I could through the suburban streets of Redmond.",,,,3,"m_en_us1219230.008"],["All this is described with a certain gay \u003cb\u003eabandon\u003c/b\u003e and without any overtones of regret, yet Wright's behaviour rapidly became self-destructive.",,,,3,"m_en_us1219230.008"],["I could no longer walk the plank or shoot down enemy fighters with the same reckless \u003cb\u003eabandon\u003c/b\u003e .",,,,3,"m_en_us1219230.008"],["They had been forced to \u003cb\u003eabandon\u003c/b\u003e the event ‘due to circumstances beyond our control’.",,,,3,"m_en_us1219230.002"],["I was privileged to be secretary of the Navy when the decision was made to \u003cb\u003eabandon\u003c/b\u003e the draft.",,,,3,"m_en_us1219230.001"],["But, unfortunately, some parents seem to be oblivious to this perception and \u003cb\u003eabandon\u003c/b\u003e such children to their fate.",,,,3,"m_en_us1219230.006"],["The devices are now being used with reckless \u003cb\u003eabandon\u003c/b\u003e .",,,,3,"m_en_us1219230.008"],["it was an attempt to persuade businesses not to \u003cb\u003eabandon\u003c/b\u003e the area to inner-city deprivation",,,,3,"m_en_us1219230.006"],["In the first 25 minutes, there was some exquisite rugby, where the balance between well-judged enterprise and reckless \u003cb\u003eabandon\u003c/b\u003e was carefully maintained.",,,,3,"m_en_us1219230.008"],["Her Juliet is delicate and gentle, her suicide a mix of restrained classicism and \u003cb\u003eabandon\u003c/b\u003e .",,,,3,"m_en_us1219230.008"],["she sings and sways with total \u003cb\u003eabandon\u003c/b\u003e",,,,3,"m_en_us1219230.008"],["an attempt to persuade businesses not to \u003cb\u003eabandon\u003c/b\u003e the area to inner-city deprivation",,,,3,"m_en_gb0000580.003"],["Never had I seen him move with such \u003cb\u003eabandon\u003c/b\u003e , such reckless expression of his feelings.",,,,3,"m_en_us1219230.008"],["Approach love and cooking with reckless \u003cb\u003eabandon\u003c/b\u003e .",,,,3,"m_en_us1219230.008"],["After he proposed numerous remodeling schemes, the clients opted to \u003cb\u003eabandon\u003c/b\u003e the original plan in favor of an entirely new structure.",,,,3,"m_en_us1219230.001"],["When one party is in power, they spend with reckless \u003cb\u003eabandon\u003c/b\u003e .",,,,3,"m_en_us1219230.008"],["The results could be quite elegant, but sometimes lacked the feeling of \u003cb\u003eabandon\u003c/b\u003e and adventure present in the music's greatest improvised solos.",,,,3,"m_en_us1219230.008"],["After months of madness in the house, they decided to \u003cb\u003eabandon\u003c/b\u003e the place and move back to Philadelphia.",,,,3,"m_en_us1219230.004"],["Consistency and cost issues were key in Whitworth College's decision to \u003cb\u003eabandon\u003c/b\u003e outsourcing.",,,,3,"m_en_us1219230.001"],["In addition, United's decision to \u003cb\u003eabandon\u003c/b\u003e its workers' pension plan could reverberate throughout the industry.",,,,3,"m_en_us1219230.001"]]],[["to abandon","abandon all hope","abandon oneself to"]]]

    '''
    tmp=re.sub(r"\[,",'["",',str)
    tmp=re.sub(r",,",',"",',tmp)
    tmp=re.sub(r",,",',"",',tmp)
    tmp=re.sub(r",,",',"",',tmp)
    jj=json.loads(tmp)
    print(tmp)
    print(jj)

def test3(word):
    basedir =os.getcwd()
    print(basedir)
    mdir = os.path.join(basedir,"f12")
    extdir = os.path.join(basedir,"ext")
    print(mdir)
    print(extdir)
    ss=re.sub(r"[ ]+","_",word);
    print (os.path.join(mdir,ss))
    print(os.path.exists(mdir))
    if os.path.exists(mdir) is not True:
        print ("create dir")
        os.mkdir(mdir)



test3("gogee go")
#test2()