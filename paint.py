import numpy as np
import matplotlib.pyplot as plt
 

x = []
y = []
x2 = []
y2 = []
data = []
sol = []
def paint():
     for i  in range(len(data)):
          for j in range(len(data[i])):
               if(sol[i] == 1):
                    x.append(data[i][0])
                    y.append(data[i][1])
               else:
                    x2.append(data[i][0])
                    y2.append(data[i][1])
     plt.plot(x, y ,'r^')
     plt.plot(x2, y2 ,'gs')
     plt.show()
def data_input():
     f = open(r'dataset/2ring.txt')
     for line in f:
          #去換行
          line = line.replace('\n', '')

          #分割 + string to int
          sp = line.split(" ")
          data_x = []
          data_y = 0
          count = 0
          for item in sp:               
               if(count == (len(sp)-1)):
                    data_y = int(item)
               else:
                    data_x.append(float(item))
               count = count + 1
               
          data.append(data_x)
          sol.append(data_y)
          
          
# red dashes, blue squares and green triangles
data_input()
for i  in range(len(data)):
     for j in range(len(data[i])):
          if(sol[i] == 1):
               x.append(data[i][0])
               y.append(data[i][1])
          else:
               x2.append(data[i][0])
               y2.append(data[i][1])


data_input()
paint()
