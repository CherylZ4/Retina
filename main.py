import photoshoot
import cloudvision
import cohereapi

time = photoshoot.openCam()
print("Photo taken")
#itemdict = cloudvision.grabobjects(f'{time}.jpg')
itemdict = cloudvision.grabobjects('current.jpg')
print(f"Grabbed item list from photo ({len(itemdict)})")
for items in itemdict:
    if items[len(items)-1] == 's':
        print(f'{items} are{cohereapi.grabDefinition(items)}')
    else:
        print(f'{items} is{cohereapi.grabDefinition(items)}')