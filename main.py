import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

from SearchForFaceClient import SearchForFaceClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

if __name__ == '__main__':
    HOST = os.environ.get("SEARCH_FOR_FACE_HOST")
    TOKEN = os.environ.get("SEARCH_FOR_FACE_API_TOKEN")
    SFSClient = SearchForFaceClient(HOST, TOKEN)

    try:
        res = SFSClient.rate_limit()
    except Exception as e:
        print(e)

