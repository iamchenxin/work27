# -*- coding: utf-8 -*-
__author__ = 'z97'
import re
import time
import threading
import os
import sys
import codecs

def test():
    str="----- 3231 -2----"
    rt=re.search(r"\d+",str)
    print(rt.group())



def test2():
    str="he-ew"
    rep_unword=re.compile(r"[^\w]")
    rt=rep_unword.search(str)
    print(rt)
    print(rt!=True)
    if rt is None:
        print(" all adc")

def test3():

    t='''
    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; charset=utf-8"><meta name="viewport" content="initial-scale=1"><title>https://translate.google.com/translate_a/single?client=t&amp;sl=en&amp;tl=zh-CN&amp;hl=en&amp;dt=bd&amp;dt=ex&amp;dt=ld&amp;dt=md&amp;dt=qca&amp;dt=rw&amp;dt=rm&amp;dt=ss&amp;dt=t&amp;dt=at&amp;ie=UTF-8&amp;oe=UTF-8&amp;source=bh&amp;ssel=0&amp;tsel=0&amp;kc=1&amp;tk=521792%7C908008&amp;q=ember</title></head>
    '''
    b='''
    [[["电解质","electrolytes"],[,,"Diànjiězhì"]],,"en",,,[["electrolytes",1,[["电解质",888,false,false],["电解液",111,false,false],["的电解质",0,false,false],["电解质的",0,false,false]],[[0,12]],"electrolytes",0,1]],1,,[["en"],,[1]],,,,,,[["electrolyte"]]]
    '''

    ck_boot = re.search(r"<!DOCTYPE",t[:20])
    if ck_boot is not None:
        print("we are blocked by google,sleep 10 min ")
        raise Exception("blockedby google")
    else:
        print("okokok")


def fffun(name):
    print("%s : %f"%(name,time.clock()))
    time.sleep(2)

