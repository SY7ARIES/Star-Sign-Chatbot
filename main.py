import random
from textblob import TextBlob
from colorama import Fore
from replit import audio
import time
  
greeting = [
  'Hey there! How are you?', "Good day mate! What's up?",
  "Hello! How are you today?", "Hi! How's everything going?", "Yo what's up?",
  "Hello there! How has your day being so far?"
]
good = ['n amazing', ' great', 'n awesome', ' good', ' fine']
sign = ['zodiac sign', 'star sign', 'constellation', 'astrological sign']
adj = ['cute', 'cool', 'sweet', 'lovely']
yes = [
  'ye', 'yes', 'yea', 'sure', 'ofc', 'of course', 'yas', 'yep', 'yup', 'yap'
]
constellations = [
  'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio',
  'sagittarius', 'capricorn', 'aquarius', 'pisces'
]
months = [
  'january', 'february', 'march', 'april', "may", "june", "july", "august",
  "september", 'october', "november", "december"
]
month31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
month30 = ['April', 'June', 'September', 'November']

Aries = [
  "DATES: March 20 – April 19", "SYMBOL: The ram ♈", "ELEMENT: Fire 🔥",
  "RULLING PLANET: Mars",
  "TRAITS: No filter; Gets angry, then forgets why they were angry; Thinks everything is a game they can win; Will do anything on a dare; Easily bored",
  "Personality: The first sign of the zodiac, Aries loves to be number one. Naturally, this dynamic fire sign is no stranger to competition. Bold and ambitious, Aries dives headfirst into even the most challenging situations—and they'll make sure they always come out on top!",
  "Famous Aries: Mariah Carey, Jackie Chan, Leonardo DaVinci, Charles Baudelaire, Charles Baudelaire..."
]
Taurus = [
  "DATES: April 20 – May 20", "SYMBOL: The bull ♉", "ELEMENT: Earth 🌏",
  "RULLING PLANET: Venus",
  "TRAITS: Just wants to cuddle; Homebody; All or nothing, no in-between; Wears the same outfit everyday; Hates big changes",
  "Personality: What sign is more likely to take a six-hour bath, followed by a luxurious Swedish massage and decadent dessert spread? Taurus, of course! Taurus is an earth sign represented by the bull. Like their celestial spirit animal, Taureans enjoy relaxing in serene, bucolic environments surrounded by soft sounds, soothing aromas, and succulent flavors.",
  "Famous Taurus: Karl Marx, Malcolm X, Audrey Hepburn, William Shakespeare, James Brown..."
]
Gemini = [
  "DATES: May 21 – June 20", "SYMBOL: The twins ♊", "ELEMENT: Air ☁️",
  "RULLING PLANET: Mercury",
  "TRAITS: Charismatic; Uses humor as a crutch; Could talk to a brick wall; Arguments as flirting; Knows a little about everything",
  "Personality: Have you ever been so busy that you wished you could clone yourself just to get everything done? That's the Gemini experience in a nutshell. Spontaneous, playful, and adorably erratic, Gemini is driven by its insatiable curiosity. Appropriately symbolized by the celestial twins, this air sign was interested in so many pursuits that it had to double itself. You know, NBD!",
  "Famous Gemini: Laverne Cox, Kendrick Lamar, Jean-Paul Sartre, Allen Ginsberg, Thomas Mann..."
]
Cancer = [
  "DATES: June 21 – July 21", "SYMBOL: The crab ♋", "ELEMENT: Water 💦",
  "RULLING PLANET: The Moon",
  "TRAITS: Sensitive; Seeks comfort; Forgives but never forgets; Only has one boundary, but it is very firm; Takes on other people's problems",
  "Personality: Represented by the crab, Cancer seamlessly weaves between the sea and shore representing Cancer’s ability to exist in both emotional and material realms. Cancers are highly intuitive and their psychic abilities manifest in tangible spaces. But—just like the hard-shelled crustaceans—this water sign is willing to do whatever it takes to protect itself emotionally. In order to get to know this sign, you're going to need to establish trust! ",
  "Famous Cancer: Ariana Grande, Frida Kahlo, Marcel Proust, Assata Shakur, Stokely Carmichael..."
]
Leo = [
  "DATES: July 22 – August 22", "SYMBOL: The lion ♌", "ELEMENT: Fire 🔥",
  "RULLING PLANET: The Sun",
  "TRAITS: Exudes warmth and creativity; A little bit vain; Really big personality; Wants to stand out; Interested in luxury",
  "Personality: Roll out the red carpet because Leo has arrived. Passionate, loyal, and infamously dramatic, Leo is represented by the lion and these spirited fire signs are the kings and queens of the celestial jungle. They're delighted to embrace their royal status: Vivacious, theatrical, and fiery, Leos love to bask in the spotlight and celebrate… well, themselves.",
  "Famous Leo: Usain Bolt, James Baldwin, Kylie Jenner, Coco Chanel, Kate Bush..."
]
Virgo = [
  "DATES: August 23 – September 22", "SYMBOL: The virgin ♍",
  "ELEMENT: Earth 🌏", "RULLING PLANET: Mercury",
  "TRAITS: Needs to feel useful; Has a quick fix for everything; Judgmental, but with good intentions; Exceptional spatial awareness; A million ideas per second",
  "Personality: You know the expression, 'if you want something done, give it to a busy person?' Well, that definitely is the Virgo anthem. Virgos are logical, practical, and systematic in their approach to life. Virgo is an earth sign historically represented by the goddess of wheat and agriculture, an association that speaks to Virgo's deep-rooted presence in the material world. This earth sign is a perfectionist at heart and isn’t afraid to improve skills through diligent and consistent practice.",
  "Famous Virgo: Fred Hampton, Bernie Sanders, Agatha Christie, Mary Shelley, D.H. Lawrence..."
]
Libra = [
  "DATES: September 23 – October 22", "SYMBOL: The Scales ♎",
  "ELEMENT: Air ☁️", "RULLING PLANET: Venus",
  "TRAITS: Hates being alone; Really good aesthetics; Conflict avoidant; Sees every side; Prone to fantasy; Can't make decisions",
  "Personality: Balance, harmony, and justice define Libra energy. As a cardinal air sign, Libra is represented by the scales (interestingly, the only inanimate object of the zodiac), an association that reflects Libra's fixation on establishing equilibrium. Libra is obsessed with symmetry and strives to create equilibrium in all areas of life — especially when it comes to matters of the heart.",
  "Famous Libra: Michel Foucault, Friedrich Nietzsche, Kim Kardashian, Donald Glover, Gwyneth Paltrow..."
]
Scorpio = [
  "DATES: October 23 – November 21", "SYMBOL: The scorpion ♏",
  "ELEMENT: Water 💦", "RULLING PLANET: Pluto",
  "TRAITS: Primary emotion is betrayal; Looks cool in a leather jacket; OK with uncomfortable silence; Can't be sure if they're serious or joking; Eyes that look into your soul",
  "Personality: Elusive and mysterious, Scorpio is one of the most misunderstood signs of the zodiac. Scorpio is a water sign that uses emotional energy as fuel, cultivating powerful wisdom through both the physical and unseen realms. In fact, Scorpio derives its extraordinary courage from its psychic abilities, which is what makes this sign one of the most complicated, dynamic signs of the zodiac.",
  "Famous Scorpio: Leonardo DiCaprio, Charles Manson, Marie Antoinette, Frank Ocean, Albert Camus..."
]
Sagittarius = [
  "DATES: November 22 – December 20", "SYMBOL: The Archer ♐",
  "ELEMENT: Fire 🔥", "RULLING PLANET: Jupiter",
  "TRAITS: No indoor voice; Forms opinions off of pure emotion; Obsessed with self-improvement; Wields their truth like a blunt weapon; Friendliest person at the party",
  "Personality: Oh, the places Sagittarius goes! But… actually. This fire sign knows no bounds. Represented by the archer, Sagittarians are always on a quest for knowledge. The last fire sign of the zodiac, Sagittarius launches its many pursuits like blazing arrows, chasing after geographical, intellectual, and spiritual adventures.",
  "Famous Sgittarius: Nicki Minaj, Jane Austen, Jean Michel Basquiat, Nostradamus, Emily Dickinson..."
]
Capricorn = [
  "DATES: December 21 – January 19", "SYMBOL: The sea goat ♑",
  "ELEMENT: Earth 🌏", "RULLING PLANET: Saturn",
  "TRAITS: Full grown adult since age six; The responsible friend; Motivated by duty; Takes a while to warm up to people; Represses any emotion that gets in the way of success",
  "Personality: What is the most valuable resource? For Capricorn, the answer is clear: Time. Capricorn is climbing the mountain straight to the top and knows that patience, perseverance, and dedication is the only way to scale. The last earth sign of the zodiac, Capricorn, is represented by the sea-goat, a mythological creature with the body of a goat and the tail of a fish. Accordingly, Capricorns are skilled at navigating both the material and emotional realms.",
  "Famous Capricorn: Issac Newton, Michelle Obama, Steven Hawking, Mao Zedong, Edgar Allen Poe..."
]
Aquarius = [
  "DATES: January 20 – February 17", "SYMBOL: The water bearer ♒",
  "ELEMENT: Air ☁️", "RULLING PLANET: Uranus",
  "TRAITS: Purposefully esoteric; No feelings, just concepts; Actually believes in conspiracy theories; More in love with humanity as a whole than individuals; Always feels like an outcast; Fetishizes personal freedom",
  "Personality: Despite the 'aqua' in its name, Aquarius is actually the last air sign of the zodiac. Innovative, progressive, and shamelessly revolutionary, Aquarius is represented by the water bearer, the mystical healer who bestows water, or life, upon the land. Accordingly, Aquarius is the most humanitarian astrological sign. At the end of the day, Aquarius is dedicated to making the world a better place.",
  "Famous Aquarius: Angela Davis, Virginia Woolf, Frederick Douglass, Michael Jordan, Yoko Ono..."
]
Pisces = [
  "DATES: February 18 – March 19", "SYMBOL: The fishes ♓", "ELEMENT: Water 💦",
  "RULLING PLANET: Neptune",
  "TRAITS: Somehow both 5 and 50 years old at once; Thinks everything is a sign; Can't remember if they dreamt it or it actually happened; Excessively romantic; Prone to fantasy; No boundaries",
  "Personality: If you looked up the word 'psychic' in the dictionary, there would definitely be a picture of Pisces next to it. Pisces is the most intuitive, sensitive, and empathetic sign of the entire zodiac — and that’s because it’s the last of the last. As the final sign, Pisces has absorbed every lesson — the joys and the pain, the hopes and the fears — learned by all of the other signs. It's symbolized by two fish swimming in opposite directions, representing the constant division of Pisces' attention between fantasy and reality.",
  "Famous Pisces: Albert Einstein, Nina Simone, Pier Paolo Pasolini, Genesis P-Orridge, Rosa Luxemburg..."
]

