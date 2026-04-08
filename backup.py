import os
import argparse
import requests
from dotenv import load_dotenv

load_dotenv()

def upload_file(file_path, api_key):
    url = "https://filelu.com/api/upload"

    try:
        with open(file_path, 'rb') as f:
            response = requests.post(
                url,
                files={"file": f},
                data={"api_key": api_key}
            )

        if response.status_code == 200:
            print(f"Uploaded: {file_path}")
        else:
            print(f"Failed: {file_path}")

    except Exception as e:
        print(f"Error: {e}")


def upload_folder(folder_path, api_key):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            upload_file(file_path, api_key)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--folder", type=str)
    parser.add_argument("--api-key", type=str)

    args = parser.parse_args()

    api_key = args.api_key or os.getenv("FILELU_API_KEY")

    if not api_key:
        print("API key required")
        return

    if not args.folder:
        print("Folder required")
        return

    upload_folder(args.folder, api_key)


if __name__ == "__main__":
    main()
