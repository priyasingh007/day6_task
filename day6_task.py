#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Numpy in python:
#1. what is Numpy
#NumPy is a general-purpose array-processing package. 
#It provides a high-performance multidimensional array object, and tools for working with these arrays.
#It is the fundamental package for scientific computing with Python


# In[2]:


#2. Why Numpy arrays?
#>NumPy arrays are faster and more compact than Python lists.
#>An array consumes less memory and is convenient to use. NumPy uses much less memory to store data and it provides a mechanism of specifying the data types. 
#>This allows the code to be optimized even further.


# In[3]:


#Limitation of Numpy:
#Require a contiguous allocation of memory: Insertion and deletion operations 
#become costly as data is stored in contiguous memory locations as shifting it requires shifting


# In[9]:


#Numpy ndarrays objects
#The most important object defined in NumPy is an N-dimensional array type called ndarray. 
#It describes the collection of items of the same type. Items in the collection can be accessed using a zero-based index.
#Every item in an ndarray takes the same size of block in the memory. Each element in ndarray is an object of data-type object (called dtype).

# The basic ndarray is created using an array function in NumPy as follows −

# syntax: numpy.array 


# In[11]:


#example:
import numpy as np 
a = np.array([2,4,6,8,10]) 
a


# In[14]:


#Aray indexing and slicing:
#Indexing in 1 dimension:
import numpy as np

a1 = np.array([1, 2, 3, 4])

print(a1)


# In[15]:


#Indexing in 2 dimensions
#We can create a 2 dimensional numpy array from a python list of lists, like this:

import numpy as np

a2 = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])


# In[16]:


print(a2)


# In[17]:


#Indexing in 3 dimensions
#We can create a 3 dimensional numpy array from a python list of lists of lists, like this:

import numpy as np

a3 = np.array([[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
               [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
               [[30, 31, 32], [33, 34, 35], [36, 37, 38]]])


# In[18]:


print(a3)


# In[21]:


#slicing 0f 1d array
import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
a1[1:4] 


# In[20]:


#slicing of 2d array
import numpy as np

a2 = np.array([[10, 11, 12, 13, 14],
               [15, 16, 17, 18, 19],
               [20, 21, 22, 23, 24],
               [25, 26, 27, 28, 29]])

print(a2[1:,2:4])


# In[25]:


#memory layout of ndarray:
#The following attributes contain information about the memory layout of the array:

#ndarray.flags:Information about the memory layout of the array.

#ndarray.shape:Tuple of array dimensions.

#ndarray.strides:Tuple of bytes to step in each dimension when traversing an array.

#ndarray.ndim:Number of array dimensions.

#ndarray.data:Python buffer object pointing to the start of the array’s data.

#ndarray.size:Number of elements in the array.

#ndarray.itemsize:Length of one array element in bytes.

#ndarray.nbytes:Total bytes consumed by the elements of the array.

#ndarray.base:Base object if memory is from some other object.


# In[1]:


import numpy as np  
a = np.array([[1,2,3]])  
print("Each item contains",a.itemsize,"bytes")  


# In[2]:


#views and copies:
#Copy: The copy is a new array.The copy owns the data and any changes made to the copy will not affect original array,
#and any changes made to the original array will not affect the copy.
    
#View: The view is just a view of the original array.The view does not own the data and any changes made to the view will affect the original array,
#and any changes made to the original array will affect the view.


# In[4]:


#copy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 9

print(arr)
print(x)


# In[6]:


#view
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 9

print(arr)
print(x)


# In[7]:


#The copy SHOULD NOT be affected by the changes made to the original array.
#The view SHOULD be affected by the changes made to the original array.


# In[8]:


#Creating array in numpy: 
#NumPy is used to work with arrays. The array object in NumPy is called ndarray.
#We can create a NumPy ndarray object by using the array() function.


# In[9]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


# In[10]:


#Create a 1-D array containing the values 1,2,3,4,5:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)


# In[11]:


#Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


# In[12]:


# Python program to demonstrate
# binary operators in Numpy
import numpy as np
 
a = np.array([[1, 2],
            [3, 4]])
b = np.array([[4, 3],
            [2, 1]])
 
# add arrays
print ("Array sum:\n", a + b)
 
# multiply arrays (elementwise multiplication)
print ("Array multiplication:\n", a*b)


# In[13]:


#Array data-types:
#Data Type Objects (dtype)
#A data type object describes interpretation of fixed block of memory corresponding to an array, depending on the following aspects −

#1.Type of data (integer, float or Python object)

#2.Size of data

#3.Byte order (little-endian or big-endian)

#In case of structured type, the names of fields, data type of each field and part of the memory block taken by each field.
#If data type is a subarray, its shape and data type


# In[21]:


#A dtype object is constructed using the following syntax −
#numpy.dtype(object, align, copy)

import numpy as np 
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
student


# In[22]:


import numpy as np 

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
a


# In[24]:


#Each built-in data type has a character code that uniquely identifies it.

#'b' − boolean

#'i' − (signed) integer

#'u' − unsigned integer

#'f' − floating-point

#'c' − complex-floating point

#'m' − timedelta

#'M' − datetime

#'O' − (Python) objects

#'S', 'a' − (byte-)string

#'U' − Unicode

#'V' − raw data (void)


# In[ ]:




