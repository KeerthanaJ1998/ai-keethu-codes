list = [] 
n = int(input("Enter number of elements : ")) 

for i in range(0, n):
    num = int(input())
    if num>0:
      list.append(num)
      i+=1
    else:
      i+=1
 
print(list)