Ariesfact = [
  "Aries Problem: The Ram doesn't know how to deal with anger and control it.",
  "Things that Aries never hesitate in: To change things they don 't like",
  "Things Aries truly want: Trust, loyalty, and respect",
  "Things Aries enjoy: Being adventurous and bossy on others",
  "Things Aries get frustrated with: When it takes a lot of time in explaining things to others.",
  "Things Aries hate: To repeat the same things again and again.",
  "Things Aries do when ignored: Talk louder",
  "Best adventurous partner for Aries: Leo",
  "The hardest thing for Aries: The hardest thing for them is to sit back and keep quiet especially when they know whatever happening is unnecessary and a waste of time.",
  "Playlist of Aries: Perfect romantic songs when romantic, songs indicating rage when they are angry. Basically, they are. music lovers and listen to genres depending on their mood.",
  "Best gift for Aries: Athletic items, clothing or work-related things."
]
Taurusfact = [
  "Taurus Problem: You are poor and slow in communicating your feelings while dating",
  "Taurus Pet Peeves: Being rushed, interruption, sudden changes, lack of common sense, ignorance, and being hungry.",
  "Taurus Motto: Don’t talk, act. Don’t say, show. Don’t promise, prove.",
  "Things Taurus appreciates: You appreciate strong work ethics, honesty, and straightforwardness.",
  "Things Taurus are well versed: You can kill people with sarcasm. You can easily read people’s true intentions. You are immune to stupid remarks.",
  "Things that Taurus can’t compromise: Intelligence, independence, stability, and money",
  "Best Adviser for Taurus: Cancer",
  "Things that only Taurus can do: You will think about your close ones all day but will never text them. You will expect them to call or text you.",
  "Things Taurus gets frustrated with: You get frustrated when you have to say the same thing twice. You don’t rephrase, interpret and explain things. You just think people are dumb if they don’t understand.",
  "The hardest thing for Taurus: The hardest thing for you is to accept the wrong things to you. You get emotionally hurt in this situation. You have the tendency to take things personally.",
  "Things Taurus hate: You hate when unknown people or the people who are not in your closed circle talks about your personal things. You hate to bring up your past and on hearing the stories of your ex-partner. You don’t like cleaning up after other people. You hate being left in the dark about things. You get irritated by last moment changes.",
  "Two things Taurus should remember: You should take care of your thoughts when you are alone. You should take care of your words when you are with people.",
  "Playlist for Taurus: Your music taste is large and vast. You have songs for every mood and thought. You will be in the hard stuff, soft stuff and things that offer a deep and meaningful experience. You share your feelings and thoughts through music. You are a master of emotion and translate your feelings in the form of a song."
]
Geminifact = [
  "Gemini Problem: You won’t ask twice. You can feel more than one emotion at a time hence are often confused",
  "Gemini in their lowest point: You will be silent and seem to be lost in another world or dreaming about something when someone approaches you.",
  "Gemini motto: I am a simple person with a complicated mind.",
  "The evil side to a Gemini: You like to mess with people for fun and enjoyment especially if you know it gets under their skin",
  "Things Gemini hate: You hate to ask for help. You believe that you can do everything on your own. You hate to do things in routine and schedule time. You hate to be reminded of all the mistakes you made.",
  "Things Gemini do when pissed off: Your face will turn tensed and you will talk less. You may turn mad but it will not be for long.",
  "Things Gemini do when doubtful: You will sit quietly and keep on thinking too much",
  "Assumptions about a Gemini: That you flirt too much, you are a troublemaker",
  "Best gift for Gemini: Latest technology, books or magazine subscription, laptop, phone accessories, video games, board games, Tv-series and movie DVDs",
  "Things Gemini gets frustrated with: When people start causing unnecessary problems. You feel irritated when people start taking things personally. You can’t stand when people make things more difficult than actual.",
  "The hardest thing for Gemini: To sit still, to trust people and to keep cool under certain pressures.",
  "Things Gemini simply ignore: You simply ignore the one who has hurt you. Moving forward in life is always your priority. You will never trust the person completely once they have burned bridges with you.",
  "Two things Gemini should remember: To be consistent and determined"
]
Cancerfact = [
  "Cancer Problem: You find difficulty in forgiving people when they betray or break your trust. You will snap without warning. It's hard for you to forget someone with whom you have shared lots of memories.",
  "Cancer when pissed off: Your face tenses up and you avoid talking with people. You disconnect with people for the time being and prefer to stay in your shell. You don’t stay mad for a long time.",
  "Cancer fears: You have the fear of losing and let go of someone or something you really care for.",
  "Things Cancer like: You like to keep old things and remember all special occasions and events in the life of your closed ones. You like family, home, and house parties.",
  "Things Cancer hate: You hate guessing games. You dislike opposition, failure, being told what to do and advice whether good or bad. You hate insensitive people who are pretentious, thoughtless, and harsh. You hate those people who constantly criticize you and indirectly taunt you about your downfalls. You also hate people who do not keep their promises and forget important events",
  "Things that irritate Cancer: You get really annoyed with careless and thoughtless people. The blatant disregard irritates you the most.",
  "Things Cancer don’t do: You don’t turn your backs on the people you love no matter what happened between you.",
  "Things that give you joy: You feel happy when you are the first priority for someone and they actually care and pamper you. You are super-duper happen with family, friends, food and good finances.",
  "Things you are not interested in: You are not interested in light flirtation. You don’t do kid play and are serious about getting in love.",
  "Perfect gift for Cancer: The perfect gift for you are collectibles and items that can be used at home."
]
Leofact = [
  "Leo Problem: You get sentimental over the smallest things at times. You can’t stand watching someone do something when you know how to do it in a better way.",
  "Leo when pissed off: You get irritated when you constantly have to fight for someone’s attention. You prefer to be alone and don’t care what you say or talk when irritated or pissed off.",
  "Things Leo hate: You hate for being taken for granted, though you probably won’t show it. You don’t like forced interactions, conversations, and friendship",
  "Things Leo do when hurt or upset: You will shut down completely and become heartless. You will make sure that others know about it or not.",
  "Things Leo like: You like to continue courting, dating, gifts, and romance forever. You love to be different and remember every keen detail. You always like to help people even if they have little to give.",
  "Leos at their lowest points: You are short-tempered and needy at your lowest points.",
  "First thing that comes in Leo mind: Follow me",
  "How to catch Leo attention: You get inspired when someone is alluring and fun.",
  "Perfect gift for Leo: The perfect gift for you is a status symbol item or a family-related collection such as a keepsake album.",
  "Leo motto: Love me or leave me alone, go hard or go home"
]
Virgofact = [
  "Virgo Problem: You can’t wait for too long. If you have to wait, you will lose interest. Once you put your mind to something, you want it right away. You find a hard time explaining what you feel. It is hard to snap you out of a bad mood.",
  "Virgo motto: I do not mean to come off as defensive. I am just making sure that you have your facts right. I rely on my damn self",
  "Virgos biggest pet peeves: Invasive or nosy people",
  "What works for a Virgo: Facts and not assumptions",
  "Things Virgo like: You like animals, beauty, eating healthy, orderliness. You are more interested in giving than receiving. You get very happy when people agree with you. You can tirelessly watch million of times your favorite movie and T.V. shows.",
  "Things Virgo hate: You hate sloppiness, squalor, being wrong, and chaos. You dislike being seen as weak. You also hate being lectured and judged. You even hate to make a scene.",
  "Things Virgo pay attention: You always pay keen attention to the vibes of the people around you.",
  "Things Virgo are attracted to: You are attracted to discipline, manners, and perfection. You are also attracted to confidence, ambition, and intelligence.",
  "Things that irritate Virgo: You get irritated when you have to work with messy people and who can’t think for themselves. You get annoyed when someone tries constantly to bring you down.",
  "Virgo does not have time for: You have no time for show-offs and be center of attention",
  "Perfect gift for Virgo: The perfect gift for you could be a health-related item. Gifts such as gym equipment, herbs for healthy meals, a goal journal, or essential oils are perfect for you."
]
Librafact = [
  "Libra Problem: You find it hard to say no when anyone asks for a favor. You tend to go overboard when caring for others to the level that it gets frustrating for you at times. Nobody can calm you down when you are angry.",
  "Things Libra hate: You hate unnecessary conflict. Also, you hate texting first, it makes you feel like you are annoying. You can’t stand selfish and inconsiderate people.",
  "Libra motto: I fall too fast, forgive too easily and care too much.",
  "Things Libra crave: You crave balance and harmonious relationships.",
  "Libra's best teammates: Scorpio",
  "Things Librans do when pissed off: You will not listen to anything and act pricey.",
  "Things that make Libra angry: You get hostile when you feel someone is going after something that belongs to you. You get annoyed when people don’t give straight answers.",
  "3 things Libra are good at: staying neutral, stylish, and sniff out unwanted things."
  "Something Libra says to themselves all the time: I gave this idiot too many chances to improve."
  "Fun things Libra like to do: Boat ride and watching a live concert."
  "Best gift for Libra: Gourmet food, stylish attire, interesting home decor, mobile, fine photo frame, a popular book, tickets of a live concert, movies, or art exhibition."
]
Scorpiofact = [
  "Scorpio Problem: You find it hard to trust people and fall in love. Until you find the truth, you keep asking questions over and over to catch the slipping in the story shared by others.",
  "Scorpio motto: The only people I owe my loyalty to are the ones who never made me question theirs.",
  "Scorpio’s Pet peeve: when someone lies to you, or you’re being made to feel jealous by a lover, being outshone at any task, being the victim of gossip, not being able to get your way, and superficial people.",
  "Things Scorpions can offer: Stimulating and riveting activities, emotional connection and dependability, promise only when you intend to keep, deep and profound conversation, loyalty, and insightful advice and tips.",
  "Things Scorpions hate: dependent on others, liars, disloyal friends, failure, dishonesty, unmotivated and non-passionate people, and inflexibility",
  "Things Scorpions are good at: managing different tasks efficiently, loving with all their heart, being both calm and crazy. You are also good at loving from a distance.",
  "Things Scorpion do when pissed off: You avoid eye contact with those who have pissed you off. You will strike them on the place which is closely attached to them.",
  "Things Scorpion would never do: You are not a fan of drama. Your words are never empty.",
  "Things Scorpion do after an argument: You go into a silent zone and make the people around to do brainstorming about what you are thinking at the moment",
  "Scorpio biggest fear: Being judged and betrayed",
  "Scorpions partner for dominance: Pisces and Cancer.",
  "Things that make Scorpion happy: Finding someone that understands you and who doesn’t think you are insane.",
  "Scorpions are allergic to: Lies, fake things, quitting, disloyalty and foolish games.",
  "Ideal gifts for Scorpions: books, necklaces, leather gloves or clothes, dark board games, sentimental keepsake, travel tickets of exotic places"
]
Sagittariusfact = [
  "Lucky Day: Thursday",
  "Lucky Number: 3, 12, 21, 30",
  "Lucky Colour: Violet, Purple, Red, Pink",
  "Lucky Stone(s): Amethyst and Topaz (The gemstone is suggested considering Aries as the Ascendant/Lagna Sign. To know your Ascendant/Lagna Sign, click here.) ",
  "Lucky Talisman: Tin, Flint, Arrowheads and Cornucopia",
  "Positive Qualities of Sagittarius: Large-hearted, Frank, Fearlessness, Self-dependent, Love for nature and travel.",
  "Negative Qualities of Sagittarius: Over-confident, Brash, Inconsistent, Lack of focus. To lessen the impact of your negativities – right away Talk to an Astrologer!"
]
Capricornfact = [
  "Lucky Day: Saturday"
  "Lucky Number: 1, 4, 8, 10, 13, 17, 19, 22, 26",
  "Lucky Colour: Brown, Steel, Grey, Black"
  "Lucky Stone(s): Dark Sapphire (The gemstone is suggested considering Aries as the Ascendant/Lagna Sign. To know your Ascendant/Lagna Sign, click here.)",
  "Lucky Talisman : The Plough",
  "Positive Qualities :Faithful, Ambitious, Self-controlled, Determined, Responsible, Sincere",
  "Negative Qualities :Shy, Pessimistic, Awkward, Detached, Self-centred, Gloomy, Stubborn."
]
Aquariusfact = [
  "Lucky Day : Sunday and Saturday",
  "Lucky Number :4, 8, 13, 17, 22, 26",
  "Lucky Colour :Blue, Blue-green, Grey, Black",
  "Lucky Stone(s) :Opal and Aquamarine (The gemstone is suggested considering Aries as the Ascendant/Lagna Sign. To know your Ascendant/Lagna Sign, click here.)",
  "Lucky Talisman :The Key (lead) and the Owl",
  "Positive Qualities of Aquarius :Truthfulness, Just, Curious, Affectionate Personality, Frank and Imaginative.",
  "Negative Qualities of Aquarius :Unpredictable, Detachment, Tendency to go off-track, and Inefficiency."
]
Piscesfact = [
  "Lucky Day: Thursday and Monday",
  "Lucky number: 3, 7, 12, 16, 21, 25, 30, 34, 43, 52",
  "Lucky Colour: Mauve, Lilac, Violet, Violet, Sea Green",
  "Lucky Stone: beruz, coral, emerald, pearl"
  "Lucky Talisman: Rocker key",
  "Positive Qualities: Deep understanding",
  "Negative Qualities: Depressed, pessimistic, escapism, and hypersensitive",
  "Symptoms: Deep understanding, understanding, intuitive, depressed, pessimistic escapism, and hypersensitive"
]

