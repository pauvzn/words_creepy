palabra = input("¿Qué palabra quieres conocer?:")

meme_dict = {"cringe": "que te da pena ajena",
"lol": "mucha risa",
"funar": "desacreditar a alguien a través de las plataformas virtuales",
"idk": "no sé",
"ntp": "no te preocupes"
"fomo": "Fear Of Missing Out"}
"xp": "Experiencia"
"noob":"novato"
"gg":"god game"
"x2":"igual yo"}

if palabra in meme_dict.keys():
  print(meme_dict[palabra])
else:
  print("esa palabra no la tenemos, pero estamos trabajando en ello")
