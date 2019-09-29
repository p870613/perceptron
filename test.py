import random

learn_rate = 0.2
epoch = 10
data = []
sol = []
def input():
     f = open(r'dataset/perceptron1.txt')
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
                    data_x.append(int(item))
               count = count + 1
          data.append(data_x)
          sol.append(data_y)
     f.close()
     

def data_split():
     data_train = []
     sol_train = [] 
     data_test = []
     sol_test = []
     for j in range(len(data)):
          if(random.random() >= 0.3333):
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
     w = [-1]
     for i in range(len(data[0]) - 1):
          w.append(random.random())
     
     data_train = []
     data_test = []
     sol_train = []
     sol_test = []
     predict = 0
     for i in range(epoch):
          data_train, sol_train, data_test, sol_test = data_split()
          predict = 0
          c = 0
          for j in range(len(data_train)):
               sum = 0
               for k in range(len(data_train[j])):
                    sum = sum + data_train[j][k] * w[k]
               if(sum > 0):
                    predict = 1
               if(sum < 0):
                    predict = 0
                    
               if(predict != sol[j]):
                    c = c + 1
                    for k in range(len(w)):
                         w[k] = w[k] - learn_rate * data_train[j][k]
               print(w)

          count = 0
          for j in range(len(data_test)):
               sum = 0
               for k in range(len(data_test[j])):
                    sum = sum + data_test[j][k] * w[k]
               if(sum >= 0):
                    predict = 1
               if(sum < 0):
                    predict = 0
               if(predict == sol[j]):
                   count = count + 1  
                
          print(c)
          print("ac", count/len(data_test))
                                 
          #print(data_train)
          data_train = []
          data_test = []
          sol_train = []
          sol_test = []
          
          

     
     
          
if __name__ == '__main__':
     
     input()
     train()
     
    



