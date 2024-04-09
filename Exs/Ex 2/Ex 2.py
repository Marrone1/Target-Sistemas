resposta = int(input("Digite um número: "))

def fibonacci(resposta):
    a = 0
    b = 1
    while a <= resposta:
        if resposta == a:
            return True
        a, b = b, a + b
    return False


    
x = fibonacci(resposta)
if x == True:
    print("Pertence")
elif x == False:
    print("Não pertence")