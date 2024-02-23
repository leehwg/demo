import pandas as pd
import numpy as np
###Cấu trúc dữ liệu trong Pandas
##SERIES
ser = pd.Series([2, 4, 6, 8])
print(ser)

arr_price = np.array([76.3, 23.1, 102.4])
arr_symbol = np.array(['FPT', 'ACB', 'VNM'])
ser = pd.Series(arr_price, index=arr_symbol)
print(ser)

dic = {'FPT':76.3, 'ACB':23.1,'VNM':102.4}
ser = pd.Series(dic)
print(ser)

#Truy xuất
print(ser['ACB'])
print(ser[2])
print(ser[1:])
print(ser[['FPT', 'VNM']])

print(ser.size)
print(len(ser))

print(ser.values)

print(ser.index)

print(ser.axes)

dic = {'FPT':76.3, 'ACB':23.1, 'VNM':102.4,
 'AGH': 7.8, 'FLC':3.5, 'HTC':24.2}
ser = pd.Series(dic)
print(ser)
print(ser.head(3))
print(ser.tail(2))

print(ser.mean())
print(ser.std())
print(ser.describe())

#Cập nhập
ser['FPT'] = 81
ser[2] = 106
print(ser)

##Xóa phần tử
print(ser.drop(ser.index[[0, 2]]))
print(ser.drop(['FLC', 'AGH']))

#Tính toán số học
print(ser + 2)
print(ser.map(lambda x:x*2))

##DATAFRAME
list_sample = [['PNJ', 180.1, 182], ['VIB', 22.3, 21.2],
['VIC', 46.2, 45.6], ['VNM', 150, 146.1]]
df = pd.DataFrame(list_sample, columns=['Symbol',
'Open', 'Close'])
print(df)

#Đọc dữ liệu từ file .csv/.xlsx
import pandas as pd
df = pd.read_csv('data sample/employee.csv')
print(df)

import pandas as pd
df = pd.read_excel('data sample/Sales.xlsx')
print(df)

df = pd.read_csv('./data sample/TCB_2018_2020.csv')
print(df)

df = pd.read_csv('./data sample/TCB_2018_2020.csv', index_col=0)
print(df.head())

##Truy xuất dữ liệu theo điều kiện
df = pd.read_csv('./data sample/TCB_2018_2020.csv', index_col=0)
# Xuất dữ liệu với điều kiện giá đóng cửa lớn hơn 98
print(df[df['Close']>98])

##Truy xuất dữ liệu theo cột
print(df[["High", "Low"]].tail())

df = pd.read_csv('./data sample/TCB_2018_2020.csv', header=None)
print(df[[0, 2, 3]].tail())

##Truy xuất dữ liệu theo dòng
df = pd.read_csv('./data sample/TCB_2018_2020.csv', index_col=0)
print(df.loc['2020-06-15'])

df = pd.read_csv('./data sample/TCB_2018_2020.csv', index_col=0)
print(df.loc[['2019-06-10', '2020-06-10']])

df = pd.read_csv('./data sample/TCB_2018_2020.csv', index_col=0)
print(df.iloc[0]) # Lấy dòng đầu tiên

df = pd.read_csv('./data sample/TCB_2018_2020.csv', index_col=0)
print(df.iloc[[0, 2]]) # Lấy nhiều dòng

df = pd.read_csv('./data sample/TCB_2018_2020.csv', index_col=0)
print(df.iloc[35:41]) # Lấy nhiều dòng liên tiếp

##Truy xuất dữ liệu theo phần tử
df = pd.read_csv('./data sample/TCB_2018_2020.csv', index_col=0)
# Truy xuất giá đóng cửa ngày 20-08-2019
print(df.loc['2019-08-20', 'Close'])
print(df.loc['2020-12-25':, 'Open'])

df = pd.read_csv('./data sample/TCB_2018_2020.csv', index_col=0)
# Truy xuất dòng thứ 5 và cột đầu tiên
print(df.iloc[4, 0])
# Truy xuất dòng từ dòng thứ 648 với tất cả các cột
print(df.iloc[648:, :])

##Xóa dữ liệu
df = pd.read_csv('./data sample/SampleData.csv', index_col=0)
print(df)

