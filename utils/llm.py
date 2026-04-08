import os
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel

# Load environment variables from .env file
load_dotenv()

# Initialize Vertex AI configuration
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION", "us-central1")
MODEL_NAME = os.getenv("MODEL", "gemini-2.5-flash")

vertexai.init(project=PROJECT_ID, location=LOCATION)
