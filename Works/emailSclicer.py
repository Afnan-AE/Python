e = input('Gmail: ')

print(f'Your username {e[:e.index("@")]} and domain {e[e.index("@")+1:]}')