serial1 , num1 , unit_price1 = map( float , (input().split()))
serial2 , num2 , unit_price2 = map( float , (input().split()))

print("VALOR A PAGAR: R$ %.2f"  %((num1*unit_price1) + (num2*unit_price2)))