error = Fore.RED
comp = Fore.BLUE
user = Fore.WHITE

#-----------------Greeting
print(Fore.LIGHTMAGENTA_EX + 'Loading...')
source = audio.play_tone(1, 600, 1)
time.sleep(3)
print("\nLoaded")
source = audio.play_tone(0.25, 1500, 1)
time.sleep(1)
print('\n')

while True:
  print(comp + random.choice(greeting))
  greetingreply = TextBlob((input(user)).lower())
  if ('hi' in greetingreply and 'nothing' not in greetingreply) or 'hello' in greetingreply or 'hey' in greetingreply:
    continue
  else:
    break

emo = greetingreply.polarity

if ' and you' in greetingreply or 'about you' in greetingreply or 'you?' in greetingreply or 'are you' in greetingreply or 'hbu' in greetingreply or 'wbu' in greetingreply:
  print(comp + "Oh, I am having a" + random.choice(good) + " day so far! Thank you for asking!\n\nSo, what's your name?")
elif emo > 0:
  print(comp + "That's amazing! \n\nSo, what's your name?")
elif emo == 0:
  print(comp + "That's nice.\n\nSo, what's your name?")
elif emo < 0:
  print(
    comp +
    "Oh, that's fine, don't worry, you'll feel much better soon since you are chating with me heheeh, anyways...\n\nSo, what's your name?"
  )

