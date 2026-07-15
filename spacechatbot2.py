import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from PIL import Image, ImageFilter
import speech_recognition as sr
#from deep_translator import GoogleTranslator 
#from textblob import TextBlob

def space_voice(): 
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for background noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source,duration=2)
        print("Listening... Speak something!")
        audio = recognizer.listen(source)
    voice_query = recognizer.recognize_google(audio)   
    return voice_query
a = space_voice()
print(a)


def check(c):
    check = ["across""left", "over","earliest","appearance","form","gets","its","final","stars","limit","exceeds","become","cannot","would","percentage","existence","come","theory","describe", "region","separates","really","more","matters",
             "years","many","towards","each other","far","will","nearest","happening","center",
             "powers","extreme","active","output","from","such","between","amounts","energy","relationship","objects","most","makes","What", "is","the","to","how","can","you","of","explain","a","an","when","there","many","do","mean",""]
    filter = [word for word in c if word.lower() not in check]
    word2 = check_in(filter)
    return word2
 
def check_in(words):
    check1 =["chandrashekhar","checkspacde","gravity","Habitable","Zone","Fermiparadox","exoplanet","Earth","tides","DrakeEquation","Cassini","Asteroids","asteroids","Cosmiceffect","Doppler","Geostationary","invisible","emit","structure","cosmic","web","microwave","ancient","earth","sun","glowing","tail","comet","fate","collapsing","dwarf","chandrasekhar","unfamiliar","escape","black hole","two stars","binary","big bang",
            "origin","scientific explanation","inner planets","quasar","galactic nucleus","Andromeda Galaxy","collide","merge","antimatter"]
    filter =[word for word in words if word.lower() in check1]        
    return filter

def Activegalactic():
    with open("D:\Python_programs\Space Chatbot\Active galactic nucleus.txt",'r') as galacticnucleus:
        a = galacticnucleus.read()
    return a

def AndromedaGalaxy():
    with open("D:\Python_programs\Space Chatbot\Andromeda Galaxy.txt",'r') as Andgalaxy:
        a = Andgalaxy.read()
    return a

def Andromedatype():
    with open("D:\Python_programs\Space Chatbot\Andromeda Galaxytype.txt",'r') as Andromedatype:
        a = Andromedatype.read()
    return a

def antimatter():
    with open("D:\Python_programs\Space Chatbot\Antimatter.txt",'r') as antimatter1:
        a = antimatter1.read()
    return a

def asteroid_belt():
    with open("D:\Python_programs\Space Chatbot\ asteroid_belt.txt",'r') as asteroidbelt1:
        a = asteroidbelt1.read()
    return a

def bigbang():
    with open("D:\Python_programs\Space Chatbot\BigBangtheory.txt",'r') as BigBangtheory:
        a = BigBangtheory.read()
    return a

def binary_star():
    with open("D:\Python_programs\Space Chatbot\binary_star.txt",'r') as binarystar:
        a = binarystar.read()
    return a

def black_hole():
    with open("D:\Python_programs\Space Chatbot\black_hole.txt",'r') as blackhole:
        a = blackhole.read()
    return a

def chandrasekhar():
    with open("D:\Python_programs\Space Chatbot\chandrasekhar_limit.txt",'r') as chandrasekhar1:
        a = chandrasekhar1.read()
    return a

def spacecheck():
    with open("D:\Python_programs\Space Chatbot\check space.txt",'r') as checkspace:
        a = checkspace.read()
    return a

def spacefile():
  a = input("how we can help you: ") 
  if a == "ArtificialSatellite":
   x = pd.read_excel("D:\Python_programs\Space Chatbot\ArtificialSatellite.xlsx")
   return x

  elif a == "Asteroids":
   x = pd.read_excel("D:\Python_programs\Space Chatbot\AsteroidsComet.xlsx")
   return x

  elif a == "Cassini":
   x = pd.read_excel("D:\Python_programs\Space Chatbot\Cassini.xlsx")
   return x

  elif a == "Drakeequation":
   x = pd.read_excel("D:\Python_programs\Space Chatbot\DrakeEquation.xlsx")
   return x

  elif a == "Earth":
   x = pd.read_excel("D:\Python_programs\Space Chatbot\EarthTides.xlsx")
   return x

  elif a == "Exoplanet":
    x = pd.read_excel("D:\Python_programs\Space Chatbot\Exoplanet.xlsx")
    return x

  elif a == "Fermiparadox":
    x = pd.read_excel("D:\Python_programs\Space Chatbot\Fermi Paradox.xlsx")
    return x  

  elif a == "Habitable":
    x = pd.read_excel("D:\Python_programs\Space Chatbot\HabitableZone.xlsx")
    return x

  elif a == "gravity":
    x = pd.read_excel("D:\Python_programs\Space Chatbot\gravity.xlsx")
    return x

  else:
    print("no answer")

