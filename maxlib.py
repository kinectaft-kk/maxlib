#
#info:
'''
Python: 3.12.3
'''
#imports:
import os
import sys
import random
from socket import socket,AF_INET,SOCK_DGRAM
from sys import modules
import time
#import hashlib
#instruction:
version=1.0
creater="Kinecraft_kk"
lis_of_w=['print','input','if','len','.append()']
bibl=['os','sys','random','from socket: socket,AF_INET,SOCK_DGRAM','time','hashlib']
command=["help(0/1)","lin_in_spis(1/2)","spis_in_lin(1/2)","searsh_sim(2)","conculator(1)","random_line(0/1)","del_sim(2)","inet.messanger.out(1/2/3)","inet.messanger.inp(0/1/2)","test.pc1(0/1/2)","test.pc2(0/1/2)"]
commands='help("Комманда") : Даёт пояснение к коммандам питона \nhelp("list of words") : Показывает список доступных слов для объяснения \nlin_in_spis("Строка") : Переводит каждый символ в отдельную ячейку в списке \nlin_in_spis("Строка","Отделяющий символ") : Переводит каждый блок отделённый вводимым символом в отдельную ячейку в списке \nconculator("Пример") : Введите любой ПРИМЕР и выдаст ответ \nspis_in_lin([Список]) : Складывает каждую ячейку списка в строку \nspis_in_lin([Список],"Соединяющий символ") : Складывает каждую ячейку списка в строку с раздилением введёного символа \nrandom_line(Длинна рандомного целога числа) : Генерирует случайное целое число необходимой длины \nsearsh_sim("Любой тип данных","Искомый символ") : Нужен для подстчёта символа в строкебспискеби тп. \ndel_sim("Любой тип данных","Символ") : Нужен для удаления символов со строки, списка, и тп \nclass inet(): Только с интеретом! \n    class messanger(): \n       out("Текст сообщения","Айпи","Порт(Не обязательно)") : Нужен для приёмки сообщения \n       inp("Айпи(Не обязательно)","Порт(Не обязательно)") : Нужен для отправки сообщения \nclass test(): \n    pc1(Примерное время теста(Не обязательно),Шаг(Не обязательно)) : Нужен для теста скорости системы    <--- Менее точный \n    pc2(Время теста(Не обязательно),Шаг(Не обязательно)) : Нужен для теста скорости системы   <--- Более точный'
    
#help cods:
sys.set_int_max_str_digits(0)
class sistem():
    def read(nom=""):
        t=[]
        f=""
        for i in [f for i,f in enumerate(open("Text_in_func.py").readline())][1:-1]:
            if i == ";":
                t.append(f)
                f=""
            else:f+=str(i)
        if nom == "":return t
        else:return t[int(nom)]
    def zap(text,nom="new"):
        f=open("Text_in_func.py")
        g=[i.rstrip() for i in f]
        f.close()
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
        f=open("Text_in_func.py", 'w')
        f.write(gg)
        f.close()
    def delete_module(modname, paranoid=None):
        try:thismod = modules[modname]
        except KeyError:raise ValueError(modname)
        these_symbols = dir(thismod)
        if paranoid:
            try:paranoid[:]  
            except:raise ValueError('must supply a finite list for paranoid')
            else:these_symbols = paranoid[:]
        del modules[modname]
        for mod in modules.values():
            try:delattr(mod, modname)
            except AttributeError:pass
            if paranoid:
                for symbol in these_symbols:
                    if symbol[:2] == '__':  continue
                    try:delattr(mod, symbol)
                    except AttributeError:pass
#cods:
def spis_in_lin(spis,typ=""):
    b=""
    if typ == "":
        for u in spis:
            b+=str(u)
    else:
        for u in spis:
            b+=str(u)+str(typ)
    return b
def help(h="commands"):
    if h == "commands":t=commands
    elif h == 'creater' or h == 'cr' or h == 'c':
        t=creater
    elif h == 'version' or h == 'ver' or h == 'v':
        t=version
    elif h == "import" or h == "imports" or h == "bibl":
        t=bibl
    elif h == "info":
        t=f"Creater:{creater},version:{version},imports:{bibl}."
    elif h == "list of words":
        t=lis_of_w
    elif h == "all_librory":
        t=spis_in_lin(modules,"\n")
    elif h == "print" or "print()":
        t="print() Нужен для вывода текста"
    elif h == "input" or "input()":
        t="input() Нужен для ввода текста"
    elif h == "if" or h == "if():" or h == "if()" or h == "if:":
        t="if: Нужен для проверки значения"
    elif h == "len" or h == "len()":
        t="len Нужен для измерения длины строки, списка,и тп"
    elif h == ".append()" or h == "append()" or h == ".append" or h == "append":
        t=".append() Нужен для добавления строки в список"
    return t


'''
def super_hash(text):
    s=[]
    for i,e in enumerate(text):
        p.append(e)
'''

def lin_in_spis(lin,typ=""):
    spis=[]
    if str(type(typ)) == "<class 'int'>":
        nom=0
        h=""
        for i,u in enumerate(str(lin)):
            if nom == typ:
                spis.append(h)
                nom=0
                h=""
            else:
                nom+=1
                h+=str(u)
        h+=str(u)
        spis.append(h)
    else:
        typ=str(typ)
        if typ == "":
            for i,u in enumerate(str(lin)):
                spis.append(u)
        else:
            h=""
            for i,u in enumerate(str(lin)):
                if u == typ:
                    spis.append(h)
                    h=""
                else:h+=str(u)
            spis.append(h)
    return spis
