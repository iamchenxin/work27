__author__ = 'z97'
import MySQLdb
import re

def test():
    db=MySQLdb.connect(host="localhost",user="www-data",passwd="135790",db="wordlist")
    cur=db.cursor()

    str='''abandon,accountable,adolescent,adversary,affect,agoge,annihilation,arcadian,ascent,assault,astinos,athenians,baptized,batters,blackness,blacksmith,blasphemies,blasphemy,
    bodyguard,bribe,campaign,captive,carneia,chamber,claim,clash,claws,coastal,combat,commitment,compound,conquers,conspires,constantly,corridor,corrupt,council,councilman,coy,crowns,
    curse,customary,d,daxos,dearest,defy,delivered,demoralized,destiny,devour,diplomatic,discarded,diseased,doesn,doesrt,drunken,eager,embraced,emissary,empire,entertaining,ephors,
    exaggerate,families,fangs,fathers,fingers,fitting,fraction,freed,freedoms,funnel,fury,gates,gather,gathered,gleaming,glorious,glowing,gossip,grabbed,greece,greek,greeks,grips,hadrt,
    handful,happened,harder,heightened,hell,holy,hurricane,imagining,immortals,inbred,initiation,inspected,insult,isn,issued,jewels,kings,lash,lecherous,leonidas,lips,ll,lmmortals,lord,
    loses,losses,lungs,madman,madness,makes,manufactured,massive,mers,messenger,milady,misshapen,mood,motherless,mystics,nerve,numbers,oracle,oracles,ordered,orders,persia,persian,
    persians,philosophers,phocian,pines,pit,plunged,pompous,potter,pray,priests,profession,protocol,provoked,punished,puny,radiant,rebuilding,remnants,reputation,reserve,rests,retreat,
    returned,returns,rivers,rob,rod,rotten,rumor,sacred,sacrifice,sake,savoring,scent,scouting,sculptor,secrecy,seek,seems,senseless,shakes,shield,shields,sickly,sire,
    slavery,slaves,smash,sniffing,snuff,softness,soldiers,sons,souls,sparta,spartan,spartans,spartars,speaks,spear,spears,stabs,started,starves,steady,steps,stretching,stroll,stronger,
    submission,superior,surprises,surrender,swine,sword,swords,sworn,taking,terrain,tested,theron,threaten,
    threatens,thunderbolts,token,tongues,tossed,tricked,villagers,violence,vote,wages,walls,warmth,warpath,warrior,warriors,winds,windswept,wits,womars,worthless,wretches,xerxes,zeus
    '''

    tmp=str.split(",")
    w_list=[]
    for w in tmp:
        w_list.append(re.search(r"\b[\w]+\b",w).group())
    out="'%s'"%(w_list[0])
    for wd in w_list[1:]:
        out+=",'%s'"%(wd)


    sql_sel_hd='''SELECT  * FROM headwords WHERE word IN (%s)'''%(out)
    print(sql_sel_hd)
    rt=cur.execute(sql_sel_hd)
    hw_data=cur.fetchall()

    sql_sel_r='''SELECT  * FROM rwords WHERE word IN (%s)'''%(out)
    rt=cur.execute(sql_sel_r)
    r_data=cur.fetchall()

    set_hw=set()
    for wl in hw_data:
        set_hw.add(wl[1])
    set_r=set()
    for wl in r_data:
        set_r.add(wl[1])


    unword=[]
    for w in w_list:
        if w not in set_hw:
            if w not in set_r:
                unword.append(w)
                print(w)
    db.close()
    print(len(hw_data))
    print(len(r_data))
    print(r_data)
    print(len(unword))
    print(len(w_list))


test()