def find_mean():
  
  print("Welcome to the mean calculator!"'\n')
  # Set a variable for the total amount of numbers
  total_num = 0
  # Initialize the sum to 0
  sum = 0
  # Initialize a bool for the while loop
  switch = True
  # Loop through the numbers and add them to the sum
  
  while(switch):
    num = (float(input("To coutinue, enter a postive # or enter '-1' to stop: ")))
    if num > 0: 
      sum += num
      total_num += 1 
    else:
      switch = False  
    
  # Calculate the mean and print it
  if total_num > 0:
    mean = sum / total_num
    print("The mean is:", mean)
  else:
    print("No numbers were entered.")

def find_stand_dev():
  # Get the number of numbers to be averaged
  int(input("How many numbers do want to use? "))
  







def main():
  find_mean()
  
  










if __name__=="__main__":
    main()
