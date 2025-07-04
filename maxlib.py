#
#info:
'''
Python="3.13.5"
creater="Kinecraft_kk"
import="from maxlib import *"
'''
#import:
import os, sys, random, time, socket, json, shutil
from decimal import Decimal
#<class 'int'>
#raise ValueError("")
#help cods:
#sys.set_int_max_str_digits(0)
#sys.setrecursionlimit(10000)
#cods:
'''def read(nom=""):
    t=[]
    f=""
    for i in [f for i,f in enumerate(open("maxlib.py").readline())][1:-1]:
        if i == ";":
            t.append(f)
            f=""
        else:f+=str(i)
    if nom == "":return t
    else:return t[int(nom)]
def zap(text,nom="new"):
    g=[i.rstrip() for i in open("maxlib.py")]
    z=g[0][1:]
    g=g[1:]
    t=[]
    f=""
    for i in z:
        f+=str(i)
        if i == ";":
            t.append(f)
            f=""
    if nom == "new":
        if text == "":t=[]
        else:t.append(str(text)+";")
    else:
        if text == "":del(t[int(nom)])
        else:t[int(nom)]=str(text)+";"
    tt=""
    for i in t:tt+=str(i)
    g.insert(0,"#"+tt)
    gg=""
    for i in g:gg+=str(i)+"\n"
    open("maxlib.py", 'w').write(gg).close()'''
def blok():
    sys.set_int_max_str_digits(0)
    sys.setrecursionlimit(10000)
def delete_module(modname):del sys.modules[modname]
def settype(text,typ,st=0,stc=""):
    typ=str(typ)
    if typ == "str" or typ == "<class 'str'>":
        if st==0:return str(text)
        else:return str(spis_in_lin(text,stc))
    elif typ == "int" or typ == "<class 'int'>":
        if st==0:return int(text)
        else:return int(spis_in_lin(text,stc))
    elif typ == "bol" or typ == "<class 'float'>":
        if st==0:return float(text)
        else:return float(spis_in_lin(text,stc))
    elif typ == "bool" or typ == "<class 'bool'>":
        if st==0:return bool(text)
        else:return bool(spis_in_lin(text,stc))
    elif typ == "complex" or typ == "<class 'complex'>":
        if st==0:return complex(text)
        else:return complex(spis_in_lin(text,stc))
    elif typ == "dict" or typ == "<class 'dict'>":return dict(text)
    elif typ == "list" or typ == "<class 'list'>":return list(text)
    elif typ == "set" or typ == "<class 'set'>":return set(text)
    elif typ == "tuple" or typ == "<class 'tuple'>":return tuple(text)
def spis_in_lin(spis,typ=""):
    b=""
    if typ == "":
        for i in spis:b+=str(i)
    else:
        for i in spis:b+=str(i)+str(typ)
    return b
def lin_in_spis(lin,typ="",prom=0,save=False):
    spis=[]
    if str(type(typ)) == "<class 'tuple'>" or str(type(typ)) == "<class 'list'>" or str(type(typ)) == "<class 'set'>" or str(type(typ)) != "<class 'dict'>":mor=1
    else:mor=0
    h=""
    if typ == "" and prom == 0:
        for u in list(lin):
            spis.append(u)
    else:
        for u in list(lin):
            if len(h) == prom and prom != 0:
                if save != False:h+=str(u)
                spis.append(h)
                h=""
            elif str(u) != "" and str(u) == str(typ) and str(typ) != "" and mor == 0:
                if save != False:h+=str(u)
                spis.append(h)
                h=""
            elif str(typ) != "" and mor == 1:
                none=True
                for i in typ:
                    if str(i) == str(u):
                        none=False
                        if save != False:h+=str(u)
                        if str(h) != "":spis.append(h)
                        h=""
                        break
                if none:h+=str(u)
            else:h+=str(u)
        if h != "":
            spis.append(h)
    return spis
