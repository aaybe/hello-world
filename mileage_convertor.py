#Takes kilometers and converts to miles
km_to_convert = float(input("This calculator converts kilometers to miles.\nEnter the number of km you would like to convert to mi: "))

#1 mile in kilometers
one_km = .621371

#conversion
result = km_to_convert / one_km

#round to 2 decimal place
result = round(result, 2)

#print result
print(f"{km_to_convert} km is {result} mi")

