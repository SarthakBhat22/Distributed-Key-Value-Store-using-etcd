from flask import Flask, render_template, request
from client import Client    # Import the Client class from client.py file
import threading

app = Flask(__name__)
available_endpoints = ["http://<ip-address>:2379", "http://<ip-address>:2380", "http://<ip-address>:2381"]

client = Client(available_endpoints)  # Instantiate the client


def reconnect_thread():
    while True:
        if not client.is_connection_active():
            try:
                client.connect()
            except Exception as e:
                print(f"Error: {e}")
        app.logger.debug("Reconnect thread running...")
        threading.Event().wait(5)


connection_thread = threading.Thread(target=reconnect_thread)
connection_thread.start()

# Route to display available options
@app.route('/')
def index():
    """
    Renders the index.html template.

    Returns:
        str: HTML content for the index page.
    """
        
    return render_template('index.html')


# Route for put operation
@app.route('/put', methods=['POST'])
def put():
    """
    Handles the PUT operation to store a key-value pair in the etcd server.

    Returns:
        str: Confirmation message indicating the success of the operation.
    """

    key = request.form['key']
    value = request.form['value']
    client.put_key(key, value)
    return "Key '{}' with value '{}' added successfully.".format(key, value)


# Route for get operation
@app.route('/get', methods=['POST'])
def get():
    """
    Handles the GET operation to retrieve the value of a key from the etcd server.

    Returns:
        str: The value associated with the requested key.
    """

    key = request.form['key']
    try:
        value = client.get_value(key)
        return value
    except Exception as e:
        return e


# Route for delete operation
@app.route('/delete', methods=['POST'])
def delete():
    """
    Handles the DELETE operation to remove a key-value pair from the etcd server.

    Returns:
        str: Confirmation message indicating the success of the operation.
    """

    key = request.form['key']
    try:
        message = client.delete_key(key)
        return message
    except Exception as e:
        return e

# Route for list operation
@app.route('/list')
def list_keys():
    """
    Lists all keys stored in the etcd server.

    Returns:
        str: HTML content displaying the list of keys.
    """
     
    keys = client.get_all_keys()
    return render_template('list.html', keys=keys)

if __name__ == '__main__':
    app.run()