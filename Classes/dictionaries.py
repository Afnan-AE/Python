at = {'Evan': 16,
      'Ashfaq': 15,
      'Abir': 16,
      'Zafar Sir': 22}

at.update({'Esam': 9})

a = at.keys()
b = at.values()
c = at.items()

at.pop('Abir')
print(at.get('Abir'))
print(at.get('Zafar Sir'))
for i, k in c:
    print(f"Key: {i} for {k}")