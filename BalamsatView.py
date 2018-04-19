
import matplotlib.pyplot as plt

from getBalamsatData import temperatura
from getBalamsatData import presion
from getBalamsatData import aceleracion
from getBalamsatData import ax, ay, az 
from getBalamsatData import ox, oy, oz

# plt.subplot(111)
# plt.plot(temperatura)
# plt.ylabel('TempTEST')

# plt.subplot(111)
# plt.plot(presion)
# plt.ylabel('PresTEST')

# plt.subplot(121)
# plt.plot(ax,'r')
# plt.plot(ay,'g')
# plt.plot(az,'b')

plt.subplot(111)
plt.plot(ox,'r')
plt.plot(oy,'g')
plt.plot(oz,'b')

# plt.subplot(528)
# plt.plot(ox,'r')
# plt.plot(oy,'g')
# plt.plot(oz,'b')

plt.show()

