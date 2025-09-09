
# Desafio condicionales

m_consumidos = int(input('Ingrese los metros consumidos:'))
tipo_cliente = input('Ingrese el tipo de cliente (Residencial, Comercial o Industrial):').lower()

subtotal_consumo = (200 * m_consumidos) + 7000
bonificacion = 0
recargo = 0

match tipo_cliente:
    case 'residencial':
        if m_consumidos < 30:
            bonificacion = 0.1
        elif m_consumidos > 80:
            recargo = 0.15
    
    case 'comercial':
        if m_consumidos > 150:
            bonificacion = 0.08
            if m_consumidos > 300:
                bonificacion += 0.12
        elif m_consumidos < 50:
            recargo = 0.05
    
    case 'industrial':
        if m_consumidos > 500:
            bonificacion = 0.2
            if m_consumidos > 1000:
                bonificacion += 0.3
        elif m_consumidos < 200:
            recargo = 0.1



if tipo_cliente == 'residencial' and subtotal_consumo < 35000:
    bonificacion += 0.05

descuento_aplicado = subtotal_consumo * bonificacion
recargo_aplicado = subtotal_consumo * recargo

subtotal = subtotal_consumo + recargo_aplicado - descuento_aplicado

monto_final = (subtotal_consumo * 0.21) + subtotal_consumo

print(f'''
Metros consumidos: {m_consumidos}
Subtotal de consumo: ${subtotal_consumo}
Descuento: {bonificacion}% Aplicado: ${descuento_aplicado}
Recargo: {recargo}% Aplicado: ${recargo_aplicado}
Subtotal con descuento y recargos aplicados: ${subtotal:.0f}
IVA aplicado: 21%
Monto final: ${monto_final:.0f}
''')
    