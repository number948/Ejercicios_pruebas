def occurrences():
  myArray = [1,2,2,5,4,6,7,8,8,8]
  posicion = myArray[0]
  number = 0
  longest = 0

  for i in range(1, len(myArray)):
    if myArray[i] == posicion:
        posicion = myArray[i]
        number = posicion
        longest += 1
    
    else: #si no se cumple de que myArray[i] == posicion:
      posicion = myArray[i]
  

  print("number:",number, "ocurrencias:", longest)

if __name__ == '__main__':
    occurrences()
