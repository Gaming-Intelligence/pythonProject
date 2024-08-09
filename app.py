from flask import Flask, render_template
import threading
import subprocess

app = Flask(__name__)

def run_game():
    subprocess.run(["python", "main.py"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    threading.Thread(target=run_game).start()
    return "Game started!"

if __name__ == '__main__':
    app.run(debug=True)
