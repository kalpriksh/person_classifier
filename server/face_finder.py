import cv2
import numpy as np
import base64

def get_cv2_image_from_b64(b46_image):
  encoded_data = b46_image.split(',')[1]
  nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
  img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  return img

# finds faces in image for path and returns cropped face.
def face_finder(image_data=None, image_path=None):
  # haar classifier defined
  
  face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
  eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

  image_ = ''
  image_gray = ''
  try:
    if image_data is not None:
      image_ = get_cv2_image_from_b64(image_data)
    elif image_path is not None:
      image_ = cv2.imread(image_path)
      
    image_gray = cv2.cvtColor(image_, cv2.COLOR_RGB2GRAY)
  except Exception as e:
    print(e)
    return
    
  faces = face_cascade.detectMultiScale(image_gray)
  
  cropped_face_images = []
  
  for (x, y, w, h) in faces:
    cropped_image = image_[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(image_gray[y:y+h,x:x+w])
    # if len(eyes) > 1:
    if cropped_image is not None:
      cropped_face_images.append(cropped_image)
  
  return cropped_face_images
