import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sympy
# These will need to be installed 

r_3=int(input("Enter a number 1 max: "))
r_4=int(input("Enter a number 2 min: "))
p = list(sympy.primerange(r_4,r_3+1))
gap2 = 0
gap3 = 0
gap4 = 0
gap5 = 0
gap6 = 0
gap7 = 0
gap8 = 0
gap9 = 0
gap10 = 0
gap11 = 0
gap12 = 0



for i in range (len(p)):
	if p[i]-p[i-1]==2:
		gap2 += 1
	elif p[i]-p[i-1]==3:
		gap3 += 1
	elif p[i]-p[i-1]==4:
		gap4 += 1
	elif p[i]-p[i-1]==5:
		gap5 += 1
	elif p[i]-p[i-1]==6:
		gap6 += 1
	elif p[i]-p[i-1]==7:
		gap7 += 1
	elif p[i]-p[i-1]==8:
		gap8 += 1
	elif p[i]-p[i-1]==9:
		gap9 += 1
	elif p[i]-p[i-1]==10:
		gap10 += 1
	elif p[i]-p[i-1]==11:
		gap11 += 1
	elif p[i]-p[i-1]==12:
		gap12 += 1
		
#Graph
objects = ('2','3','4','5','6','7','8','9','10','11','12') #x axis
y_pos = np.arange(len(objects))#positions on graph i believe
results = [gap2, gap3, gap4, gap5, gap6, gap7, gap8, gap9, gap10, gap11, gap12] #Y axis data

plt.bar(y_pos, results, align = 'center', alpha = 0.5) #create the bar graph
plt.xticks(y_pos, objects) #where you want the tick marks to show and onjects are the labels
plt.xlabel('Prime Gap')
plt.ylabel('Total Gaps')
plt.title('Number of Prime Gaps')
plt.show()




