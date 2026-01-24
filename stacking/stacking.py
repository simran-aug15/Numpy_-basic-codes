"""vertically,horizontally
   vstack()=row wise
   hstack()=column wise
"""
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print("vertical element is",np.vstack(arr1,arr2))
print("Horizontal element is",np.hstack(arr1,arr2))