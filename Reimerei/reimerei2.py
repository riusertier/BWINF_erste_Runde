import re
# Vokale/Umlaute sind: a, e, i, o, u, ä, ö ,ü
# Konsonanten sind: alle anderen der 26 Buchstaben des Alphabets 

#print("bem" in wort) # 3.

woerter = ["bemühen","Biene","breitschlagen","glühen","hersagen","Hygiene","Knecht","Recht","Schiene","schlank","Schwank"]
grundword = "Bild"
word = "Blick"

vokale = ["a","e","i","o","u","ä","ö","ü"]


def vokalgruppen_finden(wort):
  vokal_gruppen = []

  for index, buchstabe in enumerate(wort):
      voks = ""
      if buchstabe in vokale:
          for _, buc in enumerate(wort[index:]):
              if buc in vokale:
                  voks += buc
              else:
                  break
          vokal_gruppen.append(voks)
  
  index = 0
  while True:
      try:  
          if len(vokal_gruppen[index]) >= 2:
              laenge = len(vokal_gruppen[index])
              for num in range(1, laenge):
                  del vokal_gruppen[index + num]
          index += 1
      except IndexError:
          break
  return vokal_gruppen

def bedingung_1(grundwort_g, wort_g):
  print(grundwort_g, wort_g)
  last = []
  for m in re.finditer(grundwort_g[-2] or grundwort_g[-1], grundword):
      last.append(m.start())
  try:
      ind = last[-2]
  except IndexError:
      ind = last[-1]

  ab_maß1 = grundword[ind:]



  last = []
  for m in re.finditer(wort_g[-2], word):
      last.append(m.start())
  try:
      ind = last[-2]
  except IndexError:
      ind = last[-1]

  ab_maß2 = word[ind:]
  
  if ab_maß1 == ab_maß2:
    return True
  else:
    return False

  

def bedingung_3(grundwort, wort):
 return  wort in grundwort


grundword_vokgrup = vokalgruppen_finden(grundword)
wort_vokgrup = vokalgruppen_finden(word)
print(grundword_vokgrup, wort_vokgrup)

print(bedingung_3(grundword, word))
print(bedingung_1(grundword_vokgrup, wort_vokgrup))