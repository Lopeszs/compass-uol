def valor(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(f'{value}')

valor(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)