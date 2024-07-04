def anagrama(p1:str, p2:str) -> bool:
  # Las palabras se convierten a minúsculas
  p1 = p1.lower()
  p2 = p2.lower()

  #Comparación utilizando sorted()
  if p1 != p2:
    if sorted(p1) == sorted(p2):
      return True
  return False
  
res = anagrama("ramOna","aramon")
print(res)