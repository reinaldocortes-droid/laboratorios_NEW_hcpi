def cal_potencia(voltage,resistance):
    if resistance <= 0:
        raise ValueError("Resistance cannot be below zero.")
    voltage = float(voltage)
    resistance = float(resistance)
    potencia = (voltage ** 2) / resistance
    return potencia


resistance = float(input("Enter the resistance (in ohms): "))
voltage = float(input("Enter the voltage (in volts): "))

resultado = cal_potencia(voltage,resistance)
print(f'The calculated power is: {resultado:.2f} watts')
print(f'The rounded power is: {round(resultado)} watts')
