

import sys
filename = "2sum.txt"
numbers = [int(l) for l in open(filename)]
targets = range(-10000,10001)
H = {}
answers = {}
 
for i in numbers:
  H[i] = True
 
for i in numbers:
  for t in targets:
    if t - i in H:
      if i == t - i:
        continue
      if t not in answers:
        answers[t] = set([tuple(sorted([i, t - i]))])
      else:
        answers[t].add(tuple(sorted([i, t - i])))
 
print len(answers)