def searsh_sim(lin,sim,v=1):
    lin,sim=str(lin),str(sim)
    if len(sim) == 1:
        if v == 1:
            m=0
            for n in lin:
                if n == sim:m+=1
            return m
        elif v == 2:
            m=[]
            for i,n in enumerate(lin):
                if n == sim:
                    m.append(i)
            return m
    elif len(sim) > 1:
        if v == 1:
            sk=""
            pov=0
            for i in lin:
                if len(sk) == len(sim):
                    if sk == sim:
                        pov+=1
                    sk+=i;sk=sk[1:]
                else:sk+=i
            return pov
        elif v == 2:
            sk=""
            pov=[]
            for n,i in enumerate(lin):
                if len(sk) == len(sim):
                    if sk == sim:
                        pov.append([n-len(sk),n])
                    sk+=i;sk=sk[1:]
                else:sk+=i
            return pov
def calculator(prim):
    with open("wremwnno.py", 'w') as f:f.write(f'def s():return {prim}')
    import wremwnno
    a=wremwnno.s()
    delete_module('wremwnno')
    os.remove('wremwnno.py')
    for i in os.listdir('__pycache__/'):
        if i[0:17] == 'wremwnno.cpython-' and i[-4:-1] == '.pyc':os.remove('__pycache__/'+i)
    try:return float(a)
    except:return a
def random_line(dlin):
    dlin,pov,l=int(dlin),dlin//15,''
    if dlin % 15 != 0:pov+=1
    for p in range(pov):
        while True:
            r=random.random()
            k=spis_in_lin(list(r)[2:17])
            if len(str(k)) == 15:break
        l+=str(k)
    if len(str(l)) > dlin:l=spis_in_lin(lin_in_spis(l)[len(str(l))-dlin:])
    return l
def abc_line(abc,dlin):
    if str(type(abc)) != "<class 'list'>" and str(type(abc)) != "<class 'set'>" and str(type(abc)) != "<class 'tuple'>" or str(type(abc)) != "<class 'dict'>":abc=list(str(abc))
    ab,fil,t,n=[],[],'',0
    for i in range(int(dlin)):ab.append(0)
    while n==0:
        for i in range(int(dlin)):t+=str(abc[ab[i]])
        ab[0]+=1
        for u in range(int(dlin)):
            if ab[u] == len(abc):
                if ab[len(ab)-1] == len(abc):n=1;break
                else:
                    ab[u]=0
                    ab[u+1]+=1
        fil.append(t)
        t=""
    return fil
def delpoz(spis,dels,blok=False):
    t=None
    if str(type(spis)) != "<class 'list'>" and str(type(spis)) != "<class 'tuple'>":t=str(type(spis));spis=list(str(spis))
    if blok:
        try:
          for i,n in enumerate(dels):spis.pop(int(n)-i)
        except:pass
    else:
        for i,n in enumerate(dels):spis.pop(int(n)-i)
    if t != None:spis=settype(spis,t,1)
    return spis
def coding(text,txt=list(""" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890+-*/\\?.<>,[]{}()!№#$;:%^&_~`="'"""),prot=abc_line("01",10)):
    if str(type(prot)) != "<class 'list'>" and str(type(prot)) != "<class 'tuple'>":raise ValueError("Только списки")
    if str(type(txt)) != "<class 'list'>" and str(type(txt)) != "<class 'tuple'>":txt=list(str(txt))
    #if len(prot) > len(txt):raise ValueError("txt >= prot")
    if False:pass
    else:
        cod=""
        if str(type(text)) != "<class 'list'>" and str(type(text)) != "<class 'tuple'>":text=spis_in_lin(text)
        for aa in list(str(text)):
            try:
                ind=txt.index(aa)
                cod+=str(prot[ind])
            except:cod+=str(aa)
        return cod
def encoding(code,txt=list(""" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890+-*/\\?.<>,[]{}()!№#$;:%^&_~`="'"""),prot=abc_line("01",10)):
    if str(type(prot)) != "<class 'list'>" and str(type(prot)) != "<class 'tuple'>":raise ValueError("Только списки")
    if str(type(txt)) != "<class 'list'>" and str(type(txt)) != "<class 'tuple'>":txt=list(str(txt))
    if str(type(prot[0])) == "<class 'int'>":
        prot=[str(i) for i in prot]
    #if len(prot) > len(txt):raise ValueError("txt >= prot")
    if False:pass
    else:
        am,text=[],""
        if str(type(code)) != "<class 'list'>" and str(type(code)) != "<class 'tuple'>":code=lin_in_spis(str(code),prom=len(str(prot[0]))-1,save=1)
        o=len(str(prot[0]))
        for i in range(len(code)):
            text+=str(txt[prot.index(code[0])])
            code.pop(0)
        return text
