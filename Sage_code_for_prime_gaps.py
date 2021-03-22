r_3=int(input("Enter a number 1 max"))
r_4=int(input("Enter a number 2 min"))
p = prime_range(r_4,r_3)
l_2=[]
l_3=[]
l_4=[]
l_5=[]
l_6=[]
l_7=[]
l_8=[]
l_9=[]
l_10=[]
l_11=[]
l_12=[]
for i in range (len(p)):
    if p[i]-p[i-1]==2:
        l_2.append(p[i])
    if p[i]-p[i-1]==3:
        l_3.append(p[i])
    if p[i]-p[i-1]==4:
        l_4.append(p[i])
    if p[i]-p[i-1]==5:
        l_5.append(p[i])
    if p[i]-p[i-1]==6:
        l_6.append(p[i])
    if p[i]-p[i-1]==7:
        l_7.append(p[i])
    if p[i]-p[i-1]==8:
        l_8.append(p[i])
    if p[i]-p[i-1]==9:
        l_9.append(p[i])
    if p[i]-p[i-1]==10:
        l_10.append(p[i])
    if p[i]-p[i-1]==11:
        l_11.append(p[i])
    if p[i]-p[i-1]==12:
        l_12.append(p[i])
bar_chart([0,0,len(l_2),len(l_3),len(l_4),len(l_5),len(l_6),len(l_7),len(l_8),len(l_9),len(l_10),len(l_11),len(l_12)],width=.5,legend_label='Prime gaps').show()