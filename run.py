
import os
from app import app


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8888))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)
