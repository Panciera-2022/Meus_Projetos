"""
********COMANDOS**********
control + /  =  comenta toda area selecionada
control + /  novamente na mesma area descomentar o que estava comentado.
shift + tab = move toda estrutura pra esquerda
tab = move tudo pra direita
+=     - quer dizer concatenar ou seja juntar adicionar algo.
[] = lista
{} = dicionário
if = se
else = senão
elif = junção do if + else
for = laço melhor quando não se sabe o fim
while = laço melhor quando se sabe o fim
or = (ou) usado para não precisar colocar vários if
def =
control + espaço  = mostra todos os comandos das bibliotecas
\n = quebra de linha
end='' = coloca tudo na mesma linha

********CALCULOS**********

+ , soma
- , subtração
* , multiplicação
/ , divisão
// , divisão inteira (arredonda para numero inteiro)
** , exponenciação ou potenciação
% , retorna o modulo o resto da divisão
(), alterar a presedencia nas contas

********COMANDOS**********

print('multiplicação *', 10 * 10)
print('adição +', 10 + 10)
print(10 * 'maicon-',)
print(10 / 30)
print(10 // 3)
print(2 ** 10)
print(10 % 5,)
print((5+2*10),'atenção o sinal de multiplicação tem precedência no de adição e subtração')
print((5+2)*10, 'agora executara primeiro quem esta nos parentes')

********OPERADORES RELACIONAIS**********

= - um sinal de igual vc afirma ex: print( 2 = 2) to avisando que 2 e igual a 2
== - dois sinais de igual vc pergunta se é igual ex: print( 2 == 2) to perguntando se 2 e igual a 2
!= - Se é diferente um do outro
> - Maior que
>= - Maior igual
< - Menor que
<= - Menor igual

********STRING**********

nome = 'Curso em Video python'
#       123456789112345678901    (21 caracteres)
print(len(nome))                 # Diz quantos caracteres tem ao todo
print(nome.find('deo'))          # Mostra a posição da primeira letra
print(nome.find('garrafa'))      # — 1 significa que não encontrou nada
print('Curso' in nome)           # in — diz se existe ou não a palavra na frase
print(nome[9:14])                # Mostra o que tem no intervalo selecionado
print(nome[0:14])                # Mostra o que tem no intervalo inicial ate o selecionado
print(nome.count('o', 0, 14))    # Mostra quantas vezes o apareceu na frase dentro da area selecionada
print(nome.upper())              # Deixa tudo maiúsculo
print(nome.lower())              # Deixa tudo minusculo
print(nome.capitalize())         # só o primeiro fica maiúsculo
print(nome.title())              # Deixa as primeiras em maiúsculo
print(nome.strip())              # retirou os espaços do início e do fim não do meio
print(nome.rstrip())             # retirou os espaços da direita
print(nome.lstrip())             # retirou os espaços da esquerda
print(nome.split())              # Separa uma string de acordo com um delimitador em vários textos diferentes
print('-'.join(nome))            # coloca traços
print(nome.lower().find('video'))  # primeira parte colocou em minusculo segunda procurou a palavra
capitalize() -> Coloca a 1ª letra Maiúscula;
casefold() -> Transforma todas as letras em minúsculas (existe lower() mas o casefold é melhor normalmente);
count() -> Conta a quantidade de vezes que um valor/símbolo/letra aparece na string;
find() -> Procura um texto dentro de outro texto e dá como resposta a posição do texto encontrado (lá no início falamos que cada letra/símbolo tem uma posição no texto);
format() -> Formata uma string de acordo com os valores passados;
isalnum() -> Verifica se um texto é todo feito com caracteres alfanuméricos (letras e números) -> letras com acento ou ç são considerados letras para essa função;
isalpha() -> Verifica se um texto é todo feito de letras;
isnumeric() -> Verifica se um texto é todo feito por números;
replace() -> Substitui um texto por um outro texto em uma string;
split() -> Separa uma string de acordo com um delimitador em vários textos diferentes;
splitlines() -> separa um texto em vários textos de acordo com os “enters” do texto;
startswith() -> Verifica se a string começa com determinado texto;
strip() -> Retira caracteres indesejados dos textos. Por padrão, retira espaços “extras” no início e no final;
title() -> Coloca a 1ª letra de cada palavra em maiúscula;
upper() -> Coloca o texto todo em letra maiúscula.

print('-------------------------------------------------------------------')
aula = input('Digite duas palavras: ')

print(aula.upper())
print(aula.lower())
print(len(aula),aula.strip(aula))
print(aula[:6])

print('-------------------------------------------------------------------')
LISTAS

num [2] = 3  ->  adiciona o numero 3 no indice 2 da lista
num.append (7) -> adiciona o numero 7 na lista
num.sort - > organiza em ordem crescente
num.sort(reverse=True) -> organiza em ordem decrescente
num.insert(2, 2) -> adiciona item na posição 2
num.remove(2) -> remove o primeiro item 2 da lista
num.count -> conta os itens
num.index -> posição do item


if 4 in num:
    num.remove(4) -> comando para procurar e se achar remover o 4 da lista

-----------------------------
valores = [5, 4, 9]

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

Resposta do for:
Na posição 0 encontrei o valor 5
Na posição 1 encontrei o valor 4
Na posição 2 encontrei o valor 9
----------------------------------------------------
a = [2, 3, 4, 7]
b = a
b[2] = 8
No metodo acima o programa faz uma ligação entre as duas listas e o que for modificado na primeira muda na segunda.

print(a)
print(b)

resposta:
[2, 3, 8, 7]
[2, 3, 8, 7]

========================================
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
No metodo acima, b receberá uma cópia de tudo que esta em a, e se a varia, a for alterada não afetará b

print(a)
print(b)

resposta:
[2, 3, 4, 7]
[2, 3, 8, 7]

===================================================
ENCONTRAR INDICES REPETIDOS COM FOR:

VAR = [1, 2, 3 ,5 ,5]

for c in range(0, 5):
    if var[c] == max(var):
        print(f'{c + 1}', end=' ')

RESULTADO:
4 5    (POSIÇÃO DO INDICE)
"""