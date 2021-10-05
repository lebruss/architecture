#code: leb
#design: ann ja lukas
import random
while True:
    buildingList = ['library', 'church', 'kiosk', 'grocery store', 'condominium', 'apartment', 'school', 'club', 'bunker', 'disco', 'firehouse', 'police station', 'family home', 'garage']
    maakonnad = ['Harjumaa', 'Hiiumaa', 'Ida-Virumaa', 'Jõgevamaa', 'Järvamaa', 'Läänemaa', 'Lääne-Virumaa', 'Põlvamaa', 'Pärnumaa', 'Raplamaa', 'Saaremaa', 'Tartumaa', 'Valgamaa', 'Viljandimaa', 'Võrumaa']
    building = (random.choice(buildingList))
    roomAmount = (random.randint(1,9))
    area = (roomAmount * (random.randint(10,40)))
    floors = (random.randint(1, (roomAmount)))
    maakond = (random.choice(maakonnad))
    print("Please design a %d floor, %d room %s, of area %s square meters in %s." % (floors, roomAmount, building, area, maakond))
    #room = 1
    #while room <= roomAmount:
        #print(room)
        #room = room + 1
    input()
