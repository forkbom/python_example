def show(content):
    #定义列表,用于存储数据
    for i in range(len(content)):
        print('%s:%s' % (i, content[i]))

# alist=[]
#
# while True:
#     data = input('(end to quit)>')
#     if data == 'end':
#         break
#     content.append(data)
    # 将列表中的内容加上行号

fobj = open('/tmp/main.cf')
alist = fobj.readlines()
fobj.close()
show(alist)