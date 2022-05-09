import utils as u
import algorithms as alg

def help():
    print("\nPython Algorithm Switcher:")
    print(" 1 - The Middle Average Algorithm.")
    print(" 2 - The Longest Dry Spell Algorithm.")
    print(" 3 - The Number to Words Algorithm.")
    print(" 4 - The File Encryption Algorithm.")
    print(" 5 - The IPv4 to Binary Algorithm.")
    print(" 6 - The Binary Search Algorithm.")
    print(" 7 - The Stretch of 2-Vowels Algorithm.")
    print(" 8 - The Shapes Algorithm.")
    print(" 9 - The Cities Statistics Algorithm.")
    print("10 - The Satellite Orbital Speed Algorithm.")
    
    
def switcher(choice):
    if choice == "1":
        alg.middleaverage()
    elif choice == "2":
        alg.longestdryspell()
    elif choice == "3":
        alg.numbertoword()
    elif choice == "4":
        alg.fileencryption()
    elif choice == "5":
        alg.networking()
    elif choice == "6":
        alg.binarySearch()
    elif choice == "7":
        alg.matches()
    elif choice == "8":
        alg.shapes()
    elif choice == "9":
        alg.citiesstatistics()
    elif choice == "10":
        alg.satellitespeed()
    else:
        help()
    
def run():
    help()
    choice = u.read("Algorithm [1-10] or (x - exit): ")
    while choice != "x":
        switcher(choice)
        help()
        choice = u.read("Algorithm [1-10] or (x - exit): ")
    print("\nThank You and hope you enjoyed Python!\n")
    
run()