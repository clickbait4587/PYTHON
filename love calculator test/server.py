from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template('index.html')

if __name__ == "__main__":
    
    app.run(debug=True)
