def descida(x, tol, n, funcao, gradiente):
    # Definição da função objetivo
    def f(x):  
        return eval(funcao)
    # Definicao do gradiente da função objetivo g(x)
    def g(x):
        return eval(gradiente)

    
funcao    = input("Insira a Função objetivo 'f(x1,x2)':")
gradiente = input("Insira o Gradiente da Função objetivo 'g(x1,x2)':")