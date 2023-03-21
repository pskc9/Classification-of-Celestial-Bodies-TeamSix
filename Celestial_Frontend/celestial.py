import flask
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/krishna/Desktop/Celestial_Frontend/UPLOAD_FOLDER/' # the media directory from where it can be accessed (should be in the same repository as the code)
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'} # the allowed extensions of media for processing 

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('celestial.html') #the template html code written for frontenmd deployment (should be in the same repository as the code, under another folder named templates)

@app.route('/', methods=['POST'])  #type of API retrieval method
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename): #verify the allowed media files
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))

@app.route('/uploads/<filename>') #retrieval of the image upon action on upload button  
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == '__main__':
    app.run(debug=True)

'''if __name__ == '__main__':
    app.run(debug=False) #default methods anyways'''
