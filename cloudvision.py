from google.cloud import vision
import io
def grabobjects(path):
    itemdict = {}
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations
    for object in objects:
        coordslist = []
        for i in range(4):
            y = object.bounding_poly.normalized_vertices[i].y
            x = object.bounding_poly.normalized_vertices[i].x
            vertexlist = [x, y]
            coordslist.append(vertexlist)
        itemdict[object.name] = coordslist
    print(itemdict)
    return(itemdict)

grabobjects('/home/conradm/GitHub/Retina/23-01-21-07:41:58.jpg')