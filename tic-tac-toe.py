field = [[' '] * 3] * 3
def show():
    print()
    print('     A   B   C   ')
    print('   -------------')
    for i, row in enumerate(field):
        print(f'{i+1}  | {" | ".join(row)} |')
        print('   -------------')
    print()
field[0][1]='x'
field[1][1]='0'
show()