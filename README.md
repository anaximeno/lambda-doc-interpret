# Lambda Document Interpreter Project

## Current Status:

- Project is setup
- Extraction is working as expected
  - I was able to test this using `uvicorn` in the `src/` folder to serve the app, however from the lambda runtime using `sam local start-api` the request will error out claiming invalid json, even though it seems ok when testing with other kinds of run times.
- Lambda runtime for some reason is not recognizing the json even if generated from a pydantic model subclass or using json.loads to convert string (To Be Fixed)
- Supports for Persistence with a DB (To Be Done)
