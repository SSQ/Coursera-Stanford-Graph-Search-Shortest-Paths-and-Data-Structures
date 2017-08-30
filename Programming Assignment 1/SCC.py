import time
import datetime
import sys


start = time.time()
print datetime.datetime.now()

with open('test.txt') as f:
    #SCC
    #a = [[int(x) for x in ln.split()] for ln in f]
    data_set_u = []
    data_set_v = []
    for ln in f:
        #print ln
        #print type(ln)
        #print len(ln)
        if len(ln) >1:
            u,v = ln.split()
            u = int(u)
            v = int(v)            
            data_set_u.append(u)
            data_set_v.append(v)
f.close()

print 'open file time: '+ str(time.time() - start) + 's'
print datetime.datetime.now()
    
sys.setrecursionlimit((max(data_set_u+data_set_v)+ len(data_set_u))*100)

def DFS_Loop():
    num = max(data_set_u+data_set_v)
    
    start_time_DFS_Loop = time.time()
    global t
    t = 0
    global s
    s = None
    global visited
    visited = [False]* num
    global leader
    leader = [None] * num
    global f
    f = [None] * num
    
    
    for i in range(num,0,-1):
        #print i
        #print (i in visited)
        #if (i in visited)==False:
        if visited[i-1] == False:
            s = i
            #print s
            DFS(i)
    print 'end with func DFS_Loop() time: '+ str(time.time() - start_time_DFS_Loop)+ 's'
    print 'end with func DFS_Loop() whole time: '+ str(time.time() - start)+ 's'    
#print data_set_u
#print data_set_v
    
            
def DFS(node):
    start_time_DFS = time.time()
    
    global t
    visited[node-1] = True
    #print visited
    #print visited
    leader[node-1] = s
    #print leader
    arc = []
    arc = [data_set_v[i] for i,x in enumerate(data_set_u) if x==node] 
    #print arc
    for i in arc:
        #print arc
        #print i
        if visited[i-1]==0:
            #print i
            DFS(i)

    t+=1
    #print t
    f[node-1] = t
    #print f
    print 'end with func DFS time: '+ str(time.time() - start_time_DFS)+ 's'
    print 'end with func DFS whole time: '+ str(time.time() - start)+ 's'
    
DFS_Loop()
print 'DFS_Loop time: '+ str(time.time() - start)+ 's'


##reverse tail and head data
##
##

rev_u,rev_v = data_set_v,data_set_u
new_u = [None] * (len(rev_u))
new_v = [None] * (len(rev_v))
#print rev_v
#print rev_u
for i,val in enumerate(f):
    #rev_u[rev_u.index(i+1)] = val
    #print i+1,val
    #rev_v[rev_v.index(i+1,0,len(rev_v))] = val
    #print rev_v
    #print i,val
    for i_v,val_v in enumerate(rev_v):
        if val_v == i+1:
            #print val_v
            new_v[i_v] = val
    
    for i_u,val_u in enumerate(rev_u):
        if val_u == i+1:
            #print i_u,val_u
            new_u[i_u] = val    
    
#print new_u
#print new_v
data_set_u = new_u
data_set_v = new_v
#print data_set_u
#print data_set_v

print 'reverse data time: '+ str(time.time() - start)+ 's'

DFS_Loop()
print 'DFS_Loop time: '+ str(time.time() - start)+ 's'

#print leader


##calculate repeated times appearancing in leader list
##
##


count_list = [0]*len(leader)
indices = [0]*len(leader)

#for i_lea,val_lea in enumerate(leader):
i_count_list = 0
while len(leader) > 0:
    #print i_lea,val_lea

    count_list[i_count_list] = leader.count(leader[0])
    #print 'count_list: '+ str(count_list)
    indices = [i for i, x in enumerate(leader) if x == leader[0]]
    #print 'indices: '+ str(indices)
    for i in xrange(len(indices)):
        #print 'leader before del: '+ str(leader)
        del leader[leader.index(leader[0])]
        #print 'leader after del: '+ str(leader)
    #print 'leader: '+ str(leader)
    i_count_list = i_count_list+1
    #print 'i_count_list: ' + str(i_count_list)
print 'calc time: '+ str(time.time() - start)+ 's'

sorted_count_list = sorted(count_list, key=int, reverse=True)
print sorted_count_list[0:5]
print datetime.datetime.now()
