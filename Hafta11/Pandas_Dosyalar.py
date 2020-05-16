import pandas as pd
import numpy as np
# # python list
# python_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(np.array([python_list]).T)
# # numpy array
# numpy_array= np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]])
#
# numpy_array2 = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]])
# print(np.concatenate([numpy_array, numpy_array2], axis=0))
#
# print(numpy_array.reshape(4,3))
# numpy_array = numpy_array.reshape(4,3)
# print(numpy_array[1,2])
# print(np.concatenate([numpy_array, numpy_array], axis=1).T)
# print(np.array([numpy_array.sum(axis=1)]).T)
# boolean_array = numpy_array%3 == 0 and numpy_array > 5
# print(boolean_array)
# print(numpy_array[boolean_array])
# numbers = [2,4,6,8,10,12]
# index_1 = ['a', 'b', 'c', 'd', 'e', 'f']
#
# my_series = pd.Series(data=numbers)
# print(my_series)
# print(my_series[my_series > my_series.mean()])
#
# numbers_dictionary = {'a': 0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6,'h':7, 'i':8,'j':9}
# pandas_series = pd.Series(data=numbers_dictionary)
# print(pandas_series)
# print(pandas_series.ndim)

# dict1 = dict(a=1, b=2, c=3, d=4)
# dict2 = dict(a=5, b=6, c=7, d=8, e=9, f=19)
# data1 = dict(first=dict1, second=dict2)
# print(data1)
# my_dataframe = pd.DataFrame(data1)
# print(my_dataframe)
#
# s1 = pd.Series([1.1, 2.2, 3.3, 4.4])
# s2 = pd.Series(['a', 'b', 'c', 'd', 'e'])
# data2 = dict(first=s1, second=s2)
# print(data2)
# df2 = pd.DataFrame(data2)
# print(df2)

df = pd.read_csv(r"C:\Users\Akademik\Desktop\googleplaystore.csv")
print(df.dtypes)