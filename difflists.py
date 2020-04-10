n=(int(input("Enter number of elements you want to add:")))
list1 = []
list2 = []
list3 = []
i=0
l=(int(input("Enter which of the 3 lists you want to add element to:")))

   
for i in range(0,n):
  if l == 1:
      ele1=(int(input("Enter element to be added to list 1:")))
      list1.append(ele1)
    
  elif l == 2:
      ele2=(int(input("Enter element to be added to list 2:")))
      list2.append(ele2)
    
  elif l == 3:
      ele3=(int(input("Enter element to be added to list 3:")))
      list1.append(ele1)
    
  else:
      print("List not available")


print(list1)
print(list2)
print(list3)
               
