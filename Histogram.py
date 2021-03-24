lower=int(input("Enter in lower bound"))
higher=int(input("Enter upper bound"))
@ interact
def _(lower=slider(lower,higher/5,1), higher=slider(higher/5+1,higher,1)):
    r=prime_range(lower,higher)
    l = [r[i]-r[i-1] for i in range (1,len(r))]
    return histogram(l,density=True, rwidth  = .5,align = 'mid',bins=20)
