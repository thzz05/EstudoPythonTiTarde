n1 = input("Digite a primeira nota do aluno:")

n2 = input("Digite a segunda nota do aluno:")

n3 = input("Digite a terceira nota do aluno:")

n4 = input("Digite a quarta nota do aluno:")

rs =( int(n1)+int(n2)+int(n3)+int(n4) ) /4

# se o aluno tiver uma media acima ou igual a 7 
# ent esatara aprovado. senão a media
# for abaixo ou igual a 4, entao estara reprovado
# caso contrario , estara em recuperaçao
print("a sua media é  "+str(rs)+", entao voçe esta:")

if(rs >= 7):
    print("Aprovado")

elif(rs <=4):
    print("Reprovado")

else :
     print("RECUPERAÇAO SEU BURRO")