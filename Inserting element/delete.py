"""np.delete(array,index,axis=None,flatten array)"""
import numpy as np
arr_1d=np.array([10,20,30,40,50])
print(arr)
new_arr=np.delete(arr_1d,0)
print("element in row is")
print(new_arr)
arr_2d=np.array([[1,2,3],[4,5,6]])
new_2_arr_2d=np.delete(arr_2d,0,axis=0)
print(new_2_arr_2d)