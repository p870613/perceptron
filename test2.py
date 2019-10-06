import random
import numpy as np
import matplotlib.pyplot as plt

learn_rate = 0.001
epoch = 500
data = []
sol = []
sol_class = []
best_ac = 0.0
best_w = []
pre_ac = 0.0

x = []
y = []
x2 = []
y2 = []
pre_w = []
def data_input():
     global data
     f = open(r'dataset/2CloseS3.txt')
     for line in f:
          #去換行
          line = line.replace('\n', '')

          #分割 + string to int
          sp = line.split(" ")
          data_x = [-1]
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
          
          if len(sol_class) == 0:
               sol_class.append(data_y)
          else:
               ch = True
               for item in sol_class:
                    if(item == data_y):
                         ch = False
                         break
               if(ch == True):
                    sol_class.append(data_y)
     print(sol_class)
     f.close()
     
def paint():
     
     
     print(pre_w)
     for i  in range(len(data)):
          for j in range(len(data[i])):
               
               if(sol[i] == 1):
                    x.append(data[i][1])
                    y.append(data[i][2])
               else:
                    x2.append(data[i][1])
                    y2.append(data[i][2])

     max_x = max([max(x), max(x2)])
     min_x = min([min(x), min(x2)])
     max_y = max([max(y), max(y2)])
     min_y = min([min(y), min(y2)])
     print(best_w)
     print(pre_w)
     
     plt.plot(x, y ,'r^')
     plt.plot(x2, y2 ,'gs')
     plt.plot([max_x, min_x], [(best_w[0] - best_w[1] * max_x)/best_w[2], (best_w[0] - best_w[1] * min_x)/best_w[2]] ,'y--')
     plt.plot([1,-1], [(best_w[0] - best_w[1] * 1)/best_w[2], (best_w[0] - best_w[1] * -1)/best_w[2]] ,'y--')
     #plt.plot([max_x, min_x], [(pre_w[0] - pre_w[1] * max_x)/pre_w[2], (pre_w[0] - pre_w[1] * min_x)/pre_w[2]] ,'b-')
     #plt.xlim((min_x, max_x))
     #$plt.ylim((min_y, max_y))
     plt.show()
     
def data_split():
     data_train = []
     sol_train = [] 
     data_test = []
     sol_test = []
     for j in range(len(data)):
          if(random.random() >= 0.33):
               data_train.append(data[j])
               sol_train.append(sol[j])
          else:
               data_test.append(data[j])
               sol_test.append(sol[j])
                    
          if(len(data_test) == 0):
               ran = random.randint(0, len(data_train)-1)
               data_test.append(data_train[ran])
               sol_test.append(sol[j])
               del data_train[ran]
               del sol_train[ran]

     return data_train, sol_train, data_test, sol_test

def train():
     global best_ac
     global pre_ac
     global best_w
     global pre_w
     global data
     w = [-1,0, 1]
     #for i in range(len(data[0]) - 1):
      #    w.append(random.random())
     pre_w = w
     #plt.plot([-20, 6], [(pre_w[0] - pre_w[1] * -20)/pre_w[2], (pre_w[0] - pre_w[1] *6)/pre_w[2]] ,'b-')
     data_train = []
     data_test = []
     sol_train = []
     sol_test = []
     predict = 0
     data_train, sol_train, data_test, sol_test = data_split()
     for i in range(epoch):
          
          predict = 0
          for j in range(len(data)):
               sum = 0
               for k in range(len(data)):
                    sum = sum + data[j][k] * w[k]
               if(sum >= 0):
                    predict = sol_class[0]
                    if(predict != sol[j]):
                         for k in range(len(w)):
                              w[k] = w[k] - learn_rate * data[j][k]
               if(sum < 0):
                    predict = sol_class[1]
                    if(predict != sol[j]):
                         for k in range(len(w)):
                              w[k] = w[k] + learn_rate * data[j][k]
                    
               
               #print(w)

          count = 0
          for j in range(len(data_test)):
               sum = 0
               for k in range(len(data_test[j])):
                    sum = sum + data_test[j][k] * w[k]
               if(sum >= 0):
                    predict = sol_class[0]
               if(sum < 0):
                    predict = sol_class[1]
               if(predict == sol[j]):
                   count = count + 1  
          ac = count/len(data_test)
          
          if(best_ac < ac):
               best_ac = ac
               best_w = w
          
          pre_ac = ac     
          print("ac", ac)
          
          

          count = 0
          for j in range(len(data)):
               sum = 0
               for k in range(len(data[j])):
                    sum = sum + data[j][k] * w[k]
               if(sum >= 0.5):
                    predict = sol_class[0]
               if(sum < 0.5):
                    predict = sol_class[1]
               if(predict == sol[j]):
                   count = count + 1  
                
          
          print("total_ac", count/len(data))
          #print(best_w)
          #print(data_train)
          #data_train = []
          #data_test = []
          #sol_train = []
          #sol_test = []
          
          

         
if __name__ == '__main__':
     #learn_rate = float(input("學習率: "))
     data_input()
     train()
     print(pre_w)
     paint()
     
    



