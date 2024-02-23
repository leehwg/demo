##2-LÀM VIỆC VỚI THƯ VIỆN TRONG PYTHON
##THƯ VIỆN NUNPY
import numpy as np
##MẢNG 1 CHIỀU
#Khởi tạo
#VD1: Hàm np.array()
arrl = np.array([6, 6.5, 4, 5.5, 7, 8.5])
print(arrl)
print(type(arrl))
print(arrl.dtype)

#VD2: Hàm np.asarray()
list_sample = [5, 7, 6.5, 8, 9.5]
tuple_sample = (6, 4, 5.5, 8.5)
arr2 = np.asarray(list_sample)
arr3 = np.asarray(tuple_sample)
print(arr2)
print(arr3)

#VD3: Hàm np.zeros(), np.ones():
arr_zeros = np.zeros(4)
arr_ones = np.one(3,dtype=int)
print(arr_zeros)
print(arr_ones)

#VD4: Hàm np.arange(start, stop, step, dtype):
arr1 = np.arange(2, 10, 1.5)
arr2 = np.arange(6)
print(arr1)
print(arr2)

#VD5: Hàm np.linspace(start, stop, num, endpoint, dtype):
arr = np.linspace(5, 15, 6)
print(arr)

#VD6: Hàm np.random.rand()/randn()/randint():
arr1 = np.random.rand(3)
arr2 = np.random.randn(4)
arr3 = np.random.randint(10, 45, 5)
print(arr1)
print(arr2)
print(arr3)

#VD7: Hàm np.random.uniform(low, high, size):
arr1 = np.random.uniform(0.0, 5.0, 20)
print(arr1)

#VD8:Hàm np.random.normal(loc, scale, size):
arr2 = np.random.normal(5.0, 1.0, 10000)
print(arr2)

##TRUY XUẤT
#VD1:
arr = np.random.randint(10, 80, 8)
print(arr)
print(arr[1])
print(arr[-2])
print(arr[[1,3,4]])
print(arr[2:5])
print(arr[arr < 40])

#VD2:
arr = np.random.randint(10, 80, 8)
print(arr)
indices = np.where(arr>40)
print(indices)
print(arr[indices])
print(np.extract(arr>35,arr))
print(np.extract(np.mod(arr,2)==0, arr))

#VD3:
arr = np.random.randint(5, 45, 7)
print(arr)
print(np.min(arr)) # giá trị min
print(np.argmin(arr)) # index phần tử min
print(np.max(arr)) # giá trị max
print(np.argmax(arr)) # index phần tử max
print(np.mean(arr)) # giá trị trung bình
print(np.median(arr)) # giá trị trung vị
print(np.std(arr)) # độ lệch chuẩn

##THÊM PHẦN TỬ
arr = np.array([4, 2, 15, 7, 9, 5, 11, 8])
print(arr)
arr = np.append(arr, [6, 3]) # Thêm phần tử vào cuối
print(arr)
arr = np.insert(arr, 2, [6, 1]) # Thêm tại vị trí bất kỳ
print(arr)

#XÓA PHÂẦN TỬ
arr = np.array([4, 2, 15, 7, 9, 5, 11, 8])
arr = np.delete(arr, [2, 4]) # Xóa phần tử theo index
print(arr)

#SẮP XẾP
arr = np.array([4, 2, 15, 7, 9, 5, 11, 8])
print(np.sort(arr))
print(np.sort(arr)[::-1])

#TÍNH TOÁN SỐ HỌC
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 % arr2)


###MẢNG NHIỀU CHIỀU
##KHỞI TẠO
#VD1:
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.shape) # Kích thước array

#VD2:
arr = np.array([[[1, 2, 3], [4, 5, 6]],
[[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr.shape) # Kích thước array

#VD3:
arr = np.zeros([2, 3, 4], dtype=int)
print(arr)

arr = np.ones([2, 3], dtype=int)
print(arr)

##TRUY XUẤT
arr = np.array([[[1, 2, 3], [4, 5, 6]],
[[7, 8, 9], [10, 11, 12]]])
print(arr)
print(np.max(arr))
print(np.mean(arr[1]))
print(arr[np.where(arr>8)])

##CẬP NHẬP GIÁ TRỊ
arr = np.array([[[1, 2, 3], [4, 5, 6]],
[[7, 8, 9], [10, 11, 12]]])
print(arr)

arr[1][0][2] = 10
print(arr[1][0])

##SẮP XẾP
arr = np.array([[[1, 3, 2], [6, 4, 5]],
 [[7, 9, 8], [12, 10, 11]]])
print(np.sort(arr))

##TÍNH TOÁN SỐ HỌC
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([1, 2, 3])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

#CHUYỂN ĐỔI DÒNG - CỘT
arr1 = np.array(range(12))
print(arr1)

arr_reshape = arr1.reshape(3,4)
print(arr_reshape)

arr2 = arr_reshape.reshape(1,-1)
print(arr2)

arr3 = arr_reshape.flatten()
print(arr3)
