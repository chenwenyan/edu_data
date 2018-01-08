import matplotlib.pyplot as plt
import numpy as np
val_ls = [np.random.randint(100) + i*20 for i in range(7)]
scale_ls = range(7)
index_ls = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
plt.bar(scale_ls, val_ls)
plt.xticks(scale_ls,index_ls)  ## 可以设置坐标字
plt.title('Average customer flows Number by Weekdays')