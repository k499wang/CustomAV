import requests
import argparse

def upload_file(file_path, url):
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    return response.status_code, response.json()

if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('-f', '--file', required=True)
    
    args = argparse.parse_args()
    
    
    url = 'http://localhost:5000/check_file'
    file_path = args.file
    status_code, response = upload_file(file_path, url)
    print(status_code, response)