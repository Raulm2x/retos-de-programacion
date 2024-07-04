def anagrama(p1:str, p2:str) -> bool:
  p1 = p1.lower()
  p2 = p2.lower()

  if p1 != p2:
    if sorted(p1) == sorted(p2):
      return True
  return False
  
res = anagrama("ramOna","aramon")
print(res)