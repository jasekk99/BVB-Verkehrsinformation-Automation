import time
while True:
    loopQuestion = input("run again? [Y/N]: ")
    if loopQuestion == "Y":
        print("OK! Running the Application")
        import bvb_updates
        # wait 1 hour then continue
        time.sleep(1200)
        continue
    if loopQuestion == "N":
        print("OK! Exiting loop")
        break
    break