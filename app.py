from app import create_app
import os
app = create_app

# app.run(debug=False, port=os.getenv("PORT") or 8000)