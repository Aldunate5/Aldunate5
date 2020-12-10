import numpy as np
a = np.array([0, 1])
b = np.array([9, 8])
c = a
print('Array a: {}'.format(repr(a)))
c[0] = 5
print('Array a: {}'.format(repr(a))) #changes in a
d = b.copy()
d[0] = 6
print('Array b: {}'.format(repr(b)))

arr = np.array([np.nan, 1, 2]) #fill with not available
print(repr(arr))

arr = np.arange(-1.5, 4, .2) #interval, step
print(repr(arr))
arr = np.linspace(-1.5, 4, num=4) #interval, quantity
print(repr(arr))

arr = np.arange(8)
arr = np.reshape(arr, (2, 4))
flattened = arr.flatten()
transposed = np.transpose(arr)
print(repr(arr))
print('arr shape: {}'.format(arr.shape))
print(repr(flattened))
print('flattened shape: {}'.format(flattened.shape))

#exp ,e,log,log2,log10
#np.power(base,X)
print(np.log(np.e))

arr3 = np.array([[1, 2], [3, 4], [5, 6]])
print(arr3.shape)
arr4 = np.array([[-1, 0, 1], [3, 2, -4]])
print(arr4.shape)
print(repr(np.matmul(arr4, arr3)))

random_arr=np.random.randint(2,4,size=(2,2))
print(random_arr)

random_arr=np.random.uniform(2,4,size=(2,2))
print(random_arr)

print(np.random.normal(loc=1.5, scale=3.5))
print(repr(np.random.normal(loc=-2.4, scale=4.0,size=(2, 2))))

colors = ['red', 'blue', 'green']
print(np.random.choice(colors)) #allows to randomly sample
print(repr(np.random.choice(colors, size=2)))

#slicing arr[x,y]x: rows, y columns, :recorrer
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(repr(arr[:]))
print(repr(arr[1:]))
print(repr(arr[:, -1]))
print(repr(arr[:, 1:]))
print(repr(arr[0:1, 1:]))
print(repr(arr[0, 1:]))

#argmin, argmax -> position in array; axis=0 row axis=1 columns

#Filtering
arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])
print(repr(arr > 0))
print(repr(np.any(arr > 0, axis=0)))
print(repr(np.any(arr > 0, axis=1)))
print(repr(np.all(arr > 0, axis=1)))
#axis=0 column, axis=1 rows

#concatenation
arr1 = np.array([[0, 72, 3],
                 [1, 3, -60],
                 [-3, -2, 4]])
arr2 = np.array([[-15, 6, 1],
                 [8, 9, -4],
                 [5, -21, 18]])
print(repr(np.concatenate([arr1, arr2])))
print(repr(np.concatenate([arr1, arr2], axis=1)))
print(repr(np.concatenate([arr2, arr1], axis=0)))

'''
arr = np.array([1, 2, 3])
np.save('arr.npy', arr)
load_arr = np.load('arr.npy')
print(repr(load_arr))
'''