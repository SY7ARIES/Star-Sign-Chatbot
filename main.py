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
good = [
  'n amazing',
  ' great',
  'n awesome',
  ' good',
  ' fine'
]
sign = [
  'zodiac sign',
  'star sign',
  'constellation',
  'astrological sign'
]
adj = [
  'cute',
  'cool',
  'sweet'
]

greeting = random.choice(greeting)
error = Fore.RED
comp = Fore.LIGHTMAGENTA_EX
user = Fore.BLUE

#-----------------Greeting
print(comp + greeting)
greetingreply = input(user)

emo = TextBlob(greetingreply).polarity

if ' and you' in greetingreply or 'about you' in greetingreply or 'you?' in greetingreply:
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

ynstar = input(user)