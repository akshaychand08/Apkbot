from .start import start_cmd
from .broadcast import broadcast_cmd

def setup_handlers(app):
    app.add_handler(start_cmd)
    app.add_handler(broadcast_cmd)
    
