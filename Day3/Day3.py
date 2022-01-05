Python 3.7.8rc1 (tags/v3.7.8rc1:5f3933d61d, Jun 17 2020, 16:59:29) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:/Users/seungjae/Desktop/Strike/Day1_12865.py ===========
4 7
6 13
4 8
3 6
5 12
>>> 
============ RESTART: C:/Users/seungjae/Desktop/Strike/Day1_12865.py ===========
4 7
6 13
4 8
3 6
5 12
[0]
[0, 3]
[0, 3, 6]
[0, 3, 6, 9]
>>> 
============ RESTART: C:/Users/seungjae/Desktop/Strike/Day1_12865.py ===========
4 7
6 13
4 8
3 6
5 12
[13]
[13, 12]
Traceback (most recent call last):
  File "C:/Users/seungjae/Desktop/Strike/Day1_12865.py", line 41, in <module>
    check(stack,weight,value,idx,wsum,vsum)
  File "C:/Users/seungjae/Desktop/Strike/Day1_12865.py", line 11, in check
    answer.append(value[sumcheck])
IndexError: list index out of range
>>> 
============ RESTART: C:/Users/seungjae/Desktop/Strike/Day1_12865.py ===========
4
Traceback (most recent call last):
  File "C:/Users/seungjae/Desktop/Strike/Day1_12865.py", line 15, in <module>
    N,K = map(int,input().split()) #입력값을 공백단위로 분리후 N,K에 map
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
============ RESTART: C:/Users/seungjae/Desktop/Strike/Day1_12865.py ===========
4 7
6 13
4 8
3 6
5 12
[13]
[13, 27]
[13, 27, 41]
[13, 27, 41, 53]
>>> 
============ RESTART: C:/Users/seungjae/Desktop/Strike/Day1_12865.py ===========
4 7
6 13
4 8
3 6
5 12
[13]
[13, 13, 21, 27]
[13, 13, 21, 27, 13, 21, 27, 33, 41]
[13, 13, 21, 27, 13, 21, 27, 33, 41, 13, 21, 27, 33, 41, 53]
>>> 
============ RESTART: C:/Users/seungjae/Desktop/Strike/Day1_12865.py ===========
4 7
6 13
4 8
3 6
5 12
[13]
[13, 27]
[13, 27, 41]
[13, 27, 41, 53]
[13, 14, 14, 12]
>>> 
============ RESTART: C:/Users/seungjae/Desktop/Strike/Day1_12865.py ===========
4 7
6 13
4 8
3 6
5 12
[13, 14, 14, 12]
14
>>> 
============ RESTART: C:/Users/seungjae/Desktop/Strike/Day1_12865.py ===========
4 7
6 13
4 8
3 
Traceback (most recent call last):
  File "C:/Users/seungjae/Desktop/Strike/Day1_12865.py", line 7, in <module>
    w,v = map(int,input().split())
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
============ RESTART: C:/Users/seungjae/Desktop/Strike/Day1_12865.py ===========
4 7
6 13
4 8
3 6
 5 12
14
>>> a = 'a'
>>> for i in range(26):
	print(a+i)

	
Traceback (most recent call last):
  File "<pyshell#3>", line 2, in <module>
    print(a+i)
TypeError: can only concatenate str (not "int") to str
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
Traceback (most recent call last):
  File "C:/Users/seungjae/Desktop/Strike/Day2.py", line 1, in <module>
    from collection import itertools
ModuleNotFoundError: No module named 'collection'
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
Traceback (most recent call last):
  File "C:/Users/seungjae/Desktop/Strike/Day2.py", line 1, in <module>
    from collections import itertools
ImportError: cannot import name 'itertools' from 'collections' (C:\Users\seungjae\AppData\Local\Programs\Python\Python37\lib\collections\__init__.py)
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
Traceback (most recent call last):
  File "C:/Users/seungjae/Desktop/Strike/Day2.py", line 1, in <module>
    from collections import itertool
ImportError: cannot import name 'itertool' from 'collections' (C:\Users\seungjae\AppData\Local\Programs\Python\Python37\lib\collections\__init__.py)
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
Traceback (most recent call last):
  File "C:/Users/seungjae/Desktop/Strike/Day2.py", line 1, in <module>
    print(itertools.permutation('1',2))
NameError: name 'itertools' is not defined
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
Traceback (most recent call last):
  File "C:/Users/seungjae/Desktop/Strike/Day2.py", line 2, in <module>
    print(itertools.permutation('1',2))
AttributeError: module 'itertools' has no attribute 'permutation'
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
<itertools.permutations object at 0x000001C8B094CF48>
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
<itertools.permutations object at 0x000002808B28CF48>
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
[('1', '2'), ('2', '1')]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
cc
650
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dcdd
18720
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dd
90
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
cccc
358800
>>> 26*25*24*23
358800
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dddd
5040
>>> 10*9*8*7
5040
>>> 10*26*10*9
23400
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dcdd
[0, 0, 0, 0]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dcdd
[0, 0, 0, 1]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dcdd
23400
[0, 0, 0, 1]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
cc
650
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dd
90
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
c
26
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
d
10
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dddd
5040
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
cccc
358800
>>> 26*25*24*23
358800
>>> 10*9*8*7
5040
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
cdcd
67600
>>> 26*10*26*10
67600
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
d
10
[0]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dcd
2600
[0, 0, 0]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
c
26
[0]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
d
10
[0]
>>> 

=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
>>> 
cc
650
[0, 1]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dd
90
[0, 1]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
cd
260
[0, 0]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============

=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dc
260
[0, 0]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
ccd
6500
[0, 1, 0]
>>> 26*25*10
6500
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
cdc
6760
[0, 0, 0]
>>> 26*10*26
6760
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dcc
6500
[0, 0, 1]
>>> 10*26*25
6500
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
ddc
2340
[0, 1, 0]
>>> 10*9*26
2340
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dcd
2600
[0, 0, 0]
>>> 10*26*10
2600
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
cccd
156000
[0, 1, 2, 0]
>>> 26*25*24*10
156000
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
ccdc
169000
[0, 1, 0, 0]
>>> 26*25*10*26
169000
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
cdcc
169000
[0, 0, 0, 1]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dccc
156000
[0, 0, 1, 2]
>>> 10*26*25*24
156000
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
ddcc
58500
[0, 1, 0, 1]
>>> 10*9*26*25
58500
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dddc
18720
[0, 1, 2, 0]
>>> 10*9*8*26
18720
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dcdd
23400
[0, 0, 0, 1]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
ddcd
23400
[0, 1, 0, 0]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dddd
5040
[0, 1, 2, 3]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
cccc
358800
[0, 1, 2, 3]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
cdcc
169000
[0, 0, 0, 1]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
cdcc
169000
[0, 0, 0, 1]
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dcdd
9
>>> 
=============== RESTART: C:/Users/seungjae/Desktop/Strike/Day2.py ==============
dcdd
23400
>>> 
=== RESTART: C:/Users/seungjae/AppData/Local/Programs/Python/Python37/Day3.py ==
