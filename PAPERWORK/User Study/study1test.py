import scipy.stats as stats
from scipy.stats import shapiro
import pandas as pd
import statsmodels.stats.multicomp as mc
from scipy.stats import levene


data1 = [8.72, 8.11, 9.19, 9.57, 8.44, 8.98, 11.51, 8.99, 9.08, 10.27, 8.33, 9.01, 10.25, 10.29]
data2 = [11.32, 13.19, 14.94, 10.09, 13.56, 12.34, 13.17, 11.31, 12.44, 13.58, 11.72, 9.86, 11.02, 14.13]

data3 = [28, 31, 21, 39, 13, 24, 29, 18, 19, 22, 27, 17, 29, 11]
data4 = [37, 28, 31, 39, 21, 30 ,40, 20, 33, 32, 39, 24, 35, 22]

data5 = [87, 85, 92, 82, 89, 89, 90, 93, 88, 82, 79, 95, 71, 96]
data6 = [75, 79, 81, 68, 78, 86, 64, 82, 83, 81, 76, 80, 66, 84]

data7 = [28, 18, 27, 19, 20, 30, 29, 23, 25, 21, 15, 24, 31, 19]
data8 = [45, 34, 27, 49, 31, 38, 42, 52, 30, 26, 48, 41, 39, 36]

# import matplotlib.pyplot as plt
# plt.rcParams['font.family'] = ['Arial Unicode MS']

# # 设置每组数据及其标题
# datasets = [[(8.72, 8.11, 9.19, 9.57, 8.44, 8.98, 11.51, 8.99, 9.08, 10.27, 8.33, 9.01, 10.25, 10.29), 
#              (11.32, 13.19, 14.94, 10.09, 13.56, 12.34, 13.17, 11.31, 12.44, 13.58, 11.72, 9.86, 11.02, 14.13), 
#              '完成时间（s）'],
#             [(28, 31, 21, 39, 13, 24, 29, 18, 19, 22, 27, 17, 29, 11), 
#              (37, 28, 31, 39, 21, 30 ,40, 20, 33, 32, 39, 24, 35, 22), 
#              'SSQ'],
#             [(87, 85, 92, 82, 89, 89, 90, 93, 88, 82, 79, 95, 71, 96), 
#              (75, 79, 81, 68, 78, 86, 64, 82, 83, 81, 76, 80, 66, 84), 
#              'SUS'],
#             [(28, 18, 27, 19, 20, 30, 29, 23, 25, 21, 15, 24, 31, 19), 
#              (45, 34, 27, 49, 31, 38, 42, 52, 30, 26, 48, 41, 39, 36), 
#              'NASA-TLX']]

# # 绘图
# fig, axs = plt.subplots(1, 4, figsize=(10, 3))
# axs = axs.flatten()
# for i, (data1, data2, title) in enumerate(datasets):
#     ax = axs[i]
#     x = ['我们的方法', 'OrthoGaze']
#     y = [sum(data1)/len(data1), sum(data2)/len(data2)]
#     ax.bar(x, y, color=['black', 'grey'])
#     ax.set_title(title)
# plt.tight_layout()
# plt.show()

# stat, p = shapiro(data1)
# print('p=%.3f' % (p))
# if p > 0.05:
#     print('数据符合正态分布')
# else:
#     print('数据不符合正态分布')

# stat, p = shapiro(data2)
# print('p=%.3f' % (p))
# if p > 0.05:
#     print('数据符合正态分布')
# else:
#     print('数据不符合正态分布')

# stat, p = shapiro(data3)
# print('p=%.3f' % (p))
# if p > 0.05:
#     print('数据符合正态分布')
# else:
#     print('数据不符合正态分布')

# stat, p = shapiro(data4)
# print('p=%.3f' % (p))
# if p > 0.05:
#     print('数据符合正态分布')
# else:
#     print('数据不符合正态分布')


# stat, p = shapiro(data5)
# print('p=%.3f' % (p))
# if p > 0.05:
#     print('数据符合正态分布')
# else:
#     print('数据不符合正态分布')

# stat, p = shapiro(data6)
# print('p=%.3f' % (p))
# if p > 0.05:
#     print('数据符合正态分布')
# else:
#     print('数据不符合正态分布')

# stat, p = shapiro(data7)
# print('p=%.3f' % (p))
# if p > 0.05:
#     print('数据符合正态分布')
# else:
#     print('数据不符合正态分布')

# stat, p = shapiro(data8)
# print('p=%.3f' % (p))
# if p > 0.05:
#     print('数据符合正态分布')
# else:
#     print('数据不符合正态分布\n')

f_val, p_val = stats.f_oneway(data1, data2)

stat, p = levene(data1, data2)
print('Statistics=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print("方差齐性检验通过")
else:
    print("方差齐性检验不通过")

print("One-Way ANOVA results:")
print("F-value:", f_val)
print("P-value:", p_val)

f_val, p_val = stats.f_oneway(data3, data4)

stat, p = levene(data3, data4)
print('Statistics=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print("方差齐性检验通过")
else:
    print("方差齐性检验不通过")

print("One-Way ANOVA results:")
print("F-value:", f_val)
print("P-value:", p_val)

f_val, p_val = stats.f_oneway(data5, data6)

stat, p = levene(data5, data6)
print('Statistics=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print("方差齐性检验通过")
else:
    print("方差齐性检验不通过")

print("One-Way ANOVA results:")
print("F-value:", f_val)
print("P-value:", p_val)

f_val, p_val = stats.f_oneway(data7, data8)

stat, p = levene(data7, data8)
print('Statistics=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print("方差齐性检验通过")
else:
    print("方差齐性检验不通过")

print("One-Way ANOVA results:")
print("F-value:", f_val)
print("P-value:", p_val)