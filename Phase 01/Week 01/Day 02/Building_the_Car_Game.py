command = ""
started = False

while True:
  command = input("> ").lower()
  if command == "start":
    if started:
      print("Car is already started!")
    else:
      started = True
      print("Car started... Ready to go.")
  elif command == "stop":
    if not started:
      print("Car is already stopped!")
    else:
      started = False
      print("... Car stopped.")
  elif command == "help":
    print("""
      start - To start the car
      stop - to stop the car
      quit - To quit
    """)
  elif command == "quit":
    print("You are exiting the game...")
    break
  else:
    print("Sorry, I don't understand that!")