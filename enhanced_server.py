from flask import Flask, request, jsonify
import logging
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Initialize the Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup rate limiting
limiter = Limiter(get_remote_address, app=app)

# In-memory persistence - can be replaced with a database
memory_store = {}

@limiter.limit("5 per minute")
@app.route('/submit_task', methods=['POST'])
def submit_task():
    data = request.json
    task_id = data.get('task_id')
    # Logic to submit task to the multi-agent system
    memory_store[task_id] = 'Task submitted'
    logger.info(f'Task {task_id} submitted')
    return jsonify({'message': 'Task submitted', 'task_id': task_id}), 201

@limiter.limit("5 per minute")
@app.route('/monitor_agents', methods=['GET'])
def monitor_agents():
    # Logic to monitor agents
    logger.info('Monitoring agents status')
    return jsonify({'agents': 'Agents status here'}), 200

@limiter.limit("5 per minute")
@app.route('/retrieve_result/<task_id>', methods=['GET'])
def retrieve_result(task_id):
    # Logic to retrieve task result from memory
    logger.info(f'Retrieving result for task {task_id}')
    result = memory_store.get(task_id, 'No such task')
    return jsonify({'task_id': task_id, 'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)