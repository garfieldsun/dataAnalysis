flag=0
datalist=[]
name=1
with open('D:/huashuData/huashu2018/fifth_rec.csv',encoding='utf-8') as f:
    for line in f:
        flag+=1
        datalist.append(line)
        if flag==2000000:
            with open('D:/huashuData/huashu2018/data'+str(name)+'.csv','w+') as wf:
                for data in datalist:
                    wf.write(data)
            name+=1
            flag=0
            datalist=[]

with open('D:/huashuData/huashu2018/data'+str(name)+'.csv','w+') as wf:
    for data in datalist:
        wf.write(data)
