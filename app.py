from flask import Flask, render_template, request, Response, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"name" : "mufasa"})  # jsonify converts a JS object into a json

if __name__ == "__main__":
    app.run(debug=True)