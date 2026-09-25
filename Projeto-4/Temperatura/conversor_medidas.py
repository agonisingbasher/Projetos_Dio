def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("--- Conversor de Temperatura ---")
temp_c = float(input("Digite a temperatura em graus Celsius: "))
temp_f = celsius_para_fahrenheit(temp_c)
print(f"{temp_c}°C equivale a {temp_f:.2f}°F")
