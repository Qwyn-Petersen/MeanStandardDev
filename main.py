def find_mean():
  
  print("Welcome to the mean calculator!"'\n')
  total_num = 0
  sum = 0
  switch = True
  
  # Loop through the numbers and add them to the sum
  while(switch):
    num = (float(input("To coutinue, enter a postive # or enter '-1' to stop: ")))
    if num == '':
      print("Invalid input. Please enter a valid number.")
      continue
    if num > 0: 
      sum += num
      total_num += 1 
    else:
      switch = False  
    
  # Calculate the mean and print it
  if total_num > 0:
    mean = sum / total_num
    print("The mean is: ", mean,'\n')
    return mean
  else:
    print("No numbers were entered.")
 

def find_stand_dev(mean):

  print("Welcome to the standard deviation calculator!"'\n')
  total_num = 0
  sum = 0
  switch = True

  while(switch):
    num = (float(input("To coutinue, enter a postive # or enter '-1' to stop: ")))
    if num == '':
      print("Invalid input. Please enter a valid number.")
      continue
    if num > 0:
      dev = abs((mean - num) ** 2)
      sum += dev
      total_num += 1
    else:
      switch = False

  if total_num > 0:
      standard_dev = sum / total_num
      print("The standard deviation is:", standard_dev,'\n')
      return standard_dev
  else:
      print("No numbers were entered.")
      
def main():
  mean = find_mean()
  standard_dev = find_stand_dev(mean)
  print("The mean is: ", mean)
  print("The standard deviation is:", standard_dev)
  





if __name__=="__main__":
    main()
