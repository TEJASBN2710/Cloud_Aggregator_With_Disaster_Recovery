from flask import Flask, render_template, redirect, url_for
import sys

app = Flask(__name__)

# Global variable to track maintenance mode
maintenance_mode = False

@app.route('/')
def index():
    if maintenance_mode:
        return render_template('maintenance.html')  # Render maintenance page
    return render_template('index.html')  # Render normal page

@app.route('/set_maintenance_mode/<mode>', methods=['POST'])
def set_maintenance_mode(mode):
    global maintenance_mode
    maintenance_mode = (mode == 'on')
    return 'Maintenance mode is now ' + mode

if __name__ == '__main__':
    # Get the port from command-line arguments
    port = 5000  # Default port
    if '--port' in sys.argv:
        port_index = sys.argv.index('--port') + 1
        if port_index < len(sys.argv):
            port = int(sys.argv[port_index])

    app.run(port=port)
