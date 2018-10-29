import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#打开点云数据文件
f=open('reconstruction.txt','r')
point=f.read()
f.close()
#数据预处理
l1=point.replace('\n',',')
#将数据以“，”进行分割
l2=l1.split(',')
l2.pop()
#print(l2)
#将数据转为矩阵
m1=np.array(l2[0:327])
print(m1)
#变形
m2=m1.reshape(109,3)
print(m2)
m3=[]
for each in m2:
	each_line=list(map(lambda x:float(x),each))
	m3.append(each_line)
m4=np.array(m3)
#列表解析x,y,z的坐标
x=[k[0] for k in m4]
y=[k[1] for k in m4]
z=[k[2] for k in m4]
#开始绘图
fig=plt.figure(dpi=120)
ax=fig.add_subplot(111,projection='3d')
#标题
plt.title('point cloud')
#利用xyz的值，生成每个点的相应坐标（x,y,z）
ax.scatter(x,y,z,c='b',marker='.',s=2,linewidth=0,alpha=1,cmap='spectral')
ax.axis('scaled')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
#显示
plt.show()