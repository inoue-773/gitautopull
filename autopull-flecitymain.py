from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/repo1', methods=['POST'])
def repo1():
    if request.method == 'POST':
        data = request.json
        # Validate the payload
        if 'resource' in data and 'refUpdates' in data['resource']:
            # Change to the directory of your local repo
            os.chdir('your_local_repo_directory')
            # Pull the latest changes
            result = subprocess.run(['git', 'pull', 'origin', 'master'], capture_output=True, text=True, shell=True)
            return jsonify({'message': 'Git pull executed in repo1', 'output': result.stdout}), 200
        else:
            return jsonify({'message': 'Invalid payload'}), 400
    else:
        return jsonify({'message': 'Invalid request method'}), 405
    
@app.route('/repo2', methods=['POST'])
def repo2():
    if request.method == 'POST':
        data = request.json
        # Validate the payload
        if 'resource' in data and 'refUpdates' in data['resource']:
            # Change to the directory of your local repo
            os.chdir('your_local_repo_directory')
            # Pull the latest changes
            result = subprocess.run(['git', 'pull', 'origin', 'master'], capture_output=True, text=True, shell=True)
            return jsonify({'message': 'Git pull executed in repo2', 'output': result.stdout}), 200
        else:
            return jsonify({'message': 'Invalid payload'}), 400
    else:
        return jsonify({'message': 'Invalid request method'}), 405

@app.route('/repo3', methods=['POST'])
def repo3():
    if request.method == 'POST':
        data = request.json
        # Validate the payload
        if 'resource' in data and 'refUpdates' in data['resource']:
            # Change to the directory of your local repo
            os.chdir('your_local_repo_directory')
            # Pull the latest changes
            result = subprocess.run(['git', 'pull', 'origin', 'master'], capture_output=True, text=True, shell=True)
            return jsonify({'message': 'Git pull executed in repo3', 'output': result.stdout}), 200
        else:
            return jsonify({'message': 'Invalid payload'}), 400
    else:
        return jsonify({'message': 'Invalid request method'}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=999)
