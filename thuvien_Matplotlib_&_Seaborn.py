import matplotlib.pyplot as plt
import pandas as pd
##Thiết lập thông số cấu hình chung cho biểu đồ
plt.rcParams['figure.figsize'] = (10,8)
plt.rcParams['figure.dpi'] = 200
plt.rcParams['font.size'] = 13
# plt.rcParams['savefig.dpi'] = 200
# plt.rcParams['legend.fontsize'] = 'large'
# plt.rcParams['figure.titlesize'] = 'medium'
# plt.rcParams["legend.loc"] = 'best'

##Biểu đồ đường
df = pd.read_csv('./data sample/NetProfit.csv')
dat = df[['Year', 'VIC']]
print(dat)

plt.plot('Year', 'VIC', data=dat)
plt.show()

df = pd.read_csv('./data sample/NetProfit.csv')
plt.plot('Year', 'VNM', data=df)
plt.plot('Year', 'PNJ', data=df)
plt.plot('Year', 'VCB', data=df)
plt.plot('Year', 'VIC', data=df)
plt.show()

plt.plot('Year', 'VNM', data=df, color='b', linestyle= '-', marker='o')
plt.plot('Year', 'PNJ', data=df, color='g', linestyle= '--', marker='s')
plt.plot('Year', 'VCB', data=df, color='#FF0000', linestyle=':', marker='+')
plt.plot('Year', 'VIC', data=df, color='orange', linestyle= '-.', marker='*')
plt.title("Lợi nhuận của VNM, PNJ, VCB, VIC từ 2010 đến 2020", fontweight='bold')
plt.xlabel("Năm", fontweight='bold')
plt.ylabel("Lợi nhuận", fontweight='bold')
plt.legend()
plt.show()


##Biểu đồ cột
df = pd.read_csv('./data sample/PVD_Asset.csv')
print(df)

plt.bar('Year', 'Liabilities', data=df)
plt.title("Nợ của PVD qua các năm")
plt.xlabel("Năm")
plt.ylabel("Nợ")
plt.show()

plt.barh('Year', 'Equity', data=df)
plt.title("Vốn của PVD qua các năm")
plt.xlabel("Vốn")
plt.ylabel("Năm")
plt.show()

plt.bar('Year', 'Liabilities', data=df, color= 'orange', label="Nợ")
plt.bar('Year', 'Equity', data=df, bottom='Liabilities', color= 'darkgreen', label="Vốn")
plt.title("Tài sản của PVD từ 2010-2020")
plt.xlabel("Năm")
plt.ylabel("Tỷ đồng")
plt.legend()
plt.show()