from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from keras.applications.vgg19 import preprocess_input

filepath = r'D:\Academics_GCEK\5th_Sem\Mini_Project\Project\best_model1.h5'

model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

def Pred_Leaf_Disease(path):
  test_image = load_img(path, target_size = (256, 256)) # load image 
  print("@@ Got Image for prediction")

  imgg = img_to_array(test_image) # convert image to np array and normalize

  img = preprocess_input(imgg)

  test_image = np.expand_dims(img, axis = 0) # change dimention 3D to 4D

  result = model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)

  pred = np.argmax(result, axis=1)
  print(pred[0])
  
  if pred==0:
    return "Apple - Apple Scab Disease", 'Apple-Scab.html'

  elif pred==1:
    return "Apple - Black Rot Disease", 'Apple-Black-rot.html'

  elif pred==2:
    return "Apple - Cedar Rust Disease", 'Apple-Cedar_rust.html'

  elif pred==3:
    return "Apple - Healthy And Fresh", 'Apple -Healthy.html'

  elif pred==4:
    return "BlueBerry - Healthy and Fresh", 'BlueBerry -Healthy.html'

  elif pred==5:
    return "Cherry - Powdery Mildew Disease", 'Cherry-Powdery_Mildew.html'

  elif pred==6:
    return "Cherry - Healthy(including Sour)", 'Cherry-Healthy.html'

  elif pred==7:
    return "Corn - Grey Leaf Spot Disease", 'Corn-GreyLeafSpot.html'

  elif pred==8:
    return "Corn - Common Rust Disease", 'Corn-CommonRust.html'

  elif pred==9:
    return "Corn - Northern Leaf Blight Disease", 'Corn-NorthernLeafBlight.html'

  elif pred==10:
    return "Corn - Healthy And Fresh", 'Corn-Healthy.html'

  elif pred==11:
    return "Grape - Black Rot Disease", 'Grape-BlackRot.html'

  elif pred==12:
    return "Grape - Esca (Black Measles) Disease", 'Grape-BlackMeasles.html'

  elif pred==13:
    return "Grape - Leaf Blight(Isariopsis Leaf Spot) Disease", 'Grape-LeafBlight.html'

  elif pred==14:
    return "Grape - Healthy", 'Grape-Healthy.html'

  elif pred==15:
    return "Orange - Citrus Greening(HUanglongbing) Disease", 'Orange-CitrusGreening.html'

  elif pred==16:
    return "Peach - Bacterial spot Disease", 'Peach-BacterialSpot.html'

  elif pred==17:
    return "Peach - Healthy", 'Peach-Healthy.html'

  elif pred==18:
    return "Pepper - Bacterial spot Disease", 'Pepper-BacterialSpot.html'

  elif pred==19:
    return "Pepper - Healthy", 'Pepper-Healthy.html'

  elif pred==20:
    return "Potato - Early Blight Disease", 'Potato-EarlyBlight.html'

  elif pred==21:
    return "Potato - Late Blight Disease", 'Potato-LateBlight.html'

  elif pred==22:
    return "Potato - Healthy", 'Potato-Healthy.html'

  elif pred==23:
    return "Raspberry - Healthy", 'Raspberry-Healthy.html'

  elif pred==24:
    return "Soybean - Healthy", 'Soybean-Healthy.html'

  elif pred==25:
    return "Squash - Powdery mildew Disease", 'Squash-PowderyMildew.html'

  elif pred==26:
    return "Strawberry - Leaf scorch Disease", 'Strawberry-LeafScorch.html'

  elif pred==27:
    return "Strawberry - Healthy Disease", 'Strawberry-Healthy.html'

  elif pred==28:
    return "Tomato - Bacterial Spot Disease", 'Tomato-BacterialSpot.html'

  elif pred==29:
    return "Tomato - Early Blight Disease", 'Tomato-EarlyBlight.html'

  elif pred==30:
    return "Tomato - Late Blight Disease", 'Tomato-LateBlight.html'

  elif pred==31:
    return "Tomato - Leaf Mold Disease", 'Tomato-LeafMold.html'

  elif pred==32:
    return "Tomato - Septoria Leaf Spot Disease", 'Tomato-SeptoriaLeafSpot.html'

  elif pred==33:
    return "Tomato - Spider Mites(Two Spotted) Disease", 'Tomato-TwoSpottedSpiderMite.html'

  elif pred==34:
    return "Tomato - Target Spot Disease", 'Tomato-TargetSpot.html'

  elif pred==35:
    return "Tomato - Yellow Leaf Curl Virus", 'Tomato-YellowLeafCurlVirus.html'

  elif pred==36:
    return "Tomato - Mosaic Virus Disease", 'Tomato-MosaicVirus.html'

  elif pred==37:
    return "Tomato - Healthy", 'Tomato-Healthy.html'




# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')


# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)

        file_path = os.path.join('static/upload', filename)
        file.save(file_path)
        # print("file_path = ", file_path)
        print("@@ Predicting class......")
        pred, output_page = Pred_Leaf_Disease(path=file_path)

        return render_template(output_page, pred_output = pred, user_image = file_path, filename=filename)

# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=8080) 