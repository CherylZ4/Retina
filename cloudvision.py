from google.cloud import vision
import io
def grabobjects(path):
    itemlist = []
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations
    for object in objects:
        itemlist.append(object.name)
    return(itemlist)