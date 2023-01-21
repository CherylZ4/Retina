import photoshoot
import cloudvision
import cohereapi

photoshoot.openCam()
print("Photo taken")
itemlist = cloudvision.grabobjects('/home/conradm/GitHub/Retina/capture.jpg')
for items in itemlist:
    print(f'{items} is {cohereapi.grabDefinition(items)}')