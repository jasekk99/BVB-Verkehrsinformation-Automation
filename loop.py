import time
from colorama import init, Fore, Back
while True:
    loopQuestion = input(f"{Fore.BLACK+Back.WHITE}run again? [Y/N]: {Fore.RESET+Back.RESET}")
    if loopQuestion == "Y" or loopQuestion == "y" or loopQuestion == "yes":
        print("OK! Running the Application")
        import bvb_updates
        # wait 1 hour then continue
        time.sleep(1200)
        continue
    if loopQuestion == "N" or loopQuestion == "n" or loopQuestion == "no":
        print("OK! Exiting loop")
        break
    break