import requests

def upload_file(file_path, url):
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    return response.status_code, response.json()

if __name__ == '__main__':
    url = 'http://localhost:5000/check_file'
    file_path = 'C2ImplantSrc.exe'
    status_code, response = upload_file(file_path, url)
    print(status_code, response)