def searsh_sim(lin,sim,v=1):
    if str(type(lin)) == "<class 'tuple'>" or str(type(lin)) == "<class 'list'>" or str(type(lin)) == "<class 'set'>" :lin=spis_in_lin(lin)
    lin=lin_in_spis(lin)
    if v == 1:
        m=0
        for n in str(lin):
            if n == str(sim):m+=1
        return m
    elif v == 2:
        m=[]
        for i,n in enumerate(str(lin)):
            if n == str(sim):
                m.append(str(i))
        return m
        
def del_sim(lin,sim):
    b=""
    types=str(type(lin))
    if types == "<class 'tuple'>" or types == "<class 'list'>" or types == "<class 'set'>":
        h=[]
        for u in lin:
            typi=str(type(u))
            u=lin_in_spis(u)
            for i in u:
                if i != sim:
                    b+=str(i)
            if typi == "<class 'int'>":b=int(b)
            elif typi == "<class 'float'>":b=float(b)
            h.append(b)
            b=""
        if types == "<class 'tuple'>":h=tuple(h)
        elif types == "<class 'set'>":h=set(h)
        return h
    else:
        lin=lin_in_spis(lin)
        for u in lin:
            if u != sim:
                b+=str(u)
        if types == "<class 'int'>":b=int(b)
        elif types == "<class 'float'>":b=float(b)
        return b
    
def conculator(prim):
    n=open("Kinecraft_kk.py", 'w')
    n.write(f'def s():return ({str(prim)})')
    n.close()
    import Kinecraft_kk
    a=Kinecraft_kk.s()
    sistem.delete_module('Kinecraft_kk')
    os.remove('Kinecraft_kk.py')
    os.remove('__pycache__\\Kinecraft_kk.cpython-312.pyc')
    return a

def random_line(dlin=10):
    dlin=int(dlin)
    pov=dlin//15
    if dlin % 15 != 0:
        pov+=1
    l=""
    for p in range(pov):
        while True:
            r=random.random() 
            k=spis_in_lin(lin_in_spis(r)[2:17])
            if len(str(k)) == 15:
                break
        l+=str(k)


    if len(str(l)) > dlin:l=spis_in_lin(lin_in_spis(l)[len(str(l))-dlin:])
    return l

        
def abc_line(d,abc="abcdefghijklmnopqrstuvwxyz"):
    if str(type(abc)) == "<class 'str'>" or str(type(abc)) == "<class 'int'>" or str(type(abc)) == "<class 'float'>":
        abc=lin_in_spis(str(abc))
    tim=time.time()
    ab=[]
    fil=[]
    for i in range(d):
        ab.append(0)
    t=""
    n=0
    while n==0:
        for i in range(d):t+=str(abc[ab[i]])
        ab[0]+=1
        for u in range(d):
            if ab[u] == len(abc):
                if ab[len(ab)-1] == len(abc):n=1
                else:
                    ab[u]=0
                    ab[u+1]+=1

        fil.append(t)
        t=""
    return fil
def coding(text,txt=lin_in_spis(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890+-*/?\|.<>,[]{}()!@#№$;:%^&_~`="),prot=abc_line(10,"01")):
    cod=""
    for aa in list(str(text)):
        for i,s in enumerate(txt):
            if aa == s:
                cod+=str(prot[i])
                break
    return cod
        
        
def encoding(code,txt=lin_in_spis(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890+-*/?\|.<>,[]{}()!@#№$;:%^&_~`="),prot=abc_line(10,"01")):
    d=""
    am=[]
    for i,s in enumerate(str(code)):
        d+=str(s)
        if len(d) == 10:
            am.append(d)
            d=""
    text=""
    for aa in am:
        for i,s in enumerate(prot):
            if aa == s:
                text+=str(txt[i])
                break
    return text

#class:
class seting():
    pass
class test():

    def pc1(max_time=10,types=1):
        tin=time.time()
        tim=time.time()
        o=[]
        while time.time()-tim <= max_time:
            types*=10
            tim=time.time()
            random_line(types)
            if time.time()-tim != 0:o.append(str(types/1000000)+" million символов за "+str(time.time()-tim)+" Sec")
        return spis_in_lin(o,"\n")+"Время теста: "+str(time.time()-tin)+" Sec"
    def pc2(times=10,types=1):
        tim=time.time()
        n=0
        while time.time()-tim <= times:
            random_line(types)
            n+=types
        return str(n)+" символов за "+str(times)+" sec"
    def pc3(max_time=10,d=5):
        abc=lin_in_spis("abcdefghijklmnopqrstuvwxyz")
        tim=time.time()
        ab=[]
        fil=[]
        for i in range(d):
            ab.append(0)
        t=""
        n=0
        while n==0 and time.time()-tim < max_time:
            for i in range(d):t+=abc[ab[i]]
            ab[0]+=1
            for u in range(d):
                if ab[u] == 26:
                    if ab[len(ab)-1] == 26:n=1
                    else:
                        ab[u]=0
                        ab[u+1]+=1

            fil.append(f'{t}\n')
            t=""

        return len(fil)
class inet():
    class messanger():
        def out(text,ip='127.0.0.1',port=2010):
            try:
                uCliSock = socket(AF_INET,SOCK_DGRAM)
                uCliSock.sendto(text.encode(), (ip,port))
                return "Nise"
            except:return "Err"
        def inp(ip="",port=2010):
            try:
                uServSock = socket(AF_INET,SOCK_DGRAM)
                uServSock.bind((ip,port))
                inp,addr = uServSock.recvfrom(9999)
                uServSock.close()
                if inp != "":return inp.decode()
            except:return "Err"

    
class job():
    pass


#The end

os.remove('__pycache__\\maxlib.cpython-312.pyc')


'''
class hasi():
    def sup_hash(text):
        return text
'''
