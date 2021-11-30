import wavelet
import face_finder
import base64
import numpy as np
import cv2

def classify_image(b64_image_data=None, file_path=None):
  faces = face_finder.face_finder(image_data=b64_image_data)
  X = []
  
  for face in faces:
    img = face
    img_scaled = cv2.resize(img, (64,64))
    img_wave_transformed = wavelet.w2d(img_scaled, 'db1', 5)
    img_wave_transformed_scaled = cv2.resize(img_wave_transformed, (64,64))
    img_combined = np.vstack((img_scaled.reshape(64*64*3,1), img_wave_transformed_scaled.reshape(64*64,1)))
  
  return

# for person, images in image_file_path.items():
#   for image_path in images:
#     img = cv2.imread(image_path)
#     if img is not None:
#       img_scaled = cv2.resize(img, (64,64))
#       img_wave_transformed = w2d(img_scaled, 'db1', 5)
#       img_wave_transformed_scaled = cv2.resize(img_wave_transformed, (64,64))
      
#       img_combined = np.vstack((img_scaled.reshape(64*64*3,1), img_wave_transformed_scaled.reshape(64*64,1)))
      
#       X.append(img_combined)
#       y.append(person_dict[person])
  
  
#   return

def get_cv2_image_from_b64(b46_image):
  encoded_data = b46_image.split(',')[1]
  nparr = np.frombuffer(base64.b64decode(encoded_data), np.unit8)
  img = cv2.imdecode()(nparr, cv2.IMREAD_COLOR)
  return img

def get_b64_image():
  with open("b64.txt") as f:
    return f.read()


if __name__ == '__main__':
  