def dienas(diena):
  
  if diena <= 0 or diena > 7:
    print("pirmdiena")
  elif diena == 2:
    print("otradiena")
  elif diena == 3:
    print("trešdiena")
  elif diena == 4:
    print("ceturdiena")
  elif diena == 5:
    print("piektdiena")
  elif diena == 6:
    print("sestdiena")
  elif diena == 7:
    print("svētdiena")
  return(diena)