class fetchWorker(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name =name

    def run(self):
        i=100
        while i>0:
            fffun(self.name)
            i-=1



def test4():
    td = fetchWorker("jim")
    td.start()
    time.sleep(0.5)
    tm = fetchWorker("hlishenj!")
    tm.start()


def test5():
    str= '''  [[["电解质","electrolytes"],[,,"Diànjiězhì"]],,"en",,,[["electrolytes",1,[["电解质",888,false,false],["电解液",111,false,false],["的电解质",0,false,false],["电解质的",0,false,false]],[[0,12]],"electrolytes",0,1]],1,,[["en"],,[1]],,,,,,[["electrolyte"]]]
'''
    str2='''
    [[["效果","effect"],[,,"Xiàoguǒ","iˈfekt"]],[["noun",["影响","效果","作用","效应","成效","功效","功用","结果","效"],[["影响",["influence","affect","effect"],,0.29559943],["效果",["effect","result","consequent","sequel","sound effects"],,0.2608656],["作用",["effect","action","function","activity","intention"],,0.097478345],["效应",["effect"],,0.093014486],["成效",["effect","result"]],["功效",["effect","efficacy"]],["功用",["function","effect","use"]],["结果",["result","bottom line","consequence","consequent","educt","effect"]],["效",["effect","efficacy"]]],"effect",1],["verb",["影响","招致"],[["影响",["influence","affect","effect"],,0.29559943],["招致",["lead to","incur","beget","court","draw down","effect"]]],"effect",2]],"en",,,[["effect",1,[["效果",733,false,false],["影响",138,false,false],["效应",66,false,false],["功效",36,false,false],["作用",24,false,false]],[[0,6]],"effect",0,1]],0.98994976,,[["en"],,[0.98994976]],,,[["noun",[[["result","consequence","upshot","outcome","repercussions","ramifications","end result","conclusion","culmination","corollary","concomitant","aftermath","fruit(s)","product","by-product","payoff","sequela"],"m_en_us1243233.001"],[["impact","action","effectiveness","influence","power","potency","strength","success","efficacy"],"m_en_us1243233.005"],[["force","operation","enforcement","implementation","effectiveness","validity","lawfulness","legality","legitimacy"],"m_en_us1243233.002"],[["sense","meaning","theme","drift","import","intent","intention","tenor","significance","message","gist","essence","spirit"],"m_en_us1243233.013"],[["belongings","possessions","goods","worldly goods","chattels","goods and chattels","property","paraphernalia","gear","tackle","things","stuff"],"m_en_us1243233.007"],[["impression"],""],[["burden","essence","core","gist"],""],[["consequence","event","upshot","result","issue","outcome"],""],[["force"],""]],"effect"],["verb",[[["achieve","accomplish","carry out","realize","manage","bring off","execute","conduct","engineer","perform","do","perpetrate","discharge","complete","consummate","cause","bring about","create","produce","make","provoke","occasion","generate","engender","actuate","initiate","effectuate"],"m_en_us1243233.008"],[["effectuate","set up"],""]],"effect"]],[["noun",[["a change that is a result or consequence of an action or other cause.","m_en_us1243233.001","the lethal effects of hard drugs"],["the lighting, sound, or scenery used in a play, movie, or broadcast.","m_en_us1243233.006","the production relied too much on spectacular effects"],["personal belongings.","m_en_us1243233.007","the insurance covers personal effects"]],"effect"],["verb",[["cause (something) to happen; bring about.","m_en_us1243233.008","nature always effected a cure"]],"effect"]],[[["However, the splashing water also created a nostalgic \u003cb\u003eeffect\u003c/b\u003e on the minds of onlookers.",,,,3,"m_en_us1243233.005"],["Most of us have said something of the sort on more than one occasion with little \u003cb\u003eeffect\u003c/b\u003e .",,,,3,"m_en_us1243233.003"],["he achieved a beautiful \u003cb\u003eeffect\u003c/b\u003e with the paint",,,,3,"neid_5939"],["The marches that take place occasionally against crime are meaningless and of no \u003cb\u003eeffect\u003c/b\u003e .",,,,3,"m_en_us1243233.003"],["the new law had little \u003cb\u003eeffect\u003c/b\u003e on people",,,,3,"neid_5937"],["The closure will take \u003cb\u003eeffect\u003c/b\u003e in February, pending consultation.",,,,3,"m_en_us1243233.002"],["In Britain, the experience of the revolution had a liberating \u003cb\u003eeffect\u003c/b\u003e on people's minds.",,,,3,"m_en_us1243233.005"],["wind power can be used to great \u003cb\u003eeffect\u003c/b\u003e",,,,3,"m_en_us1243233.003"],["With the rule changes on hold, we now have the opportunity to void them for good - before they ever take \u003cb\u003eeffect\u003c/b\u003e .",,,,3,"m_en_us1243233.002"],["it had an adverse \u003cb\u003eeffect\u003c/b\u003e on her",,,,3,"neid_5938"],["the treatment had no \u003cb\u003eeffect\u003c/b\u003e on his condition",,,,3,"neid_5937"],["This could represent an important source of bias and in a worst case scenario could have a large \u003cb\u003eeffect\u003c/b\u003e on the results.",,,,3,"m_en_us1243233.001"],["The soundtrack is used to great \u003cb\u003eeffect\u003c/b\u003e in most scenes, dubious effect in some.",,,,3,"m_en_us1243233.003"],["A large \u003cb\u003eeffect\u003c/b\u003e on compliance resulted from a relatively small intervention effort.",,,,3,"m_en_us1243233.001"],["the book had a profound \u003cb\u003eeffect\u003c/b\u003e on me",,,,3,"neid_5937"],["The move towards more transparency was expected to take \u003cb\u003eeffect\u003c/b\u003e by the end of this year or early next year.",,,,3,"m_en_us1243233.002"],["The new rental policy will not come into \u003cb\u003eeffect\u003c/b\u003e until the outcome of a court appeal which is expected tomorrow.",,,,3,"m_en_us1243233.002"],["All very understandable, but the \u003cb\u003eeffect\u003c/b\u003e on the impressionable minds of our intellectual class has been deleterious.",,,,3,"m_en_us1243233.005"],["But he fears the campaign could have a damaging \u003cb\u003eeffect\u003c/b\u003e on impressionable teenagers.",,,,3,"m_en_us1243233.005"],["Labour and Conservatives seem to have forgotten that the student population is large enough to have an \u003cb\u003eeffect\u003c/b\u003e on the election results.",,,,3,"m_en_us1243233.001"],["By analogy, the electromagnetic radiation emitted by a moving object also exhibits the Doppler \u003cb\u003eeffect\u003c/b\u003e .",,,,3,"m_en_us1243233.004"],["Becket was armed with letters from the Pope which would take \u003cb\u003eeffect\u003c/b\u003e upon delivery.",,,,3,"m_en_us1243233.002"],["The long journey and the early start were beginning to take \u003cb\u003eeffect\u003c/b\u003e .",,,,3,"m_en_us1243233.002"],["If all that sounds worryingly alcoholic, fear not: the whole \u003cb\u003eeffect\u003c/b\u003e was wonderfully impressive.",,,,3,"m_en_us1243233.005"],["He is trotted out to play a hulking but child-like soldier to no great \u003cb\u003eeffect\u003c/b\u003e .",,,,3,"m_en_us1243233.003"],["The revisions take \u003cb\u003eeffect\u003c/b\u003e from this week, says a bank press release.",,,,3,"m_en_us1243233.002"],["Its parapets, grand staircases and sheltered side gardens are used to great \u003cb\u003eeffect\u003c/b\u003e .",,,,3,"m_en_us1243233.003"],["the Doppler \u003cb\u003eeffect\u003c/b\u003e",,,,3,"m_en_us1243233.004"],["Clever lighting prevents it from being too dark, though, and the overall \u003cb\u003eeffect\u003c/b\u003e is impressive.",,,,3,"m_en_us1243233.005"],["We could see low-lying islands in the Pacific totally disappear as a result of the \u003cb\u003eeffect\u003c/b\u003e of greenhouse gases.",,,,3,"m_en_us1243233.001"]]],[["side effect","in effect","greenhouse effect","sound effect","special effect","cause and effect","take effect","adverse effect","put into effect","ripple effect"]]]
    '''

    str3='''
    [[["后","back"],[,,"Hòu","bak"]],[["noun",["背面","后","后面","后边","后部","后身","脊","脊背","腰","腰杆子"],[["背面",["back","rear","reverse","reverse side","wrong side"],,0.043936934],["后",["queen","back","behind","empress","offspring","rear"],,0.032651156],["后面",["behind","back","rear"],,0.026235942],["后边",["behind","back","rear"]],["后部",["rear","back","behind"]],["后身",["back","rear"]],["脊",["ridge","spine","back","vertebra"]],["脊背",["back"]],["腰",["waist","back","small of the back","loin","middle"]],["腰杆子",["back","backing","support"]]],"back",1],["adverb",["向后","以前"],[["向后",["backward","back","backwards","towards the back","behind"],,0.011825466],["以前",["before","back","formerly"]]],"back",4],["adjective",["后边的","后部的","后的","后面的"],[["后边的",["back"]],["后部的",["back"]],["后的",["back"]],["后面的",["back"]]],"back",3],["verb",["赌钱","冀","襄","翊","支持"],[["赌钱",["gamble","back","bet","game","play","speculate"]],["冀",["aim","aspire","back","bargain","expect","gasp"]],["襄",["aid","assist","be of assistance","back","lend a hand","help"]],["翊",["assist","back","cheer","defer","give a hand","lend a hand"]],["支持",["support","back","bear","buttress","carry along","countenance"]]],"back",2]],"en",,,[["back",1,[["后",317,false,false],["背部",267,false,false],["后面",236,false,false],["背面",160,false,false],["后面的",18,false,false]],[[0,4]],"back",0,1]],1,,[["en"],,[1]],,,[["adjective",[[["rear","rearmost","backmost","hind","hindmost","hinder","posterior"],"m_en_us1224262.035"],[["past","old","previous","earlier","former","out of date"],"m_en_us1224262.037"],[["hinder","hind"],""]],"back"],["adverb",[[["backward","behind one","to one's rear","rearward","away","off"],"m_en_us1224262.014"],[["ago","earlier","previously","before","in the past"],"m_en_us1224262.020"],[["backward"],""],[["rearwards","rearward","backwards","backward"],""]],"back"],["noun",[[["spine","backbone","spinal column","vertebral column"],"m_en_us1224262.003"],[["rear","rear side","other side","stern"],"m_en_us1224262.008"],[["end","tail end","rear end","rear","tail","tag end"],"m_en_us1224262.008"],[["reverse","other side","underside","verso","flip side"],"m_en_us1224262.010"],[["backrest"],""],[["dorsum"],""],[["rachis","spine","vertebral column","backbone","spinal column"],""],[["rear"],""],[["binding","cover"],""]],"back"],["verb",[[["sponsor","finance","put up the money for","fund","subsidize","underwrite","be a patron of","act as guarantor of","foot the bill for","pick up the tab for","bankroll","stake"],"m_en_us1224262.023"],[["support","endorse","sanction","approve of","give one's blessing to","smile on","favor","advocate","promote","uphold","champion","vote for","ally oneself with","stand behind","stick by","side with","be on the side of","defend","take up the cudgels for","second","throw one's weight behind"],"m_en_us1224262.023"],[["bet on","gamble on","stake money on"],"m_en_us1224262.024"],[["reverse","draw back","step back","move backward","back off","pull back","retreat","withdraw","give ground","backtrack","retrace one's steps","recede"],"m_en_us1224262.030"],[["bet on","stake","punt","game","gage"],""],[["back up"],""],[["plump for","support","plunk for","indorse","endorse"],""],[["indorse","second","endorse"],""]],"back"]],[["adjective",[["of or at the back of something.","m_en_us1224262.035","the back garden"],["(especially of wages or something published or released) from or relating to the past.","m_en_us1224262.037","she was owed back pay"],["directed toward the rear or in a reversed course.","m_en_us1224262.038","back currents"],["(of a sound) articulated at the back of the mouth.","m_en_us1224262.039","Back vowels have their name because the sound resonates at the back of the mouth."]],"back"],["adverb",[["toward the rear; in the opposite direction from the one that one is facing or traveling.","m_en_us1224262.014","she moved back a pace"],["expressing a return to an earlier or normal condition.","m_en_us1224262.018","she put the book back on the shelf"],["in or into the past.","m_en_us1224262.020","he made his fortune back in 1955"],["in return.","m_en_us1224262.022","they wrote back to me"]],"back"],["noun",[["the rear surface of the human body from the shoulders to the hips.","m_en_us1224262.001","he lay on his back"],["the side or part of something that is away from the spectator or from the direction in which it moves or faces; the rear.","m_en_us1224262.008","at the back of the hotel is a secluded garden"],["a player in a field game whose initial position is behind the front line.","m_en_us1224262.012","their backs showed some impressive running and passing"]],"back"],["verb",[["give financial, material, or moral support to.","m_en_us1224262.023","he had a newspaper empire backing him"],["cover the back of (an object) in order to support, protect, or decorate it.","m_en_us1224262.027","a mirror backed with tortoiseshell"],["walk or drive backward.","m_en_us1224262.030","she tried to back away"],["(of a property) have its back adjacent to (a piece of land or body of water).","m_en_us1224262.033","a row of cottages backed on the water"]],"back"]],[[["she put the file in the \u003cb\u003eback\u003c/b\u003e of the drawer",,,,3,"neid_1515"],["There are residential facilities, but most pitch a tent on land at the \u003cb\u003eback\u003c/b\u003e of the centre.",,,,3,"m_en_us1224262.008"],["she turned to the girls in the \u003cb\u003eback\u003c/b\u003e",,,,3,"neid_1516"],["Mrs Gaspar grabbed at her arm as she ran past her and out onto the \u003cb\u003eback\u003c/b\u003e verandah.",,,,3,"m_en_us1224262.035"],["When I reserved back, they threw a big rock out of my garden through the \u003cb\u003eback\u003c/b\u003e window.",,,,3,"m_en_us1224262.035"],["It was there that I found him, leaning \u003cb\u003eback\u003c/b\u003e in his chair, one foot propped on Connie's lap.",,,,3,"m_en_us1224262.015"],["she was seated with her \u003cb\u003eback\u003c/b\u003e to the door",,,,3,"neid_1513"],["Go \u003cb\u003eback\u003c/b\u003e a few years and past examples of new indices and trackers don't inspire much confidence either.",,,,3,"m_en_us1224262.020"],["I don the headset, close my notebook, turn off the overhead light and lean \u003cb\u003eback\u003c/b\u003e to enjoy the movie.",,,,3,"m_en_us1224262.015"],["The supermodel and her companion then stood up and moved to the \u003cb\u003eback\u003c/b\u003e of the bar.",,,,3,"m_en_us1224262.008"],["\u003cb\u003eback\u003c/b\u003e somersault",,,,3,"neid_1500"],["he was lying on his \u003cb\u003eback\u003c/b\u003e",,,,3,"neid_1513"],["The bank are on their \u003cb\u003eback\u003c/b\u003e , and it would be prudent not to deny the possibility of a quick sale at the right price.",,,,3,"m_en_us1224262.007"],["The good folks \u003cb\u003eback\u003c/b\u003e home would never know the difference.",,,,3,"m_en_us1224262.021"],["It takes the pressure off and you can be more selective about which races you \u003cb\u003eback\u003c/b\u003e horses in.",,,,3,"m_en_us1224262.024"],["he's \u003cb\u003eback\u003c/b\u003e drinking again",,,,3,"neid_1486"],["Kan leaned \u003cb\u003eback\u003c/b\u003e against his office chair and crossed both feet at the corner of his desk.",,,,3,"m_en_us1224262.015"],["his father broke his \u003cb\u003eback\u003c/b\u003e in an accident",,,,3,"neid_1513"],["In the centre is a minuscule island housing a former monastery which dates \u003cb\u003eback\u003c/b\u003e to the ninth century.",,,,3,"m_en_us1224262.020"],["Tests showed that he had broken a vertebrae in his \u003cb\u003eback\u003c/b\u003e and cracked a rib and will be out for several weeks at least.",,,,3,"m_en_us1224262.003"],["Meanwhile, \u003cb\u003eback\u003c/b\u003e at the camp Sara sat in her tent and ran her fingers through her hair.",,,,3,"m_en_us1224262.021"],["When this failed they moved around to the \u003cb\u003eback\u003c/b\u003e and tried to unsuccessfully open the kitchen window.",,,,3,"m_en_us1224262.008"],["I am afraid, but I am also relieved that we will be able to get our lives \u003cb\u003eback\u003c/b\u003e to normal again.",,,,3,"m_en_us1224262.018"],["The night was such a success that spectators paid to stand at the \u003cb\u003eback\u003c/b\u003e of the hall after all the seats were filled.",,,,3,"m_en_us1224262.008"],["she came home a couple of years \u003cb\u003eback\u003c/b\u003e",,,,3,"neid_1491"],["When Grant first conceived the film project a decade \u003cb\u003eback\u003c/b\u003e he wrote to her.",,,,3,"m_en_us1224262.020"],["I smiled \u003cb\u003eback\u003c/b\u003e at him, a little confused, but followed the direction of his gaze.",,,,3,"m_en_us1224262.022"],["Once the floodwaters had peaked, it was still days before water levels were \u003cb\u003eback\u003c/b\u003e to normal.",,,,3,"m_en_us1224262.018"],["The man then remembered he had a ticket in his \u003cb\u003eback\u003c/b\u003e pocket that had been through the wash a few times.",,,,3,"m_en_us1224262.035"],["I can see four or five rigids a few miles \u003cb\u003eback\u003c/b\u003e thermalling up at my level and a couple higher.",,,,3,"m_en_us1224262.016"]]],[["come back","go back","be right back","get back","welcome back","back up","call back","bring back","hold back","laid back"]]]
    '''


    tmp=re.sub(r"\[,",'["",',str3)
    tmp=re.sub(r",,",',"",',tmp)
    tmp=re.sub(r",,",',"",',tmp)
    tmp=re.sub(r",,",',"",',tmp)

    print(tmp)

def test6():
    for dirpath,dirs,files in os.walk(os.getcwd()):
        print (dirpath)
        print("\niam dir:\n")
        for dd in dirs:
            print(dd)

        print("\niam file!!:\n")
        for ff in files:
            print(ff)

def test7():
    basedir=os.getcwd()
    flist=os.listdir(basedir)
    for ff in flist:
        if os.path.isfile(os.path.join(basedir,ff)) ==True:
            print("!!!!!!![%s]"%(ff))
        else:
            print(ff)

def test8():

    jg=[["000",],["1111",],["2222",],["3333",],["4444",],["66555",]]
    json_len=len(jg)
    print(json_len)
    jg_en_meaning = [] if 2>=json_len else jg[2]  # en meaning
    jg_en_sentence= [] if json_len<4 else jg[3] # example sentence
    jg_seealso=[] if json_len<7 \
        else jg[6] # see also

    print (jg_en_meaning)
    print (jg_en_sentence)
    print (jg_seealso)

def test9():
    str='''
[[["热闹","liven"],[,,"Rènào","ˈlīvən"]],[["verb",["使 ... 快乐起来"],[["使 ... 快乐起来"]],"liven",2]],"en",,,[["liven",1,[["热闹",541,false,false],["搞活",397,false,false],["炒热",61,false,false],["活跃气氛",0,false,false],["助兴",0,false,false]],[[0,5]],"liven",0,1]],0.83838385,,[["en"],,[0.83838385]],,,[["verb",[[["animate","enliven","liven up","invigorate"],""]],"liven"]],[["verb",[["make or become more lively or interesting.","m_en_us1263912.001","liven up bland foods with a touch of mustard"]],"liven"]],[[["the match didn't \u003cb\u003eliven\u003c/b\u003e up until the second half",,,,3,"m_en_gb0475870.001"],["A close pal can \u003cb\u003eliven\u003c/b\u003e up an afternoon by announcing that her new love interest has, without warning, moved to Chicago.",,,,3,"m_en_us1263912.001"],["However, in the third quarter the game began to \u003cb\u003eliven\u003c/b\u003e up and for once I was interested in the plays.",,,,3,"m_en_us1263912.001"],["the match didn't \u003cb\u003eliven\u003c/b\u003e up until the second half",,,,3,"m_en_us1263912.001"],["The chamber is looking for people with new ideas and fresh input to \u003cb\u003eliven\u003c/b\u003e things up and help promote the town's business interests.",,,,3,"m_en_us1263912.001"],["\u003cb\u003eliven\u003c/b\u003e up bland foods with a touch of mustard",,,,3,"m_en_us1263912.001"],["\u003cb\u003eliven\u003c/b\u003e up bland foods with a touch of mustard",,,,3,"m_en_gb0475870.001"],["A lively debate helps \u003cb\u003eliven\u003c/b\u003e up the evening, exercises the mind and gets the blood flowing.",,,,3,"m_en_us1263912.001"],["The author's wry sense of humour \u003cb\u003elivens\u003c/b\u003e the narration and sometimes some passages seem to touch on topics not merely medical.",,,,3,"m_en_us1263912.001"],["The waterslide town is also known for its annual arts fest, which \u003cb\u003elivens\u003c/b\u003e up the Laurentians every August with classical music and dance for nine days straight.",,,,3,"m_en_us1263912.001"],["On the other hand, suspending all rational powers of disbelief and gasping out loud in glee can be great fun, and \u003cb\u003elivens\u003c/b\u003e up a mundane weekday evening.",,,,3,"m_en_us1263912.001"],["Sometimes a colorful insult or description \u003cb\u003elivens\u003c/b\u003e up a detailed argument.",,,,3,"m_en_us1263912.001"],["Counting beads \u003cb\u003elivens\u003c/b\u003e up math class for young students.",,,,3,"m_en_us1263912.001"],["The model might have been a real maja - one of the bright young things of questionable virtue who \u003cb\u003elivened\u003c/b\u003e up the streets of Madrid, the way Goths and gender-benders do today.",,,,3,"m_en_us1263912.001"],["Who cares; fact is, they've \u003cb\u003elivened\u003c/b\u003e up the charts with bright and tuneful pop music that reveals exactly as much as you want at the moment.",,,,3,"m_en_us1263912.001"],["I guess I'd better get this book so I can enrich my life while \u003cb\u003elivening\u003c/b\u003e up my daily commute!",,,,3,"m_en_us1263912.001"],["Now, I'm all for \u003cb\u003elivening\u003c/b\u003e up political debate with evocative language and different means of expression, but I did find this one a bit too cryptic.",,,,3,"m_en_us1263912.001"],["The other parties in this collusion shall, of course, remain nameless - but thank you for \u003cb\u003elivening\u003c/b\u003e up what would have otherwise been an astoundingly dull evening.",,,,3,"m_en_us1263912.001"],["This colourful collection of adverts certainly \u003cb\u003elivens\u003c/b\u003e up what would otherwise be just another dilapidated shop, and acts as an unofficial noticeboard of the latest music releases.",,,,3,"m_en_us1263912.001"],["Self-medication simply \u003cb\u003elivens\u003c/b\u003e up the process for spectators and riders alike.",,,,3,"m_en_us1263912.001"],["Musical rhythms from symphonic masterpieces are translated into sequences of stripes and colours, \u003cb\u003elivening\u003c/b\u003e up an inspired line of clothing that comes with a CD as a free gift.",,,,3,"m_en_us1263912.001"],["So they set about \u003cb\u003elivening\u003c/b\u003e it up (or dumbing it down, depending on your viewpoint.)",,,,3,"m_en_us1263912.001"],["Potent purple pigments in the blueberries are excellent for \u003cb\u003elivening\u003c/b\u003e up the arteries, while their vitamin C content wakes up the immune system.",,,,3,"m_en_us1263912.001"],["All those hours of driving them to to rehearsals and waiting for them to finish seemed worth it as kids lined up on stage and pranced about in attractive costumes, \u003cb\u003elivening\u003c/b\u003e up the show.",,,,3,"m_en_us1263912.001"]]],[["liven up"]]]
'''

    tmp=re.sub(r"\[,",'["",',str)

    tmp=re.sub(r",,",',"",',tmp)
    tmp=re.sub(r",,",',"",',tmp)
    tmp=re.sub(r",,",',"",',tmp)

    print(tmp)

def test10():
    for i in range(len(sys.argv)):
        print("%d => %s\n"%(i,sys.argv[i]))

def re_bad():
    base_path=os.getcwd()
    src_path=os.path.join(base_path,"bad_file")

    f_list = os.listdir(src_path)
    f_list.sort()

    for w_list in f_list:
        src_file_f=os.path.join(src_path,w_list)
        with codecs.open(src_file_f,mode="r",encoding="utf-8") as f:
            str_txt=f.read()
        tmp=re.sub(r"\[,",'["",',str_txt)

        tmp=re.sub(r",,",',"",',tmp)
        tmp=re.sub(r",,",',"",',tmp)
        tmp=re.sub(r",,",',"",',tmp)

        print(tmp)

re_bad()