name = input(user)
name = name.lower()

if "my name is " in name or "i'm " in name or "i am " in name:
  name = name.replace('my name is ', '')
  name = name.replace("i'm ", '')
  name = name.replace("i am ", '')

while len(name.split()) > 1 or len(name.split()) < 1:
  if "don't" in name or "no" in name or "not" in name:
    print(comp + "Oh, that's fine, I'm sorry for any offense, I swear didn't mean that \U0001F622\n\nAnyways, my name is Asta, a star Sign expert. I am an Aries, do you know what your", random.choice(sign), "is?")
    name = 'no'
    break
  if len(name.split()) > 1:
    print(comp + "\nWow, I'm sorry but I am really bad at memorising, your name is sooooo long \U0001F635. Just give me your first name please =.=")
    name = input(user)
    if len(name.split()) == 1:
      break
  if len(name.split()) < 1:
    print(comp + "Oh come on, don't kill our chat 🥹")
    print(comp + "What's your first name?")
    name = input(user)
    if len(name.split()) == 1:
      break

if name == 'no':
  pass
else:
  name = name.capitalize()
  print(comp + 'Awww', name, "That's such a",random.choice(adj), "name! ☆*:.o(≧▽≦)o.:*☆")
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
        astro_sign = (star.replace(star, x)).capitalize()
    if 'aries' in star or 'too' in star:
      print(comp + "That's", random.choice(adj), "\b! We got the same", random.choice(sign), "\b!")
    else:
      if star[-1] == 's':
        starplu = 'es'
      else:
        starplu = 's'
      print(comp + "Wow, " + random.choice(adj) + "! I always love " + astro_sign + starplu + ".")

