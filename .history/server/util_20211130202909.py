import wavelet
import face_finder
import base64
import numpy as n

def classify_image(image_data, file_path=None):
  face_finder.face_finder(image_data)
  return

def get_cv2_image_from_b64(b46_image):
  encoded_data = b46_image.split(',')[1]
  nparr = np.frombuffer(base64.b64decode(encoded_data), np.unit8)

def get_b64_image():
  with open("b64.txt") as f:
    return f.read()


if __name__ == '__main__':
  