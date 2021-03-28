import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sympy

prime = list(sympy.primerange(1,100))
prime2 = prime

composites = {}
primetosum = []
n=0
m=0
while n < len(prime):
	sum = int(prime[n])+int(prime[m])
	
	if (sympy.isprime(sum) == False):
		if (composites.get(sum) is not None):
		  composites[sum] = composites.get(sum, 0) + 1
		else: 
		  composites[sum] = 1
	if(m == len(prime)-1):	  
	   n+=1
	   m =0
	m+=1


# Python program to get 
# dictionary keys as list
  
def getobjects(dict):
    list = []
    for key in dict.keys():
        list.append(key)
          
    return list
def getresults(dict):
    list = []
    for key in dict.keys():
        list.append(dict.get(key,0))
          
    return list


#Graph
objects = getobjects(composites)
#y_pos = np.arange(len(objects))
results = getresults(composites)

plt.bar(objects, results, align = 'center', alpha = 0.5)
#plt.xticks(y_pos, objects)
plt.xticks(np.arange(min(objects), max(objects)+1, 10.0))
plt.yticks(np.arange(min(results), max(results)+1, 1.0))
plt.xlabel('Composites')
plt.ylabel('Occurances')
plt.title('Number of composites')
plt.show()