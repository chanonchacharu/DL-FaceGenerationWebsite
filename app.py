from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate_page():
    return render_template('generate.html')

@app.route('/generate-image', methods=['POST'])
def generate_images():
    initial_image_path, modified_image_path, features = generate_image()
    return render_template('generate.html', 
                           initial_image=initial_image_path, 
                           modified_image=modified_image_path, 
                           features=features)

if __name__ == '__main__':
    app.run(debug=True)
