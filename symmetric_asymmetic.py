def isSymmetric():
  matrix = ['a','b','c', 'd', 'd', 'c', 'b', 'a']
  reverse = matrix[::-1]
  print(reverse)

  if matrix == reverse:
     print("Symmetric")
  else:
     print("Asymmetric")

if __name__ == '__main__':
    isSymmetric()
