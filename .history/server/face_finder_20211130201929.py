import cv2


# finds faces in image for path and returns cropped face.
def face_finder(image_path=''):
  # haar classifier defined
  face_cascade = cv2.CascadeClassifier(r'C:\Users\kalpr\.conda\pkgs\libopencv-4.0.1-hbb9e17c_0\Library\etc\haarcascades\haarcascade_frontalface_default.xml')
  eye_cascade = cv2.CascadeClassifier(r'C:\Users\kalpr\.conda\pkgs\libopencv-4.0.1-hbb9e17c_0\Library\etc\haarcascades\haarcascade_eye.xml')

  image_ = ''
  image_gray = ''
  try:
    image_ = cv2.imread(image_path)
    image_gray = cv2.cvtColor(image_, cv2.COLOR_RGB2GRAY)
  except Exception as e:
    print(e)
    return
    
  faces = face_cascade.detectMultiScale(image_gray)
  
  return faces
  #check if only a single face is found
  # if len(faces) == 1:
  #   # check if there are two eyes
  #   eyes = eye_cascade.detectMultiScale(image_gray)
  #   if len(eyes) > 1:
  #     # return cropped image
  #     (x, y, w, h) = faces[0]
  #     image_cropped = image_[y:y+h, x:x+w]
  #     return image_cropped
  #   else:
  #     return
  # else:
  #   return
