print("Description: This script will convert Celsius temp to Kelvin")

print("Enter temperature value in Celsius")
celsius_value = input()
celsius_value = float(celsius_value)
celsius_value_fahr = (celsius_value * 9/5) + 32
print(f"Kelvin value is: {celsius_value + 273}")
print("Fahrenheit value is: %.2f" %celsius_value_fahr)