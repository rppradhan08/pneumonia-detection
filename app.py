from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import numpy as np
import os
import cv2

# Creating a Flask Instance
app = Flask(__name__)


IMAGE_SIZE = (150, 150)
UPLOAD_FOLDER = 'static\\uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

print("Loading Pre-trained Model ...")
model = load_model('model.h5')


def image_preprocessor(path):
    '''
    Function to pre-process the image before feeding to model.
    '''
    print('Processing Image ...')
    currImg_BGR = cv2.imread(path)
    b, g, r = cv2.split(currImg_BGR)
    currImg_RGB = cv2.merge([r, g, b])
    currImg = cv2.resize(currImg_RGB, IMAGE_SIZE)
    currImg = currImg/255.0
    currImg = np.reshape(currImg, (1, 150, 150, 3))
    return currImg


def model_pred(image):
    '''
    Perfroms predictions based on input image
    '''
    print("Image_shape", image.shape)
    print("Image_dimension", image.ndim)
    # Returns Probability:
    # prediction = model.predict(image)[0]
    # Returns class:
    prediction = model.predict_classes(image)[0]
    '''    if prediction == 1:
        return "Pneumonia"
    else:
        return "Normal"'''
    return (prediction)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # Checks if post request was submitted
    if request.method == 'POST':
        '''
        - request.url - http://127.0.0.1:5000/
        - request.files - Dictionaary of HTML elem "name" attribute and corrospondiong file details eg. 
        "imageFile" : <FileStorage: 'Profile_Pic.jpg' ('image/jpeg')>
        '''
        # check if the post request has the file part
        if 'imageFile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        # check if filename is an empty string
        file = request.files['imageFile']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # if file is uploaded
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            imgPath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(imgPath)
            print(f"Image saved at {imgPath}")
            # Preprocessing Image
            image = image_preprocessor(imgPath)
            # Perfroming Prediction
            pred = model_pred(image)
            return render_template('upload.html', name=filename, result=pred)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)