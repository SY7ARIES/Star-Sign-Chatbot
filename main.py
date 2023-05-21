import random
from textblob import TextBlob
from colorama import Fore

greeting = [
  'Hey there! How are you?',
  "Good day mate! What's up?",
  "Hello! How are you today?",
  "Hi! How's everything going?",
  "Yo what's up?",
  "Hello there! How has your day being so far?"
]
good = ['n amazing',' great','n awesome',' good',' fine']
sign = ['zodiac sign','star sign','constellation','astrological sign']
adj = ['cute','cool','sweet','lovely']
yes = ['ye', 'yes', 'yea', 'sure', 'ofc', 'of course', 'yas', 'yep', 'yup', 'yap']
constellations = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius','capricorn','aquarius', 'pisces']
months=['january', 'february', 'march', 'april', "may", "june", "july", "august", "september", 'october', "november", "december"]
month31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
month30 = ['April', 'June', 'September', 'November']
Aries=[
  "DATES: March 20 – April 19", "SYMBOL: The ram ♈", "ELEMENT: Fire 🔥", "RULLING PLANET: Mars", "TRAITS: No filter; Gets angry, then forgets why they were angry; Thinks everything is a game they can win; Will do anything on a dare; Easily bored", "Personality: The first sign of the zodiac, Aries loves to be number one. Naturally, this dynamic fire sign is no stranger to competition. Bold and ambitious, Aries dives headfirst into even the most challenging situations—and they'll make sure they always come out on top!", "Famous Aries: Mariah Carey, Jackie Chan, Leonardo DaVinci, Charles Baudelaire, Charles Baudelaire..."
]
Taurus=[
  "DATES: April 20 – May 20", "SYMBOL: The bull ♉", "ELEMENT: Earth 🌏", "RULLING PLANET: Venus", "TRAITS: Just wants to cuddle; Homebody; All or nothing, no in-between; Wears the same outfit everyday; Hates big changes", "Personality: What sign is more likely to take a six-hour bath, followed by a luxurious Swedish massage and decadent dessert spread? Taurus, of course! Taurus is an earth sign represented by the bull. Like their celestial spirit animal, Taureans enjoy relaxing in serene, bucolic environments surrounded by soft sounds, soothing aromas, and succulent flavors.", "Famous Taurus: Karl Marx, Malcolm X, Audrey Hepburn, William Shakespeare, James Brown..."
]
Gemini=[
  "DATES: May 21 – June 20", "SYMBOL: The twins ♊", "ELEMENT: Air ☁️", "RULLING PLANET: Mercury", "TRAITS: Charismatic; Uses humor as a crutch; Could talk to a brick wall; Arguments as flirting; Knows a little about everything", "Personality: Have you ever been so busy that you wished you could clone yourself just to get everything done? That's the Gemini experience in a nutshell. Spontaneous, playful, and adorably erratic, Gemini is driven by its insatiable curiosity. Appropriately symbolized by the celestial twins, this air sign was interested in so many pursuits that it had to double itself. You know, NBD!", "Famous Gemini: Laverne Cox, Kendrick Lamar, Jean-Paul Sartre, Allen Ginsberg, Thomas Mann..."
]
Cancer=[
  "DATES: June 21 – July 21", "SYMBOL: The crab ♋", "ELEMENT: Water 💦", "RULLING PLANET: The Moon", "TRAITS: Sensitive; Seeks comfort; Forgives but never forgets; Only has one boundary, but it is very firm; Takes on other people's problems", "Personality: Represented by the crab, Cancer seamlessly weaves between the sea and shore representing Cancer’s ability to exist in both emotional and material realms. Cancers are highly intuitive and their psychic abilities manifest in tangible spaces. But—just like the hard-shelled crustaceans—this water sign is willing to do whatever it takes to protect itself emotionally. In order to get to know this sign, you're going to need to establish trust! ", "Famous Cancer: Ariana Grande, Frida Kahlo, Marcel Proust, Assata Shakur, Stokely Carmichael..."
]
Leo=[
  "DATES: July 22 – August 22", "SYMBOL: The lion ♌", "ELEMENT: Fire 🔥", "RULLING PLANET: The Sun", "TRAITS: Exudes warmth and creativity; A little bit vain; Really big personality; Wants to stand out; Interested in luxury", "Personality: Roll out the red carpet because Leo has arrived. Passionate, loyal, and infamously dramatic, Leo is represented by the lion and these spirited fire signs are the kings and queens of the celestial jungle. They're delighted to embrace their royal status: Vivacious, theatrical, and fiery, Leos love to bask in the spotlight and celebrate… well, themselves.", "Famous Leo: Usain Bolt, James Baldwin, Kylie Jenner, Coco Chanel, Kate Bush..."
]
Virgo=[
  "DATES: August 23 – September 22", "SYMBOL: The virgin ♍", "ELEMENT: Earth 🌏", "RULLING PLANET: Mercury", "TRAITS: Needs to feel useful; Has a quick fix for everything; Judgmental, but with good intentions; Exceptional spatial awareness; A million ideas per second", "Personality: You know the expression, 'if you want something done, give it to a busy person?' Well, that definitely is the Virgo anthem. Virgos are logical, practical, and systematic in their approach to life. Virgo is an earth sign historically represented by the goddess of wheat and agriculture, an association that speaks to Virgo's deep-rooted presence in the material world. This earth sign is a perfectionist at heart and isn’t afraid to improve skills through diligent and consistent practice.", "Famous Virgo: Fred Hampton, Bernie Sanders, Agatha Christie, Mary Shelley, D.H. Lawrence..."
]
Libra=[
  "DATES: September 23 – October 22", "SYMBOL: The Scales ♎", "ELEMENT: Air ☁️", "RULLING PLANET: Venus", "TRAITS: Hates being alone; Really good aesthetics; Conflict avoidant; Sees every side; Prone to fantasy; Can't make decisions", "Personality: Balance, harmony, and justice define Libra energy. As a cardinal air sign, Libra is represented by the scales (interestingly, the only inanimate object of the zodiac), an association that reflects Libra's fixation on establishing equilibrium. Libra is obsessed with symmetry and strives to create equilibrium in all areas of life — especially when it comes to matters of the heart.", "Famous Libra: Michel Foucault, Friedrich Nietzsche, Kim Kardashian, Donald Glover, Gwyneth Paltrow..."
]
Scorpio=[
  "DATES: October 23 – November 21", "SYMBOL: The scorpion ♏", "ELEMENT: Water 💦", "RULLING PLANET: Pluto", "TRAITS: Primary emotion is betrayal; Looks cool in a leather jacket; OK with uncomfortable silence; Can't be sure if they're serious or joking; Eyes that look into your soul", "Personality: Elusive and mysterious, Scorpio is one of the most misunderstood signs of the zodiac. Scorpio is a water sign that uses emotional energy as fuel, cultivating powerful wisdom through both the physical and unseen realms. In fact, Scorpio derives its extraordinary courage from its psychic abilities, which is what makes this sign one of the most complicated, dynamic signs of the zodiac.", "Famous Scorpio: Leonardo DiCaprio, Charles Manson, Marie Antoinette, Frank Ocean, Albert Camus..."
]
Sagittarius=[
  "DATES: November 22 – December 20", "SYMBOL: The Archer ♐", "ELEMENT: Fire 🔥", "RULLING PLANET: Jupiter", "TRAITS: No indoor voice; Forms opinions off of pure emotion; Obsessed with self-improvement; Wields their truth like a blunt weapon; Friendliest person at the party", "Personality: Oh, the places Sagittarius goes! But… actually. This fire sign knows no bounds. Represented by the archer, Sagittarians are always on a quest for knowledge. The last fire sign of the zodiac, Sagittarius launches its many pursuits like blazing arrows, chasing after geographical, intellectual, and spiritual adventures.", "Famous Sgittarius: Nicki Minaj, Jane Austen, Jean Michel Basquiat, Nostradamus, Emily Dickinson..."
]
Capricorn=[
  "DATES: December 21 – January 19", "SYMBOL: The sea goat ♑", "ELEMENT: Earth 🌏", "RULLING PLANET: Saturn", "TRAITS: Full grown adult since age six; The responsible friend; Motivated by duty; Takes a while to warm up to people; Represses any emotion that gets in the way of success", "Personality: What is the most valuable resource? For Capricorn, the answer is clear: Time. Capricorn is climbing the mountain straight to the top and knows that patience, perseverance, and dedication is the only way to scale. The last earth sign of the zodiac, Capricorn, is represented by the sea-goat, a mythological creature with the body of a goat and the tail of a fish. Accordingly, Capricorns are skilled at navigating both the material and emotional realms.", "Famous Capricorn: Issac Newton, Michelle Obama, Steven Hawking, Mao Zedong, Edgar Allen Poe..."
]
Aquarius=[
  "DATES: January 20 – February 17", "SYMBOL: The water bearer ♒", "ELEMENT: Air ☁️", "RULLING PLANET: Uranus", "TRAITS: Purposefully esoteric; No feelings, just concepts; Actually believes in conspiracy theories; More in love with humanity as a whole than individuals; Always feels like an outcast; Fetishizes personal freedom", "Personality: Despite the 'aqua' in its name, Aquarius is actually the last air sign of the zodiac. Innovative, progressive, and shamelessly revolutionary, Aquarius is represented by the water bearer, the mystical healer who bestows water, or life, upon the land. Accordingly, Aquarius is the most humanitarian astrological sign. At the end of the day, Aquarius is dedicated to making the world a better place.", "Famous Aquarius: Angela Davis, Virginia Woolf, Frederick Douglass, Michael Jordan, Yoko Ono..."
]
Pisces=[
  "DATES: February 18 – March 19", "SYMBOL: The fishes ♓", "ELEMENT: Water 💦", "RULLING PLANET: Neptune", "TRAITS: Somehow both 5 and 50 years old at once; Thinks everything is a sign; Can't remember if they dreamt it or it actually happened; Excessively romantic; Prone to fantasy; No boundaries", "Personality: If you looked up the word 'psychic' in the dictionary, there would definitely be a picture of Pisces next to it. Pisces is the most intuitive, sensitive, and empathetic sign of the entire zodiac — and that’s because it’s the last of the last. As the final sign, Pisces has absorbed every lesson — the joys and the pain, the hopes and the fears — learned by all of the other signs. It's symbolized by two fish swimming in opposite directions, representing the constant division of Pisces' attention between fantasy and reality.", "Famous Pisces: Albert Einstein, Nina Simone, Pier Paolo Pasolini, Genesis P-Orridge, Rosa Luxemburg..."
]

