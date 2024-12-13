import numpy as np

# Take the number of rows and columns as input from the user
print("Enter the dimensions of the first array")
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Take the 2D array elements as input from the user
arr = np.zeros((rows, cols))
for i in range(rows):
    for j in range(cols):
        arr[i, j] = int(input(f"Enter element [{i+1}, {j+1}]: "))

print("Enter the dimensions of the second array")
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
# Take the 2D array elements as input from the user
arr2 = np.zeros((rows, cols))
for i in range(rows):
    for j in range(cols):
        arr2[i, j] = int(input(f"Enter element [{i+1}, {j+1}]: "))

print("The first array is:\n")
print(arr)
print("\n")
print("The second array is:\n")
print(arr2)  

#now doing matrix multiplication
new = arr2.shape
new = new[::-1]
if(arr.shape == new):

    m = np.dot(arr,arr2)
    print("\nMatrix Multiplication is: \n",m)
else:
    print("Matrix Multiplication is not possible")
#trial = np.array(range(1,32,2))
#print(trial)
#now doing matrix addition

a = np.add(arr,arr2)
print("\nAddition of two matrices is: \n",a)

#now doing matrix substraction

s = np.subtract(arr,arr2)
print("\nSubstraction of two matrices is: \n",s)