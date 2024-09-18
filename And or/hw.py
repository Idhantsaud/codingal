temp = int(input("Enter the temperature in celcius: ")) 
if temp > 0 and temp < 5:
    print("Wear something warm today it's very cold ")
elif temp > 5  and temp < 15:
    print("It's still cold but you might not need a big jacket")
elif temp > 15 and temp < 25:
    print("It's not very cold but you might need a light jacket")
elif temp > 25 and temp < 30:
    print("Very warm today wear something light")
else:
    print("Go for a swim it's too hot today")