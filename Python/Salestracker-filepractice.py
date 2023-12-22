from os import close

def menu():
  print("""Welcome to the Sales Tracker!
Enter the following details for each sale:""")
menu()

def main():
  itemf = []
  quanf = []
  salef = [] 

  ans = True
  
  while ans:
    item = input("Enter the item name:")
    itemf.append(item)
    quan = int(input("Enter the quantity sold:"))
    quanf.append(quan)
    sale = float(input("Enter the sale amount:"))
    salef.append(sale)
    con = input("Would you like to enter another set of sales?(Yes or No):")
    if con == 'Yes':
      ans = True 
    elif con == 'No':
      ans = False
      with open("sales.txt","w") as file:
        for it, qua, sal in zip(itemf, quanf, salef):
          L = [it, str(qua), str(sal)]
          for l in L:  
            file.write(l + "\n") 
        
        # file.write("Sales Entered Today:"+ "/n")
        # file.write("Items in order:" + str(itemv) + "/n")
        # file.write("Quantities in order:" + str(quanv) + "/n")
        # file.write("Sale amount in order:"+ str(salev) + "/n")
      file.close()
      print("Thank you for entering sales. Check sales.txt for accuracy!")
      break
      
main()
  
  
  
