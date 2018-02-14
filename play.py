from pprint import pprint  #Allows pretty printing
import numpy as N


#a = [2,-3.3,'hello',1,-12]
#
#for i in range(5):
#    print a[i]




#a=1
#while a < 10:
#    print a
#    a = a + 1
#
#myaddress = [23, 'Orchard', 'Terrace', 'Wynantskill', \
#             'NY', 12198]
#
#for i in myaddress:
#    print i



#def temptest(T):
#    Tflags = [False]*len(T)
#    for i in range(len(T)):
#        if(T[i] > 273.15):
#            Tflags[i] = True
#    return Tflags
#T = [273.4,265.5,277.7,285.5]
#Tflags = temptest(T)
#print Tflags
#T.reverse()
#print T
#print dir(T)
#
#maxT = numpy.max(T)
#minT = numpy.min(T)
#avg_max_min = 0.5 * (maxT+minT)
#print avg_max_min




#def area(radius):
#    if radius < 0:
#        raise ValueError, 'radius negative'
#    area = numpy.pi * radius**2
#    return area
#radius = -10
#try:
#    a = area(radius)
#except:
#    a = area(abs(radius))
#print a




#Converting  a list into an array of type double
#mylist = [[2, 3, -5],[21, -2, 1]]
#array = N.array(mylist, dtype='d')
#print array




##Initializing an array of type double with zeros
#a = N.zeros((3,2), dtype='d')
#print a
##Initializing an array of integers or floats (similar to NCL's ispan)
#a = N.arange(10)  #Integers
#a = N.arange(10.) #Floats
#print( a)
##Initialize a 4 row, 5 column array of floats set to zero
#a = N.zeros((4,5), dtype='f')
#print a
#
##Show array sizes and shapes
#a = N.zeros((4,5), dtype='f')
#print N.shape(a)  #Returns the shape of array as a tuple ((4,5))
#print N.ndim(a)   #Returns rank of array (2)
#print N.size(a)   #Returns size of array (20)
#print a.dtype.char#Returns the array type (f)
#
##Initialize 3 arrays to demonstrate some other tasks
#a = N.arange(6)
#b = N.arange(8)
#c = N.zeros((12,3), dtype='f')
##Rehape array
#print N.reshape(a,(2,3))
##Transpose array
#print N.transpose(c)
##Make array 1-D
#print N.ravel(a)
##Concatenate arrays
#print N.concatenate((a,b))
##Repeat array elements 3 times and return 1-D array of result
#print N.repeat(a,3)
##Convert array a to another type
#print a.astype('f')




##Take 1-D lat and lon arrays and convert them to a tuple of 2 elements,
##one of which is a 2-D array of lons and the other a 2-D array of lats.
##These coordinates then can be assigned to a 2-D array of data.
#lon = N.array([0,45,90,135,180,225,270,315,360])
#lat = N.array([-90,-45,0,45,90])
#a = N.meshgrid(lon,lat)
#print a




#Conditional operations within an array (like NCL's where function)
a = N.arange(8)
print a > 3
print N.greater(a, 3)
#Note that we CANNOT use Python's built-in "and" and "or" operators
#to do operations within an array. Must use NumPy functions instead:
print N.logical_and(a>1, a<=3)
#Python has a where function, too! Returns a tuple with the number of
#elements corresponding to the rank of the input array (i,e. a 2-D
#input array will return a two-element tuple whose first value is an
#array listing the row index where the condition is true, and the 2nd
#value is an array listing the column index where condition is true.
condition = N.logical_and(a>3, a<6)
answer = N.where(condition, a*2, 0)
print answer
#Where can also be used to return a list of indices
condition = N.logical_and(a>3, a<6)
answer_indices = N.where(condition)
answer = (a*2)[answer_indices]
print answer
