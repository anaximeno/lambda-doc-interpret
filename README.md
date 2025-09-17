# Lambda Document Interpreter Project

## Current Status:

Project is set up and extraction + db store is working as expected. The main issue occured with `sam local start-api` runtime not being able to recognize the resulting output response claiming it's not a valid json. This is strange considering when running the project with uvicorn inside `src/` using `uvicorn main:app --reload --port=3000` it's working without issues so I am currently not sure of what's causing the issue in the lambda api side.


## How to run:

1. Start the postgres database container 

    ```sh
    docker compose up
    ```

2. Set up google api key in `src/configs/settings.py` in the `GOOGLE_API_KEY` field of the `Settings` class

3. Running using `uvicorn`:

    - Create a python virtual environment with `python -m venv ./venv`
    - Activate the virtual environment `source venv/bin/activate`
    - Install dependencies using `pip install -r requirements.txt`
    - Enter the `src/` dir with `cd src/`
    - Run the project using `uvicorn main:app --reload --port=3000`
    - Send a request to the `/extract` route with something like (**make sure to change "pdf_url" to an appropiate one**):

        ```sh
        curl --request POST -H "Content-Type: application/json" -d '{"pdf_url": "http://192.168.122.254:8000/0809090-86.2024.8.12.0021.pdf", "case_id": "0809090-86.2024.8.12.0021"}' http://127.0.0.1:3000/extract
        ``` 

4. Running using `sam` (**NOTE**: this method for some reason didn't work with the current response format while the uvicorn runtime is working):

    - Make sure you're on the root path of this project and run:

        ```sh
        sam build && sam local start-api
        ``` 
