import sys,threading  
sys.setrecursionlimit(3000000)  
threading.stack_size(67108864)  
  
def firstdfs(vertexind):  
    global fs,isexplored,visitordered,mapDictT  
    if len(mapDictT[vertexind])>0:  
        for ind in mapDictT[vertexind]:  
            if not isexplored[ind-1]:  
                isexplored[ind-1]=True  
                firstdfs(ind)  
    visitordered[fs-1]=vertexind  
    #print(str(vertexind)+' fs: '+str(fs))  
    fs=fs-1  
  
def seconddfs(vertexind):  
    global s,secisexplored,header,mapDict  
    if len(mapDict[vertexind])==0:return  
    for ind in mapDict[vertexind]:  
        if not secisexplored[ind-1]:  
            secisexplored[ind-1]=True  
            seconddfs(ind)  
    header[s-1]+=1  
  
def sccmain():  
    global mapDict,mapDictT,fs,isexplored,visitordered,s,secisexplored,header  
    maplength=875714  
    #maplength=11  
    f=open('SCC.txt','r')  
    mapDict={x:[] for x in range(1,maplength+1)}  
    mapDictT={x:[] for x in range(1,maplength+1)}  
    for line in f.readlines():  
        tmp=[int(x) for x in line.split()]  
        mapDict[tmp[0]].append(tmp[1])  
        mapDictT[tmp[1]].append(tmp[0])  
    f.close  
  
    fs=maplength  
    isexplored=[False for x in range(1,maplength+1)]  
    secisexplored=[False for x in range(1,maplength+1)]  
    visitordered=[0 for x in range(1,maplength+1)]  
    header=[0 for x in range(1,maplength+1)]  
  
    for ind in range(1,maplength+1):  
        if not isexplored[ind-1]:  
            #print('Begin from: '+str(ind))  
            isexplored[ind-1]=True  
            firstdfs(ind)  
    print('Second DFS')  
    for ind in visitordered:  
        if not secisexplored[ind-1]:  
            s=ind  
            secisexplored[ind-1]=True  
            seconddfs(ind)  
  
    header.sort(reverse=True)  
    print(header[0:20])  
  
if __name__ =='__main__':  
    thread=threading.Thread(target=sccmain)  
    thread.start() 
