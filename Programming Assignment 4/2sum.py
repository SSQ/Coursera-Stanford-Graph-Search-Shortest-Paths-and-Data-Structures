# need 12h to get the result 

filename = "2sum.txt"
X = [int(l) for l in open(filename)]
#print len(X)
    
values = [True] * len(X)

dictionary = dict(zip(X, values))
#print dictionary[X[0]]

t = range(-10000,10001)
num = {}

for target in t:
    print "target: " + str(target)
    '''
    if target % 1000 ==0:
        print target
    '''
    for x in dictionary.keys():
        #print "x: " + str(x)
        y = target - x
        #print dictionary.has_key(y)
        if x == y:
            continue
        if dictionary.has_key(y):
            #num.append(1)
            #print dictionary.has_key(y)
            #print "target: " + str(target)
            #print "x: " + str(x)
            #print "y: " + str(y)
            num[target] = [x,y]
            break
            #print num
    print len(num)
print len(num)
#print sum(num)
#print len(num)
            
        
