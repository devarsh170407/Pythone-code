import matplotlib.pyplot as plt
import numpy as np
a=np.pi
t=np.linspace(0,10,1000)
s=np.sin(2*np.pi*t)
s2=np.cos(2*np.pi*t)
plt.subplot(2,1,1)
plt.plot(t,s,'b-')
plt.subplot(2,1,2)
plt.plot(t,s2,'k-')
plt.title('sine wave')
plt.xlabel('time')
plt.ylabel('amplitude')
# plt.legend(['Sine 1'])
plt.savefig('sinewave.jpg')
plt.show()
