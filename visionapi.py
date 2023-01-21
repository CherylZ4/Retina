from google.cloud import vision
import io
def detect_text(path: str):
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read() #Open image and read image and capture contents into content
    image = vision.Image(content=content) #Use google vision to capture contents of image and store it as a different data type
    response = client.label_detection(image=image) #Get response from google api via google's vision python package and store response in response
    labels = response.label_annotations #Grab a list of items from response
    print (labels[0].description)
    """ for label in labels:
        print(label.description) """
detect_text("/home/conradm/Videos/IMG_0177.jpg")