# filereadng.py
import random
import string

RNDSTRNUM = 1000

def OpenTextList(filename):
  f = open(filename)
  lns = f.readlines()
  f.close()
  return lns

def getrandstr(strline):
  cnt = 0
  rval = 'LINE'
  for s in strline:
    if random.randint(0, cnt) == 0:
      rval = s.replace('\n','')
    cnt += 1
  return rval

def buildrandstr(cnt = 32):
  lakira = OpenTextList('a1.txt')
  lwho   = OpenTextList('a2.txt')
  lplace = OpenTextList('a3.txt')
  ldo    = OpenTextList('a4.txt')
  lobj   = OpenTextList('a5.txt')
  lfure  = OpenTextList('a6.txt')
  lMeta  = OpenTextList('aMeta.txt')
  lst = []
  #proguresubaa
  prog = 0
  prog = cnt // 20
  if prog <= 0:
    prog = 1
  for i in range(cnt):
    akira = getrandstr(lakira)
    who   = getrandstr(lwho)
    place = getrandstr(lplace)
    do    = getrandstr(ldo)
    obj1  = getrandstr(lobj)
    obj2  = getrandstr(lobj)
    obj3  = getrandstr(lobj)
    fure  = getrandstr(lfure)
    strMeta = getrandstr(lMeta)
    m = strMeta
    m = m.replace("%f",fure)
    m = m.replace("%w",who)
    m = m.replace("%a",akira)
    m = m.replace("%n",do)
    m = m.replace("%d",place)
    m = m.replace("%1",obj)
    m = m.replace("%2",obj)
    m = m.replace("%3",obj)
    lst.append(m)
    if i % prog == 0:
      print('*',end='')
    # print(m)
  with open('aloh.txt', mode='w') as f:
    f.write('\n'.join(lst))
#   f.writelines(lst)

#f a d n o
#for i in range(10):
#  print(ss, end='')

buildrandstr(RNDSTRNUM)
