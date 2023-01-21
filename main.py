import photoshoot
import cloudvision
import cohereapi

photoshoot.openCam()
itemname = cloudvision.grabobjects('/home/conradm/GitHub/Retina/capture.jpg')
print(f'Your item is {itemname}')
print(f'{itemname} is {cohereapi.grabDefinition(itemname)}')