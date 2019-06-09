import io
import json
from google.protobuf.json_format import MessageToJson

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    response = MessageToJson(response)
    dictionary = json.loads(response)
    if len(dictionary) > 0:
        text_annotations = dictionary["textAnnotations"]
        for i in text_annotations:
            if i['description'] == '#':
                index = text_annotations.index(i)
    #           print(index)
                line = (text_annotations[index+1])
                return line['description']
    else:
        return None





print(detect_text('C:/Users/warof/Desktop/skool/sutd/year 2/term 5/30.007/google cloud vision/sing_toast.jpg'))