#imports:
import os
import sys
import random
#instruction:
version=1.0
creater="Kinecraft_kk"
lis_of_w=['print','input','if','len']
bibl=['os','sys','random']

#help cods:
sys.set_int_max_str_digits(0)
def delete_module(modname, paranoid=None):
    from sys import modules
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

def help(h="command"):

    if h == "command":
        t='Команды: 1)help("непонятное слово") Даёт пояснение к слову. 2)help("list of words") Показывает список доступных слов для объяснения. 3) 1) lin_in_spis("Строка") Переводит каждый символ в отдельную ячейку в списке. 2) lin_in_spis("Строка","Отделяющий символ") Переводит каждый блок отделённый вводимым символом в отдельную ячейку в списке. 4)conculator("Пример") Введите любой ПРИМЕР и выдаст ответ. 5) 1) spis_in_lin("Список") Складывает каждую ячейку списка в строку 2) spis_in_lin("Список", "Соединяющий символ") Складывает каждую ячейку списка в строку с раздилением введёного символа 6) random(Длинна рандомного целога числа) Генерирует случайное целое число необходимой длины.'
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
    elif h == "print" or "print()":
        t="print() Нужен для вывода текста"
    elif h == "input" or "input()":
        t="input() Нужен для ввода текста"
    elif h == "if" or h == "if():" or h == "if()" or h == "if:":
        t="if: Нужен для проверки значения"
    elif h == "len" or h == "len()":
        t="len Нужен для измерения длины строки, списка,и тп"
    return t


'''
def super_hash(text):
    s=[]
    for i,e in enumerate(text):
        p.append(e)
'''

def lin_in_spis(lin,typ=""):
    spis=[]
    typ=str(typ)
    if typ == "":
        for i,u in enumerate(str(lin)):spis.append(u)  
    else:
        h=""
        for i,u in enumerate(str(lin)):
            if u == typ:
                spis.append(h)
                h=""
            else:h+=str(u)
        spis.append(h)
    return spis
def spis_in_lin(spis,typ=""):
    b=""
    if typ == "":
        for u in spis:
            b+=str(u)
    else:
        for u in spis:
            b+=str(u)+str(typ)
    return b
        
def conculator(prim):
    n=open("Kinecraft_kk.py", 'w')
    n.write(f'def s():return ({str(prim)})')
    n.close()
    import Kinecraft_kk
    a=Kinecraft_kk.s()
    delete_module('Kinecraft_kk')
    os.remove('Kinecraft_kk.py')
    os.remove('__pycache__\\Kinecraft_kk.cpython-312.pyc')
    return a

def randoms(dlin=10):
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





#The end

os.remove('__pycache__\\maxlib.cpython-312.pyc')


'''
class hasi():
    def sup_hash(text):
        return text
'''
