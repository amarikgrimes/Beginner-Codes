def menu():
  print("""Welcome to the Sales Tracker!
  Enter the following details for each sale:""")

def main():
  itemf = []
  quanf = []
  salef = []
  def iteml():
      for item in itemf:
          print(item)

  def quanl():
      for quan in quanf:
          print(quan)

  def salel():
      for sale in salef:
          print(sale)

  menu()
  while True:
      item = input("Enter the item name: ")
      itemf.append(item)
      quan = int(input("Enter the quantity sold: "))
      quanf.append(quan)
      sale = float(input("Enter the sale amount: "))
      salef.append(sale)
      con = input("Would you like to enter another set of sales? (Yes or No): ")
      if con.lower() == 'yes':
          continue
      elif con.lower() == 'no':
          with open("sales.txt", "w") as file:
              file.write("Sales Entered Today:\n")
              file.write("Items in order: " + str(itemf) + "\n")
              file.write("Quantities in order: " + str(quanf) + "\n")
              file.write("Sale amount in order: " + str(salef) + "\n")
          print("Thank you for entering sales. Check sales.txt for accuracy!")
          break

if __name__ == "__main__":
  main()
