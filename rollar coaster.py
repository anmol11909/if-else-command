#if /elif/else
print("welcome to the rollar coaster")
height = int(input("what is your height"))
if height>=130:
  print("Congratulations you can ride")
  age = int(input("What is your age"))
  if age<12:
    print("You have to pay $5")
  elif age <= 18:
    print("You have to pay $10")
  else:
    print("You have to pay $15")
else:
  print("sorry you are not tall enough for this ride, you can go for some other ride")
