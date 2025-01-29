from efk import Ekf
import numpy as np

def f(X,U,C):
    Tcom = X[0]
    Tcap = X[1]
    P = U[0]
    dt = C[0]
    Ccom = C[1]
    Text = C[2]
    alpha = C[3]
    beta = C[4]
    gamma = C[5]
    Ccap = C[6]
    Tcryo = C[7]
    
    Tcom = Tcom + dt*(P - alpha*(Tcom - Tcryo) - beta*(Tcom - Tcap)) / Ccom
    Tcap = Tcap + dt*(beta*(Tcom - Tcap) - gamma*(Tcap - Text)) / Ccap
    
    return np.array([Tcom,Tcap])

def h(X,C = None):
    Tcap = X[1]
    return np.array([Tcap])

time = np.linspace(0,100,100)
# P increase from 0 to 1 during the first 2 seconds and stay at 1
P = np.concatenate((np.linspace(0,1000,20),1000*np.ones(80)))

dt = time[1] - time[0]

C = np.array([dt,10,20,0.5,0.1,0.5,1,-196])

TrueStateNoise = np.random.normal(0,1,len(time)) * dt * 0.5

TrueState = np.zeros((len(time),2))
TrueState[0] = np.array([C[7], -14])
Measurments = np.zeros((len(time),1))

for i in range(1,len(time)):
    TrueStateNoise[i] += TrueStateNoise[i-1]
    TrueState[i] = f(TrueState[i-1],np.array([P[i]]),C)
    TrueState[i][0] += TrueStateNoise[i]
    Measurments[i] = TrueState[i][1] + np.random.normal(0,5)*1


EkfX = np.zeros((2,len(time)))
EkfP = np.zeros((2,2,len(time)))
ekf = Ekf(2)
ekf.cov_u = np.array([[5**2]])
ekf.x = TrueState[0]
ekf.c = C

for i in range(len(time)):
    ekf.predict(f,np.array([P[i]]))
    ekf.update(h,Measurments[i], np.array([[1**2]]))
    EkfX[:,i] = ekf.x
    EkfP[:,:,i] = ekf.P
    

# plot it
import matplotlib.pyplot as plt
plt.plot(time,TrueState[:,0],label="True Tcom")
plt.plot(time,TrueState[:,1],label="True Tcap")
plt.plot(time,Measurments,label="Measurments")
plt.plot(time,EkfX[0],label="Estimated Tcom")
plt.plot(time,P,label="P")
plt.legend()
plt.show()

print("time = [",end="")
for i in range(len(time)):
    print(str(time[i]) + ",",end="")
print("]")

input("Press Enter to continue...")
print("P = [",end="")
for i in range(len(P)):
    print(str(P[i]) + ",",end="")
print("]")
input("Press Enter to continue...")

print("TrueTcom = [",end="")
for i in range(len(time)):
    print(str(TrueState[i,0]) + ",",end="")
print("]")
input("Press Enter to continue...")
print("measurments = [",end="")
for i in range(len(time)):
    print(str(Measurments[i][0]) + ",",end="")
print("]")
input("Press Enter to continue...")
print("EkfTcom = [",end="")
for i in range(len(time)):
    print(str(EkfX[0,i]) + ",",end="")
print("]")