def space_image():
  a = input("enter the image")
  if a == "Accretion":
   b = Image.open('D:\Python_programs\Space Chatbot\Accretion disk.jpg')
   display(b)
   
  elif a == "cosmic":
    b = Image.open('D:\Python_programs\Space Chatbot\Cosmiceffect.jpg')
    display(b)

  elif a == "DopplerEffect":
   b= Image.open('D:\Python_programs\Space Chatbot\DopplerEffect.jpg')
   display(b)

  elif a == "Geostationary":
   b =Image.open('D:\Python_programs\Space Chatbot\GeostationaryOrbit.jpg')
   display(b)

  else:
    print('no images are found')

a = input("enter the query")
#translated_query = GoogleTranslator(source='en', target='hi').translate(a)
#print(translated_query)
b = a.lower()
c = b.split()
print(c)
key = ' '.join(check(c))
print(key)

if key == 'Activegalactic' or key == 'nucleus':
    a = Activegalactic()
    print(a)

elif key == 'Andromeda' or key == 'galaxy':
    a = AndromedaGalaxy()
    print(a)

elif key == 'Andromeda Galaxy' or key == 'type':
    a = Andromedatype()
    print(a)

elif key == 'antimatter':
    a = antimatter()
    print(a)

elif key == 'asteroid' or key == 'belt':
    a = asteroid_belt()
    print(a)

elif key == 'bigbang' or key == 'theory':
    a = bigbang()
    print(a)

elif key == 'binarystar':
    a = binary_star()
    print(a)

elif key == 'black' or key == 'hole':
    a = black_hole()
    print(a)

elif key == 'chandrasekhar':
    a = chandrasekhar()
    print(a)

elif key == 'checkspace':
    a = spacecheck()
    print(a)

elif key == 'accretion':
  x = space_image()
  print(x)

elif key == 'Cosmiceffect':
  x = space_image()
  print(x)

elif key == 'Doppler':
  x = space_image()
  print(x)

elif key == 'Geostationary':
  x = space_image()
  print(x)

elif key == 'active' or key =='nucleus':
    y = Activegalactic()
    print(y)

elif key == 'artificial' or key == 'satellite':
    z = spacefile()
    print(z)

elif key == 'Asteroids' or key == 'asteroids':
    z = spacefile()
    print(z)

elif key == 'Cassini':
    z = spacefile()
    print(z)

elif key == 'DrakeEquation':
    z = spacefile()
    print(z)

elif key == 'Earth' or key == 'tides':
    z = spacefile()
    print(z)

elif key == 'exoplanet':
    z = spacefile()
    print(z)

elif key == 'Fermiparadox':
    z = spacefile()
    print(z)

elif key == 'Habitable' or key == 'Zone':
    z = spacefile()
    print(z)

elif key == 'gravity':
    z = spacefile()
    print(z)

else:
  print("Invalid input")


d1 = 'Activegalatic'
d2 = 'Andromedagalaxy'
d3 = 'Andromedatype'
d4 = 'antimatter'
d5 = 'asteroidbelt'
d6 = 'bigbangtheory'
d7 = 'binarystar'
d8 = 'blackhole'
d9 = 'chandrasekharlimit'
d10 = 'spacecheck'
d11 = 'ArtificialSatellite'
d12 = 'AsteroidsComet'
d13 = 'Cassini'
d14 = 'Drakeequation'
d15 = 'Earthtides'
d16 = 'europajupiter'
d17 = 'exoplanet'
d18= 'fermiparadox'
d19 = 'gravity'
d20 = 'habitablezone'
d21 = 'Accretiondisk'
d22 = 'Cosmiceffect'
d23 = 'DopplerEffect'
d24 = 'Geostationaryorbit'
d25 = 'Gravitywork'

