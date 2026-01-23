#astype()=change one data type to another data type
#astype(new type)
import numpy as np
arr=np.array([1.2,3.4,4.5,6.7])
int_arr=arr.astype(int)
print("The elements before change is",arr)
print("The elements after change is",int_arr)