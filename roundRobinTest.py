from roundRobin import *

p1 = Process(0,5)
p2 = Process(30,9)
p3 = Process(2,7)
p4 = Process(2,5)
p5 = Process(4,6)
p = [p1,p2,p3,p4,p5]
out = roundRobin(p,4)
i=1
for x in out:
    print("process",i,":")
    x.printProcess()
    i+=1