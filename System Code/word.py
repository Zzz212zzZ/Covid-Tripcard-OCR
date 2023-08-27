import re
f=open('处理.TXT',encoding='utf-8')
txt=[]
for line in f:
    txt.append(line.strip())
print(txt)
i=0
while(i<len(txt)):
    if(txt[i].find('（'))!=-1:
        print("删除",txt[i])
        txt.remove(txt[i])
        continue
    if(txt[i].find('('))!=-1:
        print("删除",txt[i])
        txt.remove(txt[i])
        continue

    pattern=re.compile(r'[0-9A-Za-z]')
    index=txt[i].find('.jpg')
    if(index==-1):
        index = txt[i].find('.png')
    # print(index)
    match=pattern.search(txt[i],index+4)

    if(not match):
        i = i + 1
        continue;

    print("删除",txt[i])
    txt.remove(txt[i])
    continue


# for i in range(len(txt)):
#     pat=r'\d+'
#     result=re.findall(pat,txt[i])
#     print(len(result))


# print(txt)
f=open('第一个文件处理后.txt','w',encoding='utf-8')
for line in txt:
    f.write(line+'\n')
f.close()