#=====================if user don't know their star sign

if know == False:
  print(comp + "That's totally fine, most of my friends don't know their",
        random.choice(sign), "\bs.")

  #----------------------month

  print(comp + "Let's find out your", random.choice(sign),
        "then!\n\nWhich month were you born in?")
  month = (TextBlob(input(user)).correct()).lower()

  monthtf = False
  for x in months:
    if x in month:
      monthtf = True

  while monthtf == False:
    print(
      comp +
      "Sorry, you didn't answer with a valid month. Please check your spelling. Let's do this again."
    )
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
    print(comp + "\n" + random.choice(adj).capitalize(),
          "\b! And which day of", month.capitalize(),
          "\b? (please just type the number without 'th')")
    try:
      day = int(input(user))
      break
    except:
      print(error + "Please enter the NUMBER without 'th'!!!;-;")

  while day > 28 or day <= 0:
    if day <= 0:
      print(
        comp +
        "Haha, funny, but I believe we all know that our birthday datess must be a natural number. Please check with your parents again, I am sure you were born on an existing date. Let's do this again."
      )
      print(comp + "Which day of", month,
            "were you born in? (please just type the number without 'th')")
      try:
        day = int(input(user))
        break
      except:
        print(error + "Please enter the NUMBER without 'th'!!!;-;")
    #------------------31 months
    elif month in month31 and day > 31:
      print(
        comp +
        "Sorry, you didn't answer with a valid day. Please check with your parents again, I am sure you were born on an existing date. Let's do this again."
      )
      print(comp + "\nWhich day of", month,
            "were you born in? (please just type the number without 'th')")
      try:
        day = int(input(user))
      except:
        print(error + "Please enter the NUMBER without 'th'!!!;-;")
      if day <= 31:
        break
    elif month in month31 and day <= 31:
      break
    #------------------30 months
    elif month in month30 and day > 30:
      print(
        comp +
        "Sorry, you didn't answer with a valid day. Please check with your parents again, I am sure you were born on an existing date. Let's do this again."
      )
      print(comp + "\nWhich day of", month,
            "were you born in? (please just type the number without 'th')")
      try:
        day = int(input(user))
      except:
        print(error + "Please enter the NUMBER without 'th'!!!;-;")
      if day <= 31:
        break
    elif month in month30 and day <= 30:
      break
    #------------------29 months
    elif month == 'February' and day > 29:
      print(
        comp +
        "Sorry, you didn't answer with a valid day. Please check with your parents again, I am sure you were born on an existing date. Let's do this again."
      )
      print(comp + "\nWhich day of", month,
            "were you born in? (please just type the number without 'th')")
      try:
        day = int(input(user))
      except:
        print(error + "Please enter the NUMBER without 'th'!!!;-;")
      if day <= 31:
        break
    elif month == 'February' and day == 29:
      print(
        comp +
        "Wow, 29th of February! What a special birthday! \nDid you know that the chances of being born on leap day are so rare that less than 0.1 percent of the world's population is born on February 29? Anyways, haha."
      )
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

    if astro_sign[-1] == 's':
      starplu = 'es'
    else:
      starplu = 's'

    if astro_sign[0] == 'a' or astro_sign[0] == 'A' or astro_sign[
        0] == 'o' or astro_sign[0] == 'O':
      if astro_sign == 'Aries':
        print(comp + "Wow, you are an " + astro_sign + "! Just like me!")
        print(comp + "I like " + astro_sign + starplu + "!")
      else:
        print("\nWow, you are an " + astro_sign + "!")
        print(comp + "I like " + astro_sign + starplu + "!")
    elif month.lower() == 'february' and day == 29:
      print(comp + "You are a " + astro_sign + "!")
      print(comp + "I like " + astro_sign + starplu + "!")
    else:
      print(comp + "Wow, you are a " + astro_sign + "!")
      print(comp + "I like " + astro_sign + starplu + "!")
  starfun()

