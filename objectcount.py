import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import morphology

figure1=np.array ([
    [1,1,1,1],
    [1,1,1,1],
    [0,0,1,1],
    [0,0,1,1],
    [1,1,1,1],
    [1,1,1,1]
    ])

figure2=np.array ([
    [1,1,1,1],
    [1,1,1,1],
    [1,1,0,0],
    [1,1,0,0],
    [1,1,1,1],
    [1,1,1,1]
    ])

figure3=np.array ([
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
    ])

figure4=np.array ([
    [1,1,0,0,1,1],
    [1,1,0,0,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
    ])

figure5=np.array ([
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,0,0,1,1],
    [1,1,0,0,1,1]
    ])

arr = np.load("ps.npy.txt")

f1= morphology.binary_hit_or_miss(arr, figure1)
f2= morphology.binary_hit_or_miss(arr, figure2)
f3= morphology.binary_hit_or_miss(arr, figure3)
f4= morphology.binary_hit_or_miss(arr, figure4)
f5= morphology.binary_hit_or_miss(arr, figure5)


print(np.sum(f1))
print(np.sum(f2))
print(np.sum(f3))
print(np.sum(f4))
print(np.sum(f5))

plt.figure()
ax1 = plt.subplot(121)
plt.imshow(arr)
plt.show()