from flask import Flask, request, jsonify
import os
import subprocess
import requests
from datetime import datetime

app = Flask(__name__)

DISCORD_WEBHOOK_URL = 'discord_webhook_here'

def send_discord_message(message):
    data = {
        "content": message
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    return response

def execute_git_pull(directory):
    os.chdir(directory)
    result = subprocess.run(['git', 'pull', 'origin', 'master'], capture_output=True, text=True, shell=True)
    return result

def format_commit_message(commit):
    author = commit['author']['name']
    date = datetime.strptime(commit['author']['date'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
    comment = commit['comment']
    files = commit.get('url', 'N/A')  # URL can be used to identify the commit details, which includes files changed
    return f"**Author:** {author}\n**Date:** {date}\n**Files:** {files}\n**Comment:** {comment}\n"

@app.route('/repo1', methods=['POST'])
def repo1():
    if request.method == 'POST':
        data = request.json
        # Validate the payload
        if 'resource' in data and 'refUpdates' in data['resource']:
            commit_messages = [format_commit_message(commit) for commit in data['resource']['commits']]
            commit_message = "\n".join(commit_messages)
            # Send the commit message to Discord
            send_discord_message(f"New commits in repo1:\n{commit_message}")

            # Change to the directory of your local repo and pull the latest changes
            result = execute_git_pull('your_git_local_directory')

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
            commit_messages = [format_commit_message(commit) for commit in data['resource']['commits']]
            commit_message = "\n".join(commit_messages)
            # Send the commit message to Discord
            send_discord_message(f"New commits in repo2:\n{commit_message}")

            # Change to the directory of your local repo and pull the latest changes
            result = execute_git_pull('your_git_local_directory')

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
            commit_messages = [format_commit_message(commit) for commit in data['resource']['commits']]
            commit_message = "\n".join(commit_messages)
            # Send the commit message to Discord
            send_discord_message(f"New commits in Flecityrepo3:\n{commit_message}")

            # Change to the directory of your local repo and pull the latest changes
            result = execute_git_pull('your_git_local_directory')

            return jsonify({'message': 'Git pull executed in repo3', 'output': result.stdout}), 200
        else:
            return jsonify({'message': 'Invalid payload'}), 400
    else:
        return jsonify({'message': 'Invalid request method'}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=700)