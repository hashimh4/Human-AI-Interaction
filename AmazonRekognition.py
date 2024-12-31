import boto3
import csv
from PIL import Image

# Ensure that you cd to Downloads

rekognition = boto3.client('rekognition',aws_access_key_id="",
             aws_secret_access_key="",
             region_name="")

with open("harold.jpg", 'rb') as image_data:
     response_content = image_data.read()
rekognition_response = rekognition.detect_faces(Image={'Bytes':response_content}, Attributes=['ALL'])

# rekognition_response = rekognition.detect_faces(Image={'S3Object': {'Bucket': BUCKET_NAME, 'Name': file_key}}, Attributes=['ALL'])

image = Image.open("harold.jpg")
image_width, image_height = image.size

i = 1
for item in rekognition_response.get('FaceDetails'):
    bounding_box = item['BoundingBox']
    width = image_width * bounding_box['Width']
    height = image_height * bounding_box['Height']
    left = image_width * bounding_box['Left']
    top = image_height * bounding_box['Top']

    left = int(left)
    top = int(top)
    width = int(width) + left
    height = int(height) + top

    box = (left, top, width, height)
    box_string = (str(left), str(top), str(width), str(height))
    cropped_image = image.crop(box)
    thumbnail_name = '{}.png'.format(i)
    i += 1
    cropped_image.save(thumbnail_name, 'PNG')

    face_emotion_confidence = 0
    face_emotion = None
    for emotion in item.get('Emotions'):
        if emotion.get('Confidence') >= face_emotion_confidence:
            face_emotion_confidence = emotion['Confidence']
            face_emotion = emotion.get('Type')
    print('{} - {} - {}'.format(thumbnail_name, face_emotion, face_emotion_confidence))