del df['Price'] # Xóa cột Price
print(df)

# Xóa dòng có index là 2
print(df.drop(df.index[2]))

##Thêm dữ liệu
df = pd.read_csv('./data sample/SampleData.csv', index_col=0)
print(df)

# Thêm cột giá USD với tỷ giá 1USD = 23.000 VND
df['Usd'] = df['Price']/23
print(df)

df = pd.read_csv('./data sample/SampleData.csv')
print(df)

# Thêm dòng vào cuối df
df.loc[df.shape[0]] = ['VCB', 113.6, 23.09]
print(df)

#Sắp xếp dữ liệu
sales_2020 = pd.DataFrame({'sales': [450, 360, 550, 480]},
index=['Mar', 'Jun', 'Feb', 'Apr'])
print(sales_2020)
print(sales_2020.sort_index())

sales_2021 = pd.DataFrame({'sales': [650, 600, 700, 680]}, index=['Feb', 'Mar', 'Apr', 'Jun'])
print(sales_2020.reindex(sales_2021.index))


##Gộp dữ liệu
df = pd.read_csv('./data sample/SampleData2.csv')
df1 = df[['Symbol', 'Price', 'Group']]
df2 = df[['Symbol', 'PE', 'Group']]
print(df1)
print(df2)

df_concat = pd.concat([df1, df2])
print(df_concat)

df_concat = pd.concat([df1, df2], join='inner')
print(df_concat)

df_concat = pd.concat([df1, df2], axis=1)
print(df_concat)

df_append = df1.append(df2)
print(df_append)

df_merge = pd.merge(df1, df2)
print(df_merge)

df = pd.read_csv('./data sample/SampleData2.csv')
df1 = df[['Symbol', 'Price', 'Group']]
df1 = df1.drop(df1.index[3]) # Xóa FPT
df2 = df[['Symbol', 'PE', 'Group']]
print(df1)

df_merge = pd.merge(df1, df2)
print(df_merge)

df_merge = pd.merge(df1, df2,
how='outer')
print(df_merge)

# ##Kiểm tra dữ liệu rỗng
df = pd.read_csv('./data sample/SampleData_NaN.csv')
print(df)

df = pd.read_csv('./data sample/SampleData_NaN.csv')
print(df.isnull())

df = pd.read_csv('./data sample/SampleData_NaN.csv')
# Kiểm tra dữ liệu rỗng cho từng cột
print(df.isnull().any())

# Kiểm tra dữ liệu rỗng cho toàn bộ DataFrame
print(df.isnull().values.any())

df = pd.read_csv('./data sample/SampleData_NaN.csv')
# Kiểm tra số lượng dữ liệu rỗng cho từng cột
print(df.isnull().sum())

# Kiểm tra số lượng dữ liệu rỗng cho toàn bộ DataFrame
print(df.isnull().sum().sum())

df = pd.read_csv('./data sample/SampleData_NaN.csv')
# Xóa dòng chứa phần tử rỗng
df_delete_na_by_row = df.dropna(axis=0)
print(df_delete_na_by_row)

df = pd.read_csv('./data sample/SampleData_NaN.csv')
# Xóa cột chứa phần tử rỗng
df_delete_na_by_col = df.dropna(axis=1)
print(df_delete_na_by_col)

df = pd.read_csv('./data sample/SampleData_NaN.csv')
# Fill giá trị 100 cho phần tử rỗng
df_fill_na_100 = df.fillna(100)
print(df_fill_na_100)

df = pd.read_csv('./data sample/SampleData_NaN.csv')
# Fill phần tử rỗng với giá trị liền kề phía dưới
df_fill_na_bfill = df.fillna(method= 'bfill')
print(df_fill_na_bfill)

df = pd.read_csv('./data sample/SampleData_NaN.csv')
# Fill phần tử rỗng với giá trị liền kề phí trên
df_fill_na_ffill = df.fillna(method='ffill')
print(df_fill_na_ffill)

df = pd.read_csv('./data sample/SampleData_NaN.csv')
# Fill phần tử rỗng với giá trị nội suy
df_fill_na_interpolate = df.interpolate()
print(df_fill_na_interpolate)
