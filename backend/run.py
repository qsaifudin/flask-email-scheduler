import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.main import app

if __name__ == "__main__":
    app.run(debug=True)