e1 = fuzz.WRatio(d1,key)
e2 = fuzz.WRatio(d2,key)
e3 = fuzz.WRatio(d3,key)
e4 = fuzz.WRatio(d4,key)
e5 = fuzz.WRatio(d5,key)
e6 = fuzz.WRatio(d6,key)
e7 = fuzz.WRatio(d7,key)
e8 = fuzz.WRatio(d8,key)
e9 = fuzz.WRatio(d9,key)
e10 = fuzz.WRatio(d10,key)
e11 = fuzz.WRatio(d11,key)
e12 = fuzz.WRatio(d12,key)
e13 = fuzz.WRatio(d13,key)
e14 = fuzz.WRatio(d14,key)
e15 = fuzz.WRatio(d15,key)
e16 = fuzz.WRatio(d16,key)
e17 = fuzz.WRatio(d17,key)
e18 = fuzz.WRatio(d18,key)
e19 = fuzz.WRatio(d19,key)
e20 = fuzz.WRatio(d20,key)
e21 = fuzz.WRatio(d21,key)
e22 = fuzz.WRatio(d22,key)
e23 = fuzz.WRatio(d23,key)
e24 = fuzz.WRatio(d24,key)
e25 = fuzz.WRatio(d25,key)

if e1 >= 60:
    print("Activegalatic =",e1)
    f1= Activegalactic()
    print(f1)
elif e2>= 60:
    print("Andromedagalaxy=",e2)
    f2 = AndromedaGalaxy()
    print(f2)
elif e3>= 60:
    print("Andromedatype =",e3)
    f3 = Andromedatype()
    print(f3)
elif e4 >= 60:
    print("Antimatter =",e4)
    f4 = antimatter()
    print(f4)
elif e5 >= 60:
    print("asteroidbelt =",e5)
    f5 = asteroid_belt()
    print(f5)

elif e6 >= 60:
    print("bigbangtheory =",e6)
    f6 = bigbang()
    print(f6)

elif e7 >= 60:
    print("binarystar =",e7)
    f7 = binary_star()
    print(f7)

elif e8 >= 60:
    print("blackhole =",e8)
    f8 = black_hole()
    print(f8)

elif e9 >= 60:
    print("chandrasekharlimit =",e9)
    f9 = chandrasekhar()
    print(f9)

elif e10 >= 60:
    print("spacecheck =",e10)
    f10 = spacecheck()
    print(f10)

elif e11 >= 60:
    print("ArtificialSatellite =",e11)
    f11 = spacefile()
    print(f11)

elif e12 >= 60:
    print("AsteroidsComet =",e12)
    f12 = spacefile()
    print(f12)

elif e13 >= 60:
    print("Cassini =",e13)
    f13 = spacefile()
    print(f13)

elif e14 >= 60:
    print("Drakeequation =",e14)
    f14 = spacefile()
    print(f14)

elif e15 >= 60:
    print("Earthtides =",e15)
    f15 = spacefile()
    print(f15)

elif e16 >= 60:
    print("europajupiter=",e16)
    f16 = spacefile()
    print(f16)

elif e17 >= 60:
    print("exoplanet =",e17)
    f17 = spacefile()
    print(f17)

elif e18 >= 60:
    print("fermiparadox=",e18)
    f18 = spacefile()
    print(f18)

elif e19 >= 60:
    print("gravity=",e19)
    f19 = spacefile()
    print(f19)

elif e20 >= 60:
    print("habitablezone =",e20)
    f20 = spacefile()
    print(f20)


elif e21 >= 60:
    print("Accretiondisk =",e21)
    f21 = space_image()
    print(f21)


elif e22 >= 60:
    print("Cosmiceffect =",e22)
    f22 = space_image()
    print(22)

elif e23 >= 60:
    print("DopplerEffect=",e23)
    f23 = space_image()
    print(f23)

elif e24 >= 60:
    print("Geostationaryorbit =",e24)
    f24 = space_image()
    print(f24)

elif e25 >= 60:
    print("Gravitywork=",e25)
    f25 = space_image()
    print(f25)
else :
    print('again enter the question')






K = input('enter the the value')
print(K)






