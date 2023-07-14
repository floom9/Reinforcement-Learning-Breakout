import numpy as np
from collections import defaultdict


def normalizedProps(size):
    randomArray=np.random.rand(size)
    randomArray/= randomArray.sum()
    return (lambda: randomArray)




somesize=3
Q = defaultdict(normalizedProps(3))






mylist=[1,2,3]

for i in range(100):
    tmp=np.random.choice(mylist, p=Q[i])
    print(Q[i])
    print(tmp)
