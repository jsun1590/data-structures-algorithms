def djb2(key):
  hash = 5381
  for c in key:
    hash = (hash * 33) + ord(c)
  return hash