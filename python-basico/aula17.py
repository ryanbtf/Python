lanches = ['pizza', 'hamburguer', 'suco', 'refrigerante', 'batata frita', 'esfiha']

lanches.append('sorvete')

if 'esfiha' in lanches:
    lanches.remove('esfiha')

n = 0

while n < len(lanches):
    print(f'Eu comi {lanches[n]}')
    n += 1
print('Estou satisfeito!')

