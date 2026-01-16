import sys

def temperature(n):
    if n < 40:
        return "Cold"
    elif n == 40:
        return "Normal"
    else:
        return "Hot"

if __name__ == "__main__":
    try:
        n = float(sys.argv[1])
    except IndexError:
        n = float(input("Enter the temperature: "))
    except ValueError:
        print("Enter a valid temperature")
        sys.exit()

    result = temperature(n)
    print(f"Entered temperature is: {n}")
    print(f"Weather condition is: {result}")
