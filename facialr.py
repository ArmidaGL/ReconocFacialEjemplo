from deepface import DeepFace
obj = DeepFace.analyze(img_path = "/home/armida/Documents/GitHub/ReconocFacialEjemplo/python/facedetection/cam_photos/aa.jpg", actions = ['age', 'gender', 'race', 'emotion'],enforce_detection=False)
print (obj)
