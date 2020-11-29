print("Welcome To Treasure Island, Your mission is to find the Treasure")
choice1=input("Do you want to turn 'right' or 'left'? ").lower()
if choice1=='left':
  choice2=input("Do you want to 'swim' or 'wait'? ").lower()
  if choice2=='wait':
     choice3=input("Which door 'Red', 'Blue', or 'Yellow'? ").lower()
     if choice3=='red':
      print("Game over for red")
     elif choice3=='Blue':
      print("Game over for Blue")
     else:
      print("You win Yellow")
  else:
    print("Game over for swim")
else:
  print("Game over")