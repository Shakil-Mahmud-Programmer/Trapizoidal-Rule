import numpy,tabulate,matplotlib.pyplot as plt
Data=[];x_val=[];y_val=[]
def f(x):
    return 2**x

n = int(input("Number of subintervals: "))
x = numpy.zeros(n)
y = numpy.zeros(n)
ul = float(input("Upper limit: "))
ll = float(input("lower limit: "))
x[0]=ll
x[n-1]=ul
h = (ul - ll) / (n-1)

for i in range(0, n):
    y[i] = f(x[i])
    x_val.append(round(x[i],3))
    y_val.append(round(y[i],3))
    try:
        x[i+1] = x[i] + h
    except:
        continue

def Tapezoidal(y,n,h):
    sum=0
    for i in range(1,n-1):
        sum+=y[i]
    return (h/2)*(y[0]+y[n-1]+2*sum)

Data.append(x_val)
Data.append(y_val)
print(tabulate.tabulate(Data,tablefmt="fancy_grid"))
print("the result is : ",round(Tapezoidal(y,n,h),4))


plt.style.use('seaborn')
plt.title("Trapizoidal Rule",color='lime')
plt.plot(x_val,y_val,color='deepskyblue',linewidth=1,marker='o',markersize=5,label='f(x)')
plt.legend()
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()


