# 作者:ふぇぎ
# 掲示板のインデックスが消えていたのを直すために作成した
# python3で書かれている
# 1.このプログラムを任意のディレクトリにコピーし、同ディレクトリにpforumの最新のlogディレクトリをコピーする
# 2.このプログラムを起動する
# 3.生成されたファイルをpforumにコピーする

import glob 
import re
def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

fitsf=sorted(glob.glob('log/*.php'), key=numericalSort,reverse=True)

ifile = open('pforumidx.php','w')
ifile.write('<?php\n')

for fname in fitsf:
    print(fname)
    file = open(fname,'r')
    logList = file.readlines()
    
    firstComment = logList[1]
    lastComment = logList[-1]

    first = firstComment.split('<>')
    last = lastComment.split('<>')

    filename = first[0]
    subject = first[7]
    firstname = first[3]
    lastname = last[3]
    mdate = first[12]
    ldate = last[12]
    solved = first[14]
    deleted = first[15]
    resnum = len(logList)-2
    viewnum = 0
    ipaddress = first[-2]

    ilog = '{0}<>{1}<>{2}<>{3}<>{4}<>{5}<>{6}<>{7}<>{8}<>{9}<>{10}<>\n'.format(filename,subject,firstname,lastname,mdate,ldate,solved,deleted,resnum,viewnum,ipaddress)

    print(ilog)
    ifile.write(ilog)
    
    
    file.close()

ifile.close()
