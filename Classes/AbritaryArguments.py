def sa(*a, **k):
    for i in a:
        print(i, end=' ')
    print()
    if 'apt' and 'pobox' in k:
        print(f"{k.get('street')} {k.get('apt')} {k.get('pobox')}")
    elif 'apt' in k:
        print(f"{k.get('street')} {k.get('apt')}")
    elif 'pobox' in k:
        print(f"{k.get('street')} {k.get('pobox')}")
    else:
        print(f"{k.get('street')}")

    print(f"{k.get('area')} {k.get('state')} {k.get('city')}")

sa('Zafar', 'A.', 'Saleh',
   street='Parlour Goli',
   apt='123 456 789',
   pobox='3(#)3',
   area='60 feet',
   state='Monipur',
   city='Dhaka')