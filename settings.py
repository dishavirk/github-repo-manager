from dotenv import load_dotenv
import os


load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
SOURCE_ORG = os.getenv('SOURCE_ORG')
TARGET_ORG = os.getenv('TARGET_ORG')
USERNAME = os.getenv('USERNAME')
SPECIFIC_REPO = os.getenv('SPECIFIC_REPO')