import requests
import argparse

def upload_string(string, url):
    response = requests.post(url, json={'string': string})
    return response.status_code, response.json()

if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('-s', '--string', required=True)
    
    args = argparse.parse_args()
    print(upload_string(args.string, 'http://localhost:5000/check_string'))