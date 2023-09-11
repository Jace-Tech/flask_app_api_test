
## Setup

### Prerequisites

- Python 3.x
- Flask web framework
- Flask-JWT-Extended for JWT authentication
- Flask-CORS for handling CORS issues

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Jace-Tech/plant-nest-backend.git
   ```

2. Navigate to the project directory:

   ```bash
   cd plant-nest-backend
   ```

3. Create a virtual enviroment

  ```shell
    # In Windows 
    py -m venv venv

    # In Unix (Mac | Linux)
    python3 -m venv venv
  ```

4. Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a new `.env` file in the root of your directory, and then add in all the variables from the `.env.examples` with the appropriate values

6. Finally, run the app with `gunicorn --workers=2 'app:create_app()'` or 

  ```bash
  # Windows
  py app.py

  #Unix
  python3 app.py
  ```
