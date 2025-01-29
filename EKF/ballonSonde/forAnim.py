from efk import Ekf
import numpy as np

def f(X,U,C):
    dt = C[0]
    v = U[0]
    return np.array([X[0] + v*dt])

def h(X,C = None):
    z = X[0]/1000
    q = 1/(1+np.exp((z-15)/5))
    t1 = -4.5*z + 20
    t2 = 1.8*z - 80
    return np.array([q*t1 + (1-q)*t2])

time = np.linspace(0,8000,100)

U = np.ones((len(time),1))*10

dt = time[1] - time[0]

C = np.array([dt])

TrueStateNoise = np.random.normal(0,1,len(time)) * dt

TrueState = np.zeros((len(time),1))
TrueState[0] = np.array([0])
Measurments = np.zeros((len(time),1))
MeasurmentsDerive = np.random.normal(0,1,len(time)) * dt * 0.01

for i in range(1,len(time)):
    TrueStateNoise[i] += TrueStateNoise[i-1]
    MeasurmentsDerive[i] += MeasurmentsDerive[i-1]
    TrueState[i] = f(TrueState[i-1],U,C)
    TrueState[i] += TrueStateNoise[i]
    Measurments[i] = h(TrueState[i]) + np.random.normal(0,1)+ MeasurmentsDerive[i]

EkfX = np.zeros((1,len(time)))
EkfP = np.zeros((1,1,len(time)))
ekf = Ekf(1)
ekf.cov_u = np.array([[5**2]])
ekf.x = TrueState[0]
ekf.c = C

Zcov = 1
for i in range(len(time)):
    ekf.predict(f,U[i])
    ekf.update(h,Measurments[i] , np.array([[Zcov]]))
    Zcov += dt * 0.01
    EkfX[:,i] = ekf.x
    EkfP[:,:,i] = ekf.P

# temp vs altitude
altitude = np.linspace(0,50000,100)
temp = np.zeros((len(altitude),1))
for i in range(len(altitude)):
    temp[i] = h(np.array([altitude[i]]))
    

# plot it
import matplotlib.pyplot as plt
plt.plot(time,TrueState,label="True altitude")
plt.plot(time,EkfX[0],label="Ekf altitude")
sigma3 = np.sqrt(EkfP[0,0])*3
plt.fill_between(time,EkfX[0]-sigma3,EkfX[0]+sigma3,alpha=0.5)
# plt.plot(time,Measurments,label="Measurments")
plt.legend()
plt.show()

print("time = [",end="")
for i in range(len(time)):
    print(str(time[i]) + ",",end="")
print("]")

input("Press Enter to continue...")
print("U = [",end="")
for i in range(len(U)):
    print(str(U[i,0]) + ",",end="")
print("]")
input("Press Enter to continue...")

print("TrueTcom = [",end="")
for i in range(len(time)):
    print(str(TrueState[i,0]) + ",",end="")
print("]")
input("Press Enter to continue...")
print("measurments = [",end="")
for i in range(len(time)):
    print(str(Measurments[i,0]) + ",",end="")
print("]")
input("Press Enter to continue...")
print("EkfTcom = [",end="")
for i in range(len(time)):
    print(str(EkfX[0,i]) + ",",end="")
print("]")
input("Press Enter to continue...")
print("temp = [",end="")
for i in range(len(altitude)):
    print(str(temp[i,0]) + ",",end="")
print("]")
input("Press Enter to continue...")
print("altitude = [",end="")
for i in range(len(altitude)):
    print(str(altitude[i]) + ",",end="")

input("Press Enter to continue...")
print("Z3Sigma = [",end="")
for i in range(len(EkfX[0])):
    print(str(sigma3) + ",",end="")
print("]")