#------------------personalities

if astro_sign[-1] == 's':
  starplu = 'es'
else:
  starplu = 's'
  
print(comp + "\nWould you like to know about the personalities of " + astro_sign + starplu + "? (Insert 'Yes' for yes)")

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
  pass

if astro_sign[-1] == 's':
  starplu = 'es'
else:
  starplu = 's'

#-------------------fun facts

print(comp + '\nWould you like to know some interesting facts of ' + astro_sign + starplu + "?")
facts = (input(user)).lower()


funfact = False
for x in yes:
  if x in facts:
    funfact = True
  
  
while funfact == True:
  funfact = False
  for x in yes:
    if x in facts:
      funfact = True

  if funfact == False:
    funfact == False
    break

  if astro_sign == 'Aries':
      fact = Ariesfact
  if astro_sign == 'Taurus':
    fact = Taurusfact
  if astro_sign == 'Gemini':
    fact = Geminifact
  if astro_sign == 'Cancer':
    fact = Cancerfact
  if astro_sign == 'Leo':
    fact = Leofact
  if astro_sign == 'Virgo':
    fact = Virgofact
  if astro_sign == 'Libra':
    fact = Librafact
  if astro_sign == 'Scorpio':
    fact = Scorpiofact
  if astro_sign == 'Sagittarius':
    fact = Sagittariusfact
  if astro_sign == 'Capricorn':
    fact = Capricornfact
  if astro_sign == 'Aquarius':
    fact = Aquariusfact
  if astro_sign == 'Pisces':
    fact = Piscesfact
  
  x = 0
  while x >= 0:
    print(Fore.LIGHTMAGENTA_EX + "\n" + fact[x])
    print(comp + "\nWould you like to know more facts about your", random.choice(sign) + "?")
    facts = input(user)
    funfact = False
    for y in yes:
      if y in facts:
        funfact = True
    if funfact == True:
      x += 1
      if fact[x-1] == fact[-1]:
        print(comp + "\nOops, I'm sorry but I forgot I have ran out of fun facts about", astro_sign + starplu +"!")
        time.sleep(2)
        facts = 'no'
        break
    if funfact == False:
      facts = 'no'
      break  
if funfact == False:  
  print(comp + f"\nAlright then, it's nice to talk to you, {name}. However I got something important to do now, so I hope we can chat later in the fure. \nCya~")
  time.sleep(2)
  print(error + "\nAsta left the chat X﹏X")