def dels(*k,**kk):return math_.dels(*k,**kk)
def cel_time(dlin=1):
    m=""
    for i in range(int(dlin)):
        for i in list(str(time.time())):
            if i != ".":m+=str(i)
    return int(m)
def minisim(text,l1=list("ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),l2=list("abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя")):
    for i,n in enumerate(l1):text=text.replace(n,l2[i])
    return text
def yn():
    if random.randrange(0,2) == 0:return False
    else:return True
def give_dict(sett,give,param=[]):
    if type(sett) != "<class 'dict'>":raise ValueError(f"type not {type(sett)}, type dict")
    if type(param) != "<class 'list'>" and type(param) != "<class 'tuple'>":raise ValueError(f"type not {type(param)}, type list")
    try:s=sett[give]
    except:return ""
    else:
        for i in param:s=s[i]
        return s
def radar(p,typ=[],js=[]):
    if len(typ) == 0:
        for i in os.listdir(p+'/'):
            _,g=os.path.splitext(i)
            if g == '':
                try:js=radar(p+'/'+i,js=js)
                except:js.append(p+'/'+i)
            else:js.append(p+'/'+i)
    else:
        for i in os.listdir(p+'/'):
            _,g=os.path.splitext(i)
            if g == '':
                try:js=radar(p+'/'+i,typ,js)
                except:
                    if g in typ:js.append(p+'/'+i)
            else:
                if g in typ:js.append(p+'/'+i)
    return js
def if_not_in(text,d):
    t=''
    for i in text:
        if i in d:t+=i
    return t
#class:
def dec(num):return Decimal(str(num))
class math_:
    def pi():return int('1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540 9171536436 7892590360 0113305305 4882046652 1384146951 9415116094 3305727036 5759591953 0921861173 8193261179 3105118548 0744623799 6274956735 1885752724 8912279381 8301194912 9833673362 4406566430 8602139494 6395224737 1907021798 6094370277 0539217176 2931767523 8467481846 7669405132 0005681271 4526356082 7785771342 7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 6892589235 4201995611 2129021960 8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 1609631859 5024459455 3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 7669147303 5982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 2164201989'.replace(' ',''))
    def easy_drob(d1,d2):
        d1,d2=int(d1),int(d2)
        for i in [2,3,10]:
            if d1%i == 0 and d2%i == 0:
                d1//=i
                d2//=i
                d1,d2=math_.easy_drob(d1,d2)
                break
        return d1,d2
    def sozd_drob(cel,pz,per):return math_.easy_drob(int(str(pz)+str(per))*int(cel),int('9'*len(str(per))+'0'*len(str(pz))))
    def dels_old(a,b,dlin,fl=True):
        if str(type(a)) == "<class 'str'>":a=int(a)
        if str(type(b)) == "<class 'str'>":b=int(b)
        dlin,t,r,per=int(dlin),0,['',''],0
        while a != 0:
            if t == dlin:break
            p=0
            while a < b:
                p+=1
                if a < 0:a*=-10
                else:a*=10
                per=1
            if p > 1:r[per]+='0'*(p-1)
            try:n=int(a/b)
            except:n=int(a//b)
            r[per]+=str(n)
            a=a-b*n
            t+=1
        if len(r[1]) > dlin:r[1]=r[1][:dlin]
        if fl:return f'{r[0]}.{r[1]}'
        return r[0]+r[1]
    def sum(*num):
        return sum(map(Decimal,map(str,num)))
    def min(*num):
        return Decimal('0')-sum(map(Decimal,map(str,num)))
    def dels(a,b,dlin,fl=True):
        if str(type(a)) == "<class 'str'>":a=int(a)
        if str(type(b)) == "<class 'str'>":b=int(b)
        a=dec(a)
        b=dec(b)
        dlin,t,r,per=int(dlin),0,['',''],0
        while a != 0:
            if t == dlin:break
            p=0
            while a < b:
                p+=1
                if a < 0:a*=-10
                else:a*=10
                per=1
            if p > 1:r[per]+='0'*(p-1)
            try:n=int(a/b)
            except:n=int(a//b)
            r[per]+=str(n)
            n=dec(n)
            a=a-b*n
            t+=1
        if len(r[1]) > dlin:r[1]=r[1][:dlin]
        if fl:return f'{r[0]}.{r[1]}'
        return r[0]+r[1]
    def sums(a:str,b:str,fl=False):
        if fl:
            while a[-1] == '0':a=a[:-1]
            while b[-1] == '0':b=b[:-1]
            zn=len(a.split('.')[1])
            zn+=len(b.split('.')[1])-1
            a=a.replace('.','')
            b=b.replace('.','')
        while len(a)>len(b):
            b='0'+b
        while len(a)<len(b):
            a='0'+a
        a,b=a[::-1],b[::-1]
        zap=0
        su=''
        for i in [[n,b[i]] for i,n in enumerate(a)]:
            s=int(i[0])+int(i[1])+zap
            zap=0
            if s > 9:zap,s=1,s-10
            su+=str(s)
        if zap == 1:su+='1'
        su=su[::-1]
        if fl:return su[zn:]+'.'+su[:zn]
        return su
    def mins(a:str,b:str,fl=False):
        if fl:
            while a[-1] == '0':a=a[:-1]
            while b[-1] == '0':b=b[:-1]
            zn=len(a.split('.')[1])
            zn+=len(b.split('.')[1])-1
            a=a.replace('.','')
            b=b.replace('.','')
        while len(a)>len(b):
            b='0'+b
        while len(a)<len(b):
            a='0'+a
        a,b=a[::-1],b[::-1]
        zap=0
        su=''
        for i in [[n,b[i]] for i,n in enumerate(a)]:
            s=int(i[0])-int(i[1])-zap
            zap=0
            if s < 0:zap,s=1,s+10
            su+=str(s)
        su=su[::-1]
        if fl:return su[zn:]+'.'+su[:zn]
        return su
class dicts:
    def sort(d,rev=False):
        di=[d[i] for i in d]
        di.sort()
        if rev:di=list(reversed(di))
        dd={}
        d=dicts.rev(d)
        for i in di:dd[i]=d[i]
        return dd
    def rev(d):
        dd={}
        for i in d:
            if d[i] in dd:dd[d[i]].append(i)
            else:dd[d[i]]=[i]
        return dd


def byte(text,encode='utf-32'):bits=bin(int.from_bytes(str(text).encode(encode,'surrogatepass'),'big'))[2:];return bits.zfill(8*((len(bits)+7)//8))



class hashm:
    def hash(text=time.time(),dlin=10):return int(hashm.hp(text+str(time.time()),param2=dlin),16)
    def h(text,param=39,param2=39,metod=False,encode='utf-32',pov=1):
        param,param2=int(param),int(param2)
        b=byte(text,encode)
        for i in range(int(pov)):b=byte(hex(int(b,2)),encode)
        j=[int(i,2) for i in [b[i*param:param+i*param] for i,n in enumerate(b) if b[i*param:param+i*param] != '']]
        if metod:m=1
        else:m=-1
        while True:
            if len(j) == 1:j=list(str(j[0]))
            p=math_.dels(j[0],[1 if str(j[m]) == '0' else j[m]][0],param2,False)
            if p == '':p=1
            j.pop(m)
            j.pop(0)
            j.append(int(p))
            if len(j) == 1:break
        return hex(j[0])[2:]
    def hp(text,param=75,param2=25,metod=False,encode='utf-32',pov=1):
        param,param2=int(param),int(param2)
        b=byte(text,encode)
        for i in range(int(pov)):b=byte(hex(int(b,2)),encode)
        j=[int(i,2) for i in [b[i*param:param+i*param] for i,n in enumerate(b) if b[i*param:param+i*param] != '']]
        if metod:m=1
        else:m=-1
        while True:
            if len(j) == 1:j=list(str(j[0]))
            q=j[0]
            while True:
                p=math_.dels([2 if str(j[0]) == '0' else j[0]][0],[1 if str(j[m]) == '0' else j[m]][0],param2,False)
                if p == '':continue
                p=str(int(p))
                if len(p) == param2:break
                elif len(p) > param2:
                    p=p[:param2]
                    break
                elif len(p) < param2:
                    while len(p) < param2:p+=p[:param2-len(p)]
                    break
            j.pop(m)
            j.pop(0)
            j.append(int(p))
            if len(j) == 1:break
        return hex(j[0])[2:]
    def hp_old(text,param=75,param2=25,metod=False,encode='utf-32',pov=1):
        param,param2=int(param),int(param2)
        b=byte(text,encode)
        for i in range(int(pov)):b=byte(hex(int(b,2)),encode)
        j=[int(i,2) for i in [b[i*param:param+i*param] for i,n in enumerate(b) if b[i*param:param+i*param] != '']]
        if metod:m=1
        else:m=-1
        while True:
            if len(j) == 1:j=list(str(j[0]))
            q=j[0]
            while True:
                p=math_.dels_old([2 if str(j[0]) == '0' else j[0]][0],[1 if str(j[m]) == '0' else j[m]][0],param2,False)
                if p == '':continue
                p=str(int(p))
                if len(p) == param2:break
                elif len(p) > param2:
                    p=p[:param2]
                    break
                elif len(p) < param2:
                    while len(p) < param2:p+=p[:param2-len(p)]
                    break
            j.pop(m)
            j.pop(0)
            j.append(int(p))
            if len(j) == 1:break
        return [hex(j[0])[2:],hashm.hp(text,param,param2,metod,encode,pov)]
    def hpi(text,dlin=39,encode='utf-32',pov=0):
        dlin=int(dlin)
        b=byte(text,encode)
        for i in range(int(pov)):b=byte(hex(int(b,2)),encode)
        text=int(b,2)
        from decimal import Decimal, getcontext
        getcontext().prec=text
        print(text)
        p=sum(1/Decimal(16)**k*(Decimal(4)/(8*k+1)-Decimal(2)/(8*k+4)-Decimal(1)/(8*k+5)-Decimal(1)/(8*k+6)) for k in range(100))
        return hex(p[text-dlin:text])[2:]
    def hp2(text,param=75,param2=25,metod=False,encode='utf-32',pov=1):
        text=str(text)
        l=0
        ha=''
        for i in range(len(hashm.hp(text=text,param=param,param2=param2,metod=metod,encode=encode,pov=pov))-1):
            h=hashm.hp(text=text,param=param,param2=param2,metod=metod,encode=encode,pov=pov)
            text+=h[i]
            ha+=h[i]
        return ha
class rundom:
    def dels(dlin=5):
        dlin=int(dlin)
        r=""
        for g in range(dlin):
            while True:
                ts=time.time()*2%time.time()
                x=list(str(ts))
                a=int(x[0])
                b=int(x[len(str(ts))-1])
                d=list(math_.dels(a,b,a*b+1,False))
                if len(d) >= a*b+1:f=str(d[a*b]);break
            r+=f
        return int(r)
    def lite(dlin=5):
        dlin=int(dlin)
        if dlin == 1:return rundom.dels(1)
        else:
            r="1"
            for g in range(dlin):r+=str(list(str(cel_time()**dlin))[-1])
            return int(r)%int('1'+'0'*dlin)
    def mini():return int(str(cel_time())[-1])
    def toch(start,stop):
        start=int(start)
        stop=int(stop)
        if start > stop:raise ValueError("start <= stop")
        elif start == stop:return stop
        else:
            rr=len(str(stop))-len(str(start))
            while True:
                r=rundom.lite()
                if int(r) < stop and int(r) >= start:break
            return int(r)
    def dels_2(dlin=5):
        dlin=int(dlin)
        r="1"
        for g in range(dlin):
            while True:
                ts=time.time()*2%time.time()
                ts=[int(i) for i in str(ts) if i !='.']
                a=int(r[-1])*int(r[0])+ts[-1]*ts[0]
                b=len(ts)+len(str(a))
                d=list(math_.dels(a,b,a+b+1,False))
                if len(d) >= a+b+1:f=str(d[a+b-int(r[-1])]);break
            r+=f
        return int(r[1:])
class inet:
    def output(text,ip='127.0.0.1',port=3542):
        socket.socket(socket.AF_INET,socket.SOCK_DGRAM).sendto(str(text).encode(), (ip,port))
    def input(ip='',port=3542,ip_get=False,lin=9999):
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind((ip,port))
        inp,addr = s.recvfrom(lin)
        s.close()
        if inp != "":
            if ip_get:return addr,inp.decode()
            return inp.decode()
