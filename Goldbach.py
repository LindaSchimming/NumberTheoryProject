import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sympy


prime = list(sympy.primerange(1,1000))
maxP = 1000
prime2 = prime

composites = {}
primetosum = {}
n=0
m=0
while n < len(prime):
	sum = int(prime[n])+int(prime[m])
	if(m >= n):
		#if (sympy.isprime(sum) == False):
		if (composites.get(sum) is not None):
			 composites[sum] = composites.get(sum, 0) + 1
			 primetosum[sum]= primetosum.get(sum,0) + ", " + str(prime[n]) + "+" + str(prime[m])
		else: 
			 composites[sum] = 1
			 primetosum[sum] =  str(prime[n]) + "+" + str(prime[m])
	if(m == len(prime)-1):	  
	   n+=1
	   m =0
	m+=1

[1,2,3,4,5,6,7,8,9,0]
{1,2,3,4,5,6,7,8,9,0}
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

#for keys,values in primetosum.items():
    #print(keys)
    #print(values)
#Graph
objects = getobjects(composites)
#y_pos = np.arange(len(objects))
results = getresults(composites)
print(min(objects))
print(max(results))
print(len(objects))
print(len(results))
print(len(composites))

plt.scatter(objects, results, s=0)
#plt.bar(objects, results, align = 'center')
#plt.xticks(y_pos, objects)

plt.xticks(np.arange(min(objects), max(objects)+1, 500.0))
plt.yticks(np.arange(0, max(results)+1, 10.0))
for i in range(len(objects)):
    plt.text(x = objects[i]-0.5 , y = results[i]+0.1, s = results[i], size = 6)
plt.xlabel('Integers')
plt.ylabel('Occurances')
plt.title('Number of Integers from Summing Pairs of Primes < ' + str(maxP))
plt.show()

#102: 120 unique integers
#1000: 1147 unique integers
#5000: 5651 unique integers
#10000: 11172 unique integers