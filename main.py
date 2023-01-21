import photoshoot
import cloudvision
import cohereapi

time = photoshoot.openCam()
print("Photo taken")
itemdict = cloudvision.grabobjects(f'/home/conradm/GitHub/Retina/{time}.jpg')
print(f"Grabbed item list from photo ({len(itemlist)})")
for items in itemdict:
    if items[len(items)-1] == 's':
        print(f'{items} are{cohereapi.grabDefinition(items)}')
    else:
        print(f'{items} is{cohereapi.grabDefinition(items)}')