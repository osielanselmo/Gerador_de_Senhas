import string as st
import numpy as np

def gerar_senha(tamanho=10, usar_letras=True, usar_numeros=True, usar_caracteres_especiais=True):
    # Conjuntos de caracteres
    let = st.ascii_letters if usar_letras else ''
    num = st.digits if usar_numeros else ''
    esp = st.punctuation if usar_caracteres_especiais else ''
    
    tudo = let + num + esp
    
    senha = np.random.choice( list(tudo), 10)
    
    
    
    if not all:
        raise ValueError("Você deve permitir ao menos 1 tipo de  caractere para gerar a senha.")
    
    senha = np.random.choice( list(tudo), tamanho)
    
    return ''.join(senha) 

tamanho = int(input('Digite o tamanho da Senha: '))
usar_letras = (input('Usar Letras? (s/n)')).lower() =='s'
usar_numeros = (input('Usar Numeros?(s/n)')).lower() =='s'
usar_caracteres_especiais = (input('Usar Caracteres Especiais?')).lower() == 's'

senha = gerar_senha(tamanho, usar_letras, usar_numeros, usar_caracteres_especiais)

print(f'Senha gerada: {senha}')