error = Fore.RED
comp = Fore.BLUE
user = Fore.WHITE

#-----------------Greeting

while True:
  print(comp + random.choice(greeting))
  greetingreply = TextBlob(input(user))
  greetingreply = greetingreply.correct()
  greetingreply = greetingreply.lower()
  if 'hi' in greetingreply or 'hello' in greetingreply or 'hey' in greetingreply:
    continue
  else:
    break
    
emo = greetingreply.polarity

if ' and you' in greetingreply or 'about you' in greetingreply or 'you?' in greetingreply or 'are you' in greetingreply:
  print(comp + "Oh, I am having a" + random.choice(good) + " day so far! Thank you for asking!\n\nSo, what's your name?")
elif emo > 0:
  print(comp + "That's amazing! \n\nSo, what's your name?")
elif emo == 0:
  print(comp + "That's nice.\n\nSo, what's your name?")
elif emo < 0:
  print(comp + "Oh, that's fine, don't worry, you'll feel much better soon since you are chating with me heheeh, anyways...\n\nSo, what's your name?")
  
name = input(user)
name = name.lower()

if "my name is " in name or "i'm " in name or "i am " in name:
  name = name.replace('my name is ', '')
  name = name.replace("i'm ", '')
  name = name.replace("i am ", '')

while len(name.split()) > 1 or len(name.split()) < 1:
  if "don't" in name or "no" in name:
    print(comp + "Oh, that's fine, I'm sorry for any offense, I swear didn't mean that \U0001F622\n\nAnyways, my name is Asta, a star Sign expert. I am an Aries, do you know what your", random.choice(sign), "is?")
    name = 'no'
    break
  elif len(name.split()) > 1:
    print(comp + "Wow, I'm sorry but I am really bad at memorising, your name is sooooo long \U0001F635. Just give me your first name please =.=")
    name=input(user)
    if name.split() == 1: 
      break
  elif len(name.split()) < 1:
    print(comp + "Oh come on, don't kill our chat 🥹")
    print(comp + "What's your first name?")
    name = input(user)
    if name.split() == 1: 
      break
  break

