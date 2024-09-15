class Calculo:
    
    def soma(self, x, y):
        return print(f'Somando: {x}+{y} = {x + y}')
    
    def subtracao(self, x, y):
        return print(f'Subtraindo: {x}-{y} = {x - y}')

x = 4 
y = 5

c = Calculo()

c.soma(x, y)
c.subtracao(x, y)    