#According to Einstein's general relativity theory the faster an object moves throught space, slower it moves through
# time....you can relate the time intervals via this formula T=t/(root(1-(v/c)^2)) T=time elapsed for observer, t=time elapsed for
# moving object in its frame, v=velocity of object, c=speed of light
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
def drawGraph(t):                                   #here we are defining a function to output Satish's age
    curve=t/(cmath.sqrt(1-pow((v/c),2)))
    answer= 25 + curve
    return answer
initialAge_Chandra=25
initialAge_Satish=25
SatishTime=8 #time is in terma of light years
v=0.8  #this is in terms of c
c=1    #this is in terms of c
ChandraTime=SatishTime*(cmath.sqrt(1-pow((v/c),2)))  #applying Einstein's equation for time dilation
ChandraAge= initialAge_Chandra+ChandraTime           #final age of Chandra
a=math.ceil(ChandraTime.real)
SatishAge=initialAge_Satish+SatishTime               #final age of Satish


xlist=np.arange(0,a,1)                               #x coordinates for graph
ylist=drawGraph(xlist)                               #y coordinates for graph
print("1)Age of Chandra is: "+ str(ChandraAge) +"\n  Age of Satish is: " + str(SatishAge)) #OUTPUT Q1
plt.plot(25+xlist,ylist,marker='.',markersize=10)#plotting graph
plt.xlabel("Chandra's age")
plt.ylabel("Satish's age")
plt.title("2)")
plt.show()    #OUTPUT Q2

def drawGraph_2(t):                                  #here we are defining a function to output Satish's time
    curve=t/(cmath.sqrt(1-pow((v/c),2)))
    return curve

xlist=np.arange(0,2.5,0.1)          #x coordinates for graph
ylist=drawGraph_2(xlist)            #y coordinates for graph
plt.xlabel("Time for Chandra (year)")
plt.ylabel("Distance (in light years)")
plt.title("3)A.")
plt.plot(xlist,ylist)               #plottting graph
tlist=np.arange(2.4,4.8,0.1)        #x coordinates for graph
dlist=8-drawGraph_2(tlist)          #y coordinates for graph
plt.plot(tlist,dlist)               #plottting graph
plt.show()

xlist=np.arange(0,5,1)              #x coordinates for graph
ylist=xlist                         #y coordinates for graph
plt.xlabel("Time for Satish (year)")
plt.ylabel("Distance (in light years)")
plt.title("3)B.")
plt.plot(xlist,ylist)                  #plottting graph
tlist=np.arange(4,9,1)                 #x coordinates for graph
dlist=8-tlist                          #y coordinates for graph
plt.plot(tlist,dlist)                  #plottting graph
plt.show()



