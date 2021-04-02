from flask import Flask
import image_capture as ic

# Function to execute image capture function on app start.
def create_app():
    app = Flask(__name__)
    def run_on_start(*args, **argv):
        ic.saveImage()
    run_on_start()
    return app

# Start app.
app = create_app()
    
