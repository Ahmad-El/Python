import requests
import sys
import os

BASE_URL = "http://localhost:8888"


def list_files():
    response = requests.get(f"{BASE_URL}/json")
    audios = response.json()
    for audio in audios["files"]:
        print(audio)


def upload_files(file_name):
    files = {"file": open(file_name, "rb")}
    response = requests.post(f"{BASE_URL}", files=files)
    print(response.status_code)


def main():
    args = sys.argv
    if args[1] == "list" and len(args) < 3:
        list_files()
    elif args[1] == "upload" and len(args) < 4:
        file_name = args[2]
        if os.path.exists(file_name) and file_name.endswith((".mp3", ".ogg", ".wav")):
            # full_path = os.path.abspath(file_name)
            upload_files(file_name)
        else:
            print("File not Found or file is not audio file")
    else:
        print("Unknown error occurred")


if __name__ == "__main__":
    main()
