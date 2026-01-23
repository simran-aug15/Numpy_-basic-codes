"""
np.insert(array,index,value,asix=None)
array=orig.array
axis=0=row wise
axis=1=column wise

"""
import numpy as np
arr=np.array([10,20,30,40,50])
new_arr=np.insert(arr,2,100)
print(new_arr)
