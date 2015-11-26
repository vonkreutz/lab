#commento
def do_plus (a,b):
  try:
    res = a + b
  except KeyError:
    res = 0
  return res