if name == 'no':
  pass
else:
  name = name.capitalize()
  print(comp + 'Awww', name, "That's such a", random.choice(adj), "name! UwU")
  print(comp + "\nMy name is Asta, a star sign expert! I am an Aries, do you know what your", random.choice(sign), "is?")

ynstar = (input(user)).lower()

know = False

for x in yes:
  if x in ynstar:
    know = True

#=====================if user knows their star sign

if know == True:
  print(comp + "Oh,", random.choice(adj), "\b! \n\nSo, what is your", random.choice(sign), "\b?")
  star = (input(user)).lower()

  starknow = False
  
  for x in constellations:
    if x in star:
      starknow = True

  #------------------if user fake know their star sign
  
  while starknow == False:
    print(comp + "I'm sorry, but perhaps you didn't insert an existing constellation, or maybe you inserted the wrong spelling. \nWould you like to try again or you want me to check your", random.choice(sign), "again? (type 'try again' to try again)")
    rechoose = ((TextBlob(input(user))).correct()).lower()
    if 'try again' in rechoose:
      print(comp + 'What is your', random.choice(sign), "\b?")
      star = (input(user)).lower()
      for x in constellations:
        if x in star:
          starknow = True
          break
        if x not in star:
          starknow = False
          continue
    else:
      know = False
      break

  #------------------if user real know their star sign
  
  if starknow == True:
    for x in constellations:
      if x in star:
        star = star.replace(star, x)
    if 'aries' in star or 'too' in star:
      star = star.capitalize()
      print(comp + "That's", random.choice(adj), "\b! We got the same", random.choice(sign), "\b! \n\nWould you like to know about the personalities of the Arieses?")
    else:
      if star[-1] == 's':
        starplu = 'es'
      else:
        starplu = 's'
      star = star.capitalize()
      print(comp + "Wow, " + random.choice(adj) + "! I always love " + star + starplu + ". \n\nWould you like to know about the personalities of the " + star + starplu + "?")

