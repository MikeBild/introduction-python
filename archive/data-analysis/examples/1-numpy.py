""" NumPy - Examples in a Nutshell """
import numpy as np

# Creation
a = np.array([1, 2, 3])
print('Creation:', a)

b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
print('Creation (2D, typed):', b)

zeros = np.zeros(3)
zeros2D = np.zeros((3, 4))
print('Zeros:', zeros)
print('Zeros (2D):', zeros2D)

arange = np.arange(10)
print('Arange:', arange)
arange = np.arange(10, 25, 2, dtype=int)
print('Arange (start, stop, step):', arange)

random = np.random.random((2, 2))
print('Random (2D):', random)

# Selection

print('Selection:', arange[2])
print('Selection (2D):', random[1, 1])
print('Selection (Slice):', arange[2:4])
print('Index (Boolean):', arange[arange>15])

# Input/Output

data = np.loadtxt("numpy.txt")
data = np.genfromtxt("numpy.txt", delimiter=';')
np.savetxt("numpy.txt", random, delimiter=';')

# Compare

print('Compare (per Element):', a == a)
print('Compare (Array):', np.array_equal(a, a))

# Aggregates

print('Sum:', a.sum())
print('Min:', a.min())
print('Max:', a.max())
print('Mean:', a.mean())

# Copy
c = np.copy(a)
print('Copy:', c)

# Sort
sorting = np.random.random(3)
sorting.sort()
print('Sort:', sorting)

# Manipulation

print('Flatten:', random.ravel())
reshape = np.random.random((2, 2))
reshape.resize(4, 2)
print('Resize:', reshape)

manipulation = np.append(reshape, np.array([[1,2]]), axis=0)
print('Append:', manipulation)

manipulation = np.insert(manipulation, 2, np.array([[3,4]]), axis=0)
print('Insert:', manipulation)

manipulation = np.delete(manipulation, 2, axis=0)
print('Delete:', manipulation)