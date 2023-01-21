import photoshoot
import cloudvision
import cohereapi

photoshoot.openCam()
print("Photo taken")
itemlist = cloudvision.grabobjects('/home/conradm/GitHub/Retina/capture.jpg')
print("Grabbed item list from photo")
for items in itemlist:
    if items[len(items)-1] == 's':
        print(f'{items} are{cohereapi.grabDefinition(items)}')
    else:
        print(f'{items} is{cohereapi.grabDefinition(items)}')