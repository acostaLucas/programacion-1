import sys

def calcularFactura(mtsConsumidos, tipoCliente):
    consFijo = 7000
    consM3 = 200
    iva = 21
    subtotal = 0
    bonificacion = 0
    recargo = 0
    subtotalBR = 0
    total = 0

    subtotal += (consFijo + (mtsConsumidos * consM3))

    if tipoCliente.upper() == "RESIDENCIAL":
        if mtsConsumidos < 30:
            bonificacion += ((subtotal * 10)/100) 
        elif mtsConsumidos > 80:
            recargo += ((subtotal * 15)/100)

    elif tipoCliente.upper() == "COMERCIAL":
        if mtsConsumidos < 50:
            recargo += ((subtotal * 5)/100)
        elif mtsConsumidos > 150:
            if mtsConsumidos < 299:
                bonificacion += ((subtotal * 8)/100) 
            else: 
                bonificacion += ((subtotal * 8)/100)

    elif tipoCliente.upper() == "INDUSTRIAL":
        if mtsConsumidos < 200:
            recargo += ((subtotal * 10)/100)
        elif mtsConsumidos > 500:
            if mtsConsumidos > 1000: 
                bonificacion += ((subtotal * 30)/100)
            else:
                bonificacion += ((subtotal * 20)/100)
    
    if recargo != 0:
        subtotalBR += recargo
    elif bonificacion != 0:
        subtotalBR -= bonificacion

    subtotal += subtotalBR
    iva += ((subtotal * 21)/100)

    total = subtotal + iva

    if tipoCliente.upper() == "RESIDENCIAL" and bonificacion == 0 and recargo == 0 and total == 35000:
        total -= ((total * 5)/100)

    factura = {
        "Subtotal": subtotal,
        "Bonificacion": bonificacion,
        "Recargo": recargo,
        "Subtotal Bonif / Recargo": subtotalBR,
        "IVA": iva,
        "Total": total
    }

    for nombre, valor in factura.items():
        print(f"{nombre}: $ {valor}")

mtsConsumido = input("Ingresá la cantidad consumida de agua (en m3): ")
cliente = input("Ingresá que tipo de cliente sos (Residencial, Comercial o Industrial): ")

try:
    mtsConsumido = float(mtsConsumido)

    if cliente.upper() != "RESIDENCIAL" and cliente.upper() != "COMERCIAL" and cliente.upper() != "INDUSTRIAL":
        print("El tipo de cliente es inválido, por favor ingresá un cliente válido: Residencial, Comercial o Industrial")
    elif mtsConsumido is None and cliente is None:
        print("Ingresá datos válidos")
    else:
        calcularFactura(mtsConsumido, cliente)
except ValueError:
    print("Ingreso del consumo de agua inválido.")
    sys.exit(1)