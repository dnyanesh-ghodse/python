print("Welcome To Rollercoaster..!")

height = int(input("Please Enter Your Height In cm."))
bill = 0

if height >= 120:
  age = int(input("Please Enter Your Age: "))
  if age < 12:
    bill = 5
    print(f"Please Pay $5.")
  elif age <= 18:
    bill = 7
    print(f"Please Pay $7.")
  else:
    bill = 12
    print(f"Plese Pay $12.")

  want_photo = input("Do You Want Photo Y or N : ")
  if want_photo == "Y":
    bill += 3
  print(f"Your final bill is ${bill}")

else:
  print("Sorry..Height Must Be 120cm Or More")