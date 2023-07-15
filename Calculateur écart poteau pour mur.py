solutions=[]
#solutions d'écarts possibles
nbre_poteaux=[]
#nombre de poteaux correspondant
rangee=int(input("Quelle est la longueur votre mur ?" ))
n=0
#curseur d'écart
p=1
#curseur de poteaux
c=1
#cuseur pour l'annonce des solutions
while n<rangee:
    n=n+1
    print((rangee-p)/n)
    if (rangee-p)/n==1:
        print("success")
        solutions.append(n)
        nbre_poteaux.append(p)
        print("n=",n)
        print("p=",p)
    else:
        while (rangee-p)/n!=1 and p<n : 
            print("n=",n)
            print("p=",p) 
            p=p+1