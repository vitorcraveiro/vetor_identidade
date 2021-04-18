#trabalhando com normalização de imagens 
 
#criando a matriz
n_coluna= int(input("numero de colunas: "))
n_linha= int(input("numero de linhas: "))

matriz=[]

v =1 
for i in range(n_linha):
    linha=[]
    for j in range(n_coluna):
        x= int(input(" escolha um numero: "))
        linha.append(x)
    matriz.append(linha)
    
    
#imprimindo a matriz
for l in matriz: 
    print(l)


#imprimindo cada valor da matriz 
for i in range(n_linha):
    for j in range(n_coluna):
        valor = matriz[i][j]
       
        
#normatização por cores 
valor_maximo_matriz = 0              #achando o maior valor da matriz
for i in range(n_linha):             #percorre a linha da matriz
    for j in range(n_coluna):        #percorre a coluna da matriz 
        numero = matriz[i][j]        
        if numero > valor_maximo_matriz:  #técnica para retirar o maior valor da matriz
            valor_maximo_matriz = numero 
        else: 
            valor_maximo_matriz = valor_maximo_matriz

     
#criando um vetor de caracteristicas           
vetor_caracteristica = [0] * (valor_maximo_matriz + 1 )

valor_auxiliar = valor_maximo_matriz +1 

for x in matriz:
    for y in x: 
        for indice in range(0,valor_auxiliar):
            if(y== indice): 
                vetor_caracteristica[indice]+= 1 
    
print(vetor_caracteristica)
