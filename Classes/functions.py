def pcn(n1, n2):
    return n1.capitalize() + n2.capitalize()
def cn(n1, n2):
    return n1.capitalize() + ' ' + n2.capitalize()


name = pcn('gito', 'ditrium')
full_name = cn('ezio', 'auditore')

print(f"{name} played as {full_name} in AC revelations")