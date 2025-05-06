import time

def display_cake(candles):
    print("\n" + "🎂" + " " * (candles + 1) + "🎂")
    print(" " * (candles + 1) + " " + "🎉" * candles)
    print(" " * (candles + 1) + " " + "🎈" * candles)
    print("\n" + " " * (candles + 1) + "Happy Birthday!")
    print("\n" + " " * (candles + 1) + "You have " + str(candles) + " candles to blow out!")
    
def blow_out_candle(candles):
    for i in range(candles, 0, -1):
        print(f"\nBlowing out candle {i}...")
        time.sleep(1)  # Simulate time taken to blow out each candle
    print("\nAll candles are blown out! 🎉")

def birthday_wish():
    wish = input("\nMake a wish: ")
    print(f"\nYou wished: '{wish}' 🎈")
    print("May your wish come true!")

def main():
    print("Welcome to the Interactive Birthday Cake!")
    candles = int(input("How many candles are on the cake? "))
    
    display_cake(candles)
    
    blow_out = input("\nDo you want to blow out the candles? (yes/no): ").strip().lower()
    if blow_out == 'yes':
        blow_out_candle(candles)
    else:
        print("\nYou decided to leave the candles unblown. Enjoy your cake! 🎂")
    
    birthday_wish()
    print("\nThank you for celebrating with us! 🎉")

if __name__ == "__main__":
    main()