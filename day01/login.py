name=input('please input your name:')
print('welcome to here '+name)
print('huan ying ni ',name)
# >>> n = input('number:')
# number:10
# >>> 10+2
# 12
# >>> n+2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: must be str, not int
# >>> int(n)
# 10
# >>> int(n)+2
# 12
# >>> n+str(2)
# '102'
# >>>
# 5/3
# 5//3
# 5%3
# divmod(5,3)
# round(5/3,2)
# 2**6
# 2*3**2
# (2*3)*2
# 10<20>15
# 10<20<30
# 10<20 and 20<30
# not 10>3
# >>> not 10>5 and 20 > 10
# False
# >>> not (10>5 and 20 > 10 )
# False
# >>> not (10<5 and 20 > 10 )
# True
# >>> not 10<5 and 20 > 10
# True
# >>> not 10 < 5 and 20 > 10
# True
# >>> not (10 < 5 and 20 > 10)
# True
# 2==2
# >>> True + 2
# 3
# >>> False + 2
# 2
# >>> False * 2
# 0
# >>> False / 2
# 0.0
# >>> False // 2
# 0
# >>> True // 2
# 0
# >>> True // 1
# 1
# >>>
# >>> 2*60*60+3*60+5
# 7385
# >>> 6*16*16+0*60+5
# 1541
# >>> 0x605
# 1541
# >>> 1*8*8*8+5*8*8+4*8+1
# 865
# >>> 0o1541
# 865
# >>> div(100,16)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'div' is not defined
# >>> divmod(100,16)
# (6, 4)
# >>>
# >>>
# >>>
# >>>
# >>>
# >>> div(100,8)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'div' is not defined
# >>> divmod(100,8)
# (12, 4)
# >>> divmod(12,8)
# (1, 4)
# >>> 0o144
# 100
# >>> name = "tom"
# >>> print("hi",name)
# hi tom
# >>> uname = "tom"
# >>> myname = "jerry"
# >>> "hi,%s. i am %s" %(uname,myname)
# 'hi,tom. i am jerry'
# >>>
# >>> "naem"
# 'naem'
# >>> "name"
# 'name'
# >>> "%s"%(uname)
# 'tom'
# >>> "woshi %s"%uname
# 'woshi tom'
# >>> "woshi %s ,nishi %s"%(uname,myname)
# 'woshi tom ,nishi jerry'
# >>>
#>>> words = """hello
# ... ni hao
# ... abc
# ... abd"""
# >>> words
# 'hello\nni hao\nabc\nabd'
# >>> w = "hello\nnihao\ngreet"
# >>> print(w)
# hello
# nihao
# greet
# >>> print(words)
# hello
# ni hao
# abc
# abd
# >>> py_str = "python"
# >>> len(py_str)
# 6
# >>> py_str[0]
# 'p'
# >>> py_str[5]
# 'n'
# >>> py_str[-1]
# 'n'
# >>> py_str[-6]
# 'p'
# >>> py_str[2]
# 't'
# >>>
# >>> print()
# >>> py_str
# 'python'
# >>> py_str[2:3]
# 't'
# >>> py_str[2:4]
# 'th'
# >>> py_str[2:5]
# 'tho'
# >>> py_str[2:6]
# 'thon'
# >>> py_str[0:1]
# 'p'
# >>> py_str[2:6]
# 'thon'
# >>> py_str[2:7]
# 'thon'
# >>>
#
# >>> py_str[6]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
# >>>
# >>> py_str
# 'python'
# >>> py_str[0:3]
# 'pyt'
# >>> py_str[0:2]
# 'py'
# >>> py_str[:2]
# 'py'
# >>> py_str[4:]
# 'on'
# >>> py_str[2:]
# 'thon'
# >>>
# >>> py_str[:]
# 'python'
# >>> py_str[::1]
# 'python'
# >>> py_str[::2]
# 'pto'
# >>> py_str[::3]
# 'ph'
# >>> py_str[::4]
# 'po'
# >>> py_str[::5]
# 'pn'
# >>> py_str[1::5]
# 'y'
# >>> py_str[1::2]
# 'yhn'
# >>> py_str[::-1]
# 'nohtyp'
# >>>

# >>> '* ' * 30
# '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * '
# >>> '#' * 30
# '##############################'
# >>> 'ab' * 30
# 'abababababababababababababababababababababababababababababab'
# >>>
# >>> py_str = "python"
# >>> "t" in py_str
# True
# >>> "th" not in  py_str
# False
# >>> "th" ~ py_str
#   File "<stdin>", line 1
#     "th" ~ py_str
#          ^
# SyntaxError: invalid syntax
# >>> "th" in py_str
# True
# >>> "oy" in py_str
# False
# >>> "o" in py_str
# True
# >>> alist[2]
# 30
# >>> alist[3:]
# [40, 'tom', 'jerry']
# >>> alist[2:]
# [30, 40, 'tom', 'jerry']
# >>> 30 in alist
# True
# >>> alist + [50]
# [10, 20, 30, 40, 'tom', 'jerry', 50]
# >>>
# >>> alist.
# alist.append(   alist.copy(     alist.extend(   alist.insert(   alist.remove(   alist.sort(
# alist.clear(    alist.count(    alist.index(    alist.pop(      alist.reverse(
# >>> alist.append(40)
# >>> alist
# [10, 20, 30, 40, 'tom', 'jerry', 40]
# >>> alist[-1] = 400
# >>> alist
# [10, 20, 30, 40, 'tom', 'jerry', 400]
# >>>
# >>> alist
# [10, 20, 30, 40, 'tom', 'jerry', 400]
# >>> atup=(10,20,30,40,'tom','jdrry')
# >>> len(atup)
# 6
# >>> atup[0]
# 10
# >>> atup[-1]
# 'jdrry'
# >>> atup[-1] bob
#   File "<stdin>", line 1
#     atup[-1] bob
#                ^
# SyntaxError: invalid syntax
# >>> atup[-1]= 'bob'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>> adict = {'name':'tom','age':'20'}
# >>> len(adict)
# 2
# >>> 'tom' in adict
# False
# >>> 'name '  in adict
# False
# >>> 'name'  in adict
# True
# >>> adict['name']
# 'tom'
# >>> adict['age']
# '20'
# >>> adict
# {'name': 'tom', 'age': '20'}
# >>>
# 20>>> adict['email']='tome@tedu.cn'
# >>> adict
# {'name': 'tom', 'age': '20', 'email': 'tome@tedu.cn'}
# >>> adict['name']
# 'tom'
# >>> adict['name'] = 'bob'
# >>> adict
# {'name': 'bob', 'age': '20', 'email': 'tome@tedu.cn'}
# >>>

