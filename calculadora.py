#calculadora
def soma(numero_um,numero_dois):
  return numero_um + numero_dois
  
def subtracao(numero_um,numero_dois):
  return numero_um - numero_dois
  
def multiplicacao(numero_um,numero_dois):
  return numero_um * numero_dois
  
def divisao(numero_um,numero_dois):
  return numero_um / numero_dois
  
  
def executar(caixa):
  print("Escolhe um numero")
  numero_um=int( input())
  print("Escolhe outro numero")
  numero_dois=int( input()) 
  if caixa=="soma":
    print (soma(numero_um, numero_dois))  
  elif caixa=="subtracao":
    print (subtracao(numero_um,numero_dois))  
  elif caixa=="multiplicacao":
    print (multiplicacao(numero_um,numero_dois))  
  elif caixa=="divisao":
    print (divisao(numero_um,numero_dois))

#testes
#print("subtracao", subtracao(2,4))
#print("soma", soma(2,2))
#print("multiplicacao", multiplicacao(2,5))
#print("divisao", divisao (15,3))
ligado = True 
while ligado:

  print("Escolhe uma operacao")
  caixa = input()
  if caixa== "soma" or caixa== "subtracao" or caixa== "multiplicacao" or caixa== "divisao":
    executar(caixa)  
  elif caixa == "desligado":
    ligado=False
  else:
    print("Operacao Desconhecida") 
    print("Escolha uma das seguintes operacoes:\n Soma \n Subtracao \n Multiplicacao \n Divisao")
