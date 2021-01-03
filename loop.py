import time
from colorama import init, Fore, Back
while True:
    loopQuestion = input(f"{Fore.BLACK+Back.WHITE}run again? [Y/N]: {Fore.RESET+Back.RESET}")
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