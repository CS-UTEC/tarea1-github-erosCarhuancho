a = int(input("Ingrese un número: "))

def primo(n):
    if (n<=2):
      return False
  
    else:
      for i in range (2,n):
        if (n%i==0):
          return False
    return True

b=primo(a)
if b==False:
  print(a,"No es un número primo")
else:
  print(a,"Es un número primo")
