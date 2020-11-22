s = float(input())

if s >= 0 and s <= 400.00 :
    new_s = s * 0.15 +s
    earn = new_s -s
    print("Novo salario: %.2f" %(new_s))
    print("Reajuste ganho: %.2f" %(abs(earn)))
    print("Em percentual: %d %s" %(15 , "%"))

if s >= 400.01 and s <= 800.00 :
    new_s = s * 0.12 +s
    earn = new_s -s
    print("Novo salario: %.2f" %(new_s))
    print("Reajuste ganho: %.2f" %(abs(earn)))
    print("Em percentual: %d %s" %(12 , "%"))

if s >= 800.01 and s <= 1200.00 :
    new_s = s * 0.10 +s
    earn = new_s -s
    print("Novo salario: %.2f" %(new_s))
    print("Reajuste ganho: %.2f" %(abs(earn)))
    print("Em percentual: %d %s" %(10 , "%"))

if s >= 1200.01 and s <= 2000.00 :
    new_s = s * 0.07 +s
    earn = new_s -s
    print("Novo salario: %.2f" %(new_s))
    print("Reajuste ganho: %.2f" %(abs(earn)))
    print("Em percentual: %d %s" %(7 , "%"))

if s > 2000.00  :
    new_s = s * 0.04 +s
    earn = new_s -s
    print("Novo salario: %.2f" %(new_s))
    print("Reajuste ganho: %.2f" %(abs(earn)))
    print("Em percentual: %d %s" %(4 , "%"))
