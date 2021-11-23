# ocr land

personCount = 0

while personCount < 8:

  height = int(input("enter height: "))

  if height > 140:
    print("ur allowed on this ride.")
    personCount = personCount + 1

  elif height < 140 and height > 120:

    withParent = input("Are you with a parent?: ")

  if withParent.lower() == "yes":
    print("GO AWAY NOT ALLOWD RIP BOZO")
  personCount = personCount + 2
    else:
      print("NOT ALLOWED")

  else:
  print("nto allwod plus ratio")

print("This ride is full.)
