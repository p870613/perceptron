import random
import numpy as np
import matplotlib.pyplot as plt

#參數
learn_rate = 0.2
epoch = 100
accuracy = 0.9

#input data
data = []
sol = []
sol_class = []

#store final solution
best_ac = 0.0
best_w = []
final_ac = 0.0


def data_input():
     #read file
     f = open(r'dataset/2Hcircle1.txt')
     
     for line in f:
          #repace '\n' to ''
          line = line.replace('\n', '')
          #split and string to int
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

          #process different class
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
     f.close()
     
def paint(data, sol):
     x = []
     y = []
     x2 = []
     y2 = []
     for i  in range(len(data)):
          for j in range(len(data[i])):
               
               if(sol[i] == 1):
                    x.append(data[i][1])
                    y.append(data[i][2])
               else:
                    x2.append(data[i][1])
                    y2.append(data[i][2])
     max_x = 0
     min_x = 0

     if(len(x) != 0 and len(x2)!= 0):
          max_x = max([max(x), max(x2)])
          min_x = min([min(x), min(x2)])
     elif(len(x) != 0):

          max_x = max(x)
          min_x = min(x)
     elif(len(x2)!= 0):
          max_x = max(x2)
          min_x = min(x2)
    
     plt.plot(x, y ,'r^')
     plt.plot(x2, y2 ,'gs')
     plt.plot([max_x, min_x], [(best_w[0] - best_w[1] * max_x)/best_w[2], (best_w[0] - best_w[1] * min_x)/best_w[2]] ,'y--')
     plt.show()


def data_split():
     data_train = []
     sol_train = [] 
     data_test = []
     sol_test = []
     #use random() 
     for j in range(len(data)):
          if(random.random() >= 0.33):
               data_train.append(data[j])
               sol_train.append(sol[j])
          else:
               data_test.append(data[j])
               sol_test.append(sol[j])
               
          #防止data_test沒有資料                     
          if(len(data_test) == 0):
               ran = random.randint(0, len(data_train)-1)
               data_test.append(data_train[ran])
               sol_test.append(sol[j])
               del data_train[ran]
               del sol_train[ran]

     return data_train, sol_train, data_test, sol_test


     
def train():
     global best_ac
     global best_w 
     global accuracy
     global final_ac
     
     #初始weight
     w = [-1,0, 1]
     data_train = []
     data_test = []
     sol_train = []
     sol_test = []
     predict = 0

     pre_ac = 0
     pre_w = []
     data_train, sol_train, data_test, sol_test = data_split()

     
     #start train
     for i in range(epoch):     
          predict = 0
          for j in range(len(data_train)):
               sum = 0
               for k in range(len(data_train[j])):
                    sum = sum + data_train[j][k] * w[k]
               #print(sol_train)
              
               if(sum >= 0):
                    predict = sol_class[0]
                    if(predict != sol_train[j]):
                         for k in range(len(w)):
                              w[k] = w[k] - (learn_rate)/(1+i/10) * data_train[j][k]
               if(sum < 0):
                    predict = sol_class[1]
                    if(predict != sol_train[j]):
                         for k in range(len(w)):
                              w[k] = w[k] + (learn_rate)/(1+i/10) * data_train[j][k]
              
                    
          #evalute
          count = 0
          for j in range(len(data_test)):
               sum = 0
               for k in range(len(data_test[j])):
                    sum = sum + data_test[j][k] * w[k]
               
               if(sum >= 0):
                    predict = sol_class[0]
               if(sum < 0):
                    predict = sol_class[1]
               if(predict == sol_test[j]):
                    count = count + 1
          ac = count/len(data_test)
          
          if(pre_ac > ac):
               w = pre_w
               ac = pre_ac
          else:
               pre_ac = ac
               pre_w = w
               
          #record best accuracy
          if(best_ac < ac):
               best_ac = ac
               best_w = w
          
          
  
          print("epoch: " + str(i+1) + "\naccuracy:", str(ac))
          
          count = 0
          for j in range(len(data)):
               sum = 0
               for k in range(len(data[j])):
                    sum = sum + data[j][k] * w[k]
               
               
               if(sum >= 0):
                    predict = sol_class[0]
               if(sum < 0):
                    predict = sol_class[1]
               if(predict == sol[j]):
                    count = count + 1
               
          final_ac = count/len(data)
          print("total_accuracy", final_ac)
          if(best_ac >= accuracy):  
               return  
          
     paint(data_train, sol_train)
         
          
if __name__ == '__main__':
     
     c1 = False
     c2 = False
     c3 = False
     while(True):
          if(c1 == False):
               try:
                    learn_rate = float(input("學習率: "))
                    c1 = True
               except:
                    print("學習率輸入錯誤")

          if(c2 == False):
               try:
                    epoch = int(input("請輸入正整數 epoch: "))
                    c2 = True
               except:
                    print("epoch輸入錯誤")

          if(c3 == False):
               try:
                    accuracy = float(input("請輸入符點數 accuracy: "))
                    c3 = True
               except:
                    print("accuracy輸入錯誤")

          if(c1 == True and c2 == True and c3 == True):
               break
     data_input()
     train()
     
     
     print("利用test data最後的accuracy: " + str(best_ac),)
     print("利用test data最後的: ", end = "")
     print(best_w)

     print("利用全部 data最後的accuracy: ", final_ac)

     paint(data, sol)
     
     

     
    



