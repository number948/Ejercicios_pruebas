def removeDuplicates():
  myArray = [1,2,3,2]
  new_list = []
  
  for i in myArray: #itera directamente en los elementos
      if i not in new_list:
         new_list.append(i)

  #myArray = new_list #la new_list es "el array" pero que solo contiene los elementos no duplicados, se quita el duplicado
  print(new_list) 

if __name__ == '__main__':
    removeDuplicates()
