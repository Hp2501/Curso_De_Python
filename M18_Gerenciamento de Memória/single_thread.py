import time
from threading import Thread


CONTADOR = 50000000

# Usando o single-thread (padrão do Python)


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')