#=====================if user don't know their star sign

if know == False:
  print(comp + "That's totally fine, most of my friends don't know their", random.choice(sign) ,"\bs.")

  #----------------------month
  
  print(comp + "Let's find out your", random.choice(sign) ,"then!\n\nWhich month were you born in?")
  month = (TextBlob(input(user)).correct()).lower()  

  monthtf = False
  for x in months:
    if x in month:
      monthtf = True

  while monthtf == False:
    print(comp + "Sorry, you didn't answer with a valid month. Please check your spelling. Let's do this again.")
    print(comp + "\nWhich month were you born in?")
    month = (input(user)).lower()
    for x in months:
      if x in month:
        monthtf = True
        break
      if x not in month:
        monthtf = False
        continue

  for x in months:
    if x in month:
      month = str(month)
      month = (month.replace(month, x)).capitalize()
  
  #---------------------day
  
  while monthtf == True:
    print(comp + "\n" + random.choice(adj).capitalize(), "\b! And which day of", month.capitalize(),"\b? (please just type the number without 'th')")
    try:
      day = int(input(user))
      break
    except:
      print(error + "Please enter the NUMBER without 'th'!!!;-;")
      
  while day > 28 or day <= 0:
    if day <= 0:
      print(comp + "Haha, funny, but I believe we all know that our birthday datess must be a natural number. Please check with your parents again, I am sure you were born on an existing date. Let's do this again.")
      print(comp + "Which day of", month,"were you born in? (please just type the number without 'th')")
      try:
        day = int(input(user))
        break
      except:
        print(error + "Please enter the NUMBER without 'th'!!!;-;")
    #------------------31 months
    elif month in month31 and day > 31:
      print(comp + "Sorry, you didn't answer with a valid day. Please check with your parents again, I am sure you were born on an existing date. Let's do this again.")
      print(comp + "\nWhich day of", month,"were you born in? (please just type the number without 'th')")
      try:
        day = int(input(user))
      except:
        print(error + "Please enter the NUMBER without 'th'!!!;-;")
      if day <= 31 :
        break 
    elif month in month31 and day <= 31:
      break
    #------------------30 months
    elif month in month30 and day > 30:
      print(comp + "Sorry, you didn't answer with a valid day. Please check with your parents again, I am sure you were born on an existing date. Let's do this again.")
      print(comp + "\nWhich day of", month,"were you born in? (please just type the number without 'th')")
      try:
        day = int(input(user))
      except:
        print(error + "Please enter the NUMBER without 'th'!!!;-;")
      if day <= 31 :
        break
    elif month in month30 and day <= 30:
      break
    #------------------29 months
    elif month == 'February' and day > 29:
      print(comp + "Sorry, you didn't answer with a valid day. Please check with your parents again, I am sure you were born on an existing date. Let's do this again.")
      print(comp + "\nWhich day of", month,"were you born in? (please just type the number without 'th')")
      try:
        day = int(input(user))
      except:
        print(error + "Please enter the NUMBER without 'th'!!!;-;")
      if day <= 31 :
        break   
    elif month=='February' and day==29:
      print(comp + "Wow, 29th of February! What a special birthday! \nDid you know that the chances of being born on leap day are so rare that less than 0.1 percent of the world's population is born on February 29? Anyways, haha.")
      break
    elif month == 'February' and day < 28:
      break

  #-------------------star sign calculation
  
  def starfun():
    global astro_sign
    global ynper
    if month == 'December':
      astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 'January':
  	   astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 'February':
  	   astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 'March':
  	   astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 'April':
  	   astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 'May':
  	   astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 'June':
  	   astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 'July':
  	   astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 'August':
  	   astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 'September':
  	   astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 'October':
  	   astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 'November':
  	   astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
  
    if astro_sign[0]=='a' or astro_sign[0]=='A' or astro_sign[0]=='o' or astro_sign[0]=='O':
      if astro_sign == 'Aries':
        print(comp + "Wow, you are an " + astro_sign +"! Just like me!")
      else:
        print("\nWow, you are an " + astro_sign + "!")
    elif month.lower() == 'february' and day == 29:
      print(comp + "You are a " + astro_sign + "!")
    else:
      print(comp + "Wow, you are a " + astro_sign + "!") 
  starfun()

  #------------------personalities

  def ynandplu():
    if astro_sign[-1] == 's':
        starplu = 'es'
    else:
      starplu='s'
    if astro_sign =='Aries':
        print(comp + "\nWould you like to know about the personalities of " + astro_sign + "? (Insert 'Yes' for yes)")
    else:    
      print(comp + "I like " + astro_sign + starplu + "!")  
      print(comp + "\nWould you like to know about the personalities of " + astro_sign + "? (Insert 'Yes' for yes)")
  ynandplu()
  
  ynper = (input(user)).lower()

  def pfunc(y):
    for x in y:
      print(Fore.LIGHTMAGENTA_EX + "\n" + x)

  if ynper == 'yes':
    if astro_sign == 'Aries':
      pfunc(Aries)
    if astro_sign == 'Taurus':
      pfunc(Taurus)
    if astro_sign == 'Gemini':
      pfunc(Gemini)
    if astro_sign == 'Cancer':
      pfunc(Cancer)
    if astro_sign == 'Leo':
      pfunc(Leo)
    if astro_sign == 'Virgo':
      pfunc(Virgo)
    if astro_sign == 'Libra':
      pfunc(Libra)
    if astro_sign == 'Scorpio':
      pfunc(Scorpio)
    if astro_sign == 'Sagittarius':
      pfunc(Sagittarius)
    if astro_sign == 'Capricorn':
      pfunc(Capricorn)
    if astro_sign == 'Aquarius':
      pfunc(Aquarius)
    if astro_sign == 'Pisces':
      pfunc(Pisces)
  else:
    print(comp + "Alright then, it's nice too talk to you, I enjoyed it very much. I got a job to do know, I hope we can chat again. See ya, pwaaa~")
    print(error + "Asta left the chat...")
