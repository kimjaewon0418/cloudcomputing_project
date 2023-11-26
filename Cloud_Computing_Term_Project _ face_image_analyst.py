import boto3
import json
def detect_faces(photo, bucket):
    client=boto3.client('rekognition')
    response = client.detect_faces(Image={'S3Object':
{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])
    
    print('Detected faces for ' + photo)
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])

            + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')

        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))
 
    # Access predictions for individual face details and print them
        print("Gender: " + str(faceDetail['Gender']))
        print("Smile: " + str(faceDetail['Smile']))
        print("Eyeglasses: " + str(faceDetail['Eyeglasses']))
        print("Emotions: " + str(faceDetail['Emotions'][0]))
        return len(response['FaceDetails'])

def main():
    photo='한소희.jpg'
    bucket='jaewon'
    face_count=detect_faces(photo, bucket)
    print("Faces detected: " + str(face_count))
    photo='한소희2.jpg'
    bucket='jaewon'
    face_count=detect_faces(photo, bucket)
    print("Faces detected: " + str(face_count))

if __name__ == "__main__":
    main() #얼굴분석
