from flask import Flask, render_template, request, jsonify
import sys
import io

# Import the game wrapper
import game_wrapper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    command = request.json.get('command')
    
    # Run the game command and get its output
    output = game_wrapper.run_game_command(command)

    return jsonify({'output': output})

if __name__ == '__main__':
    # Replit typically runs your app using 'gunicorn' or similar
    # For local testing, you can run this directly
    app.run(host='0.0.0.0', port=8080)
