import os

cmd='ls'

fp = os.popen(cmd)
#print(fp)

res = fp.read()
f=open('res.docx','w+')
f.write('[')
for i in res:
    f.write(f"'{res}',")
    print(i)
f.close()
#print(res)
