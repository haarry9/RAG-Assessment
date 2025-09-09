from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
CHROMA_DB_DIR = "chroma_db"

