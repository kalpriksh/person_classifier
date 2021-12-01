import wavelet
import face_finder
import base64
import numpy as np
import cv2
import joblib
import json

__class_name_to_index = {}
__class_index_to_name = {}

__model = None

def classify_image(b64_image_data=None, file_path=None):
  
  faces = face_finder.face_finder(image_data=b64_image_data)
  result = []
  if len(faces) == 0 or faces is None:
    print("no face found")
    return
  try:
    X = []
    for face in faces:
      img = face
      img_scaled = cv2.resize(img, (64,64))
      img_wave_transformed = wavelet.w2d(img_scaled, 'db1', 5)
      img_wave_transformed_scaled = cv2.resize(img_wave_transformed, (64,64))
      img_combined = np.vstack((img_scaled.reshape(64*64*3,1), img_wave_transformed_scaled.reshape(64*64,1)))
      X.append(img_combined)
    
    X = np.array(X).reshape(len(X), 16384).astype(float)

    result.append(__model.predict(X)[0])
  except Exception as e:
    print(e)

  return result

def get_b64_image():
  with open("./server/b64.txt") as f:
    return f.read()



def load_saved_artifacts():
  print('Loading saved artifacts....')
  
  global __class_index_to_name
  global __class_name_to_index
  
  with open('./server/artifacts/person_dict.json', 'r') as f:
    __class_name_to_index = json.load(f)
    __class_index_to_name = {v:k for k,v in __class_name_to_index.items()}
    
  global __model
  if __model is None:
    with open('./server/artifacts/saved_model.pkl', 'rb') as f:
      __model = joblib.load(f)
  
  print('Loading Complete.....')

if __name__ == '__main__':
  load_saved_artifacts()
  print(classify_image(get_b64_image(), None))