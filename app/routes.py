from flask import Flask, Blueprint, request, current_app
from core.antiHashMap import AntiHashMap
from core.trieNode import Trie, insert_trie
from core.utils import extract_strings  

anti = Blueprint('anti', __name__)

@anti.route('/')
def hello_world():
    return 'Hello, World!'

@anti.route('/check_file', methods=["POST"])
def check_file():
    db = current_app.config['db']
    trie = current_app.config['trie']
    
    if 'file' not in request.files:
        return {'error': 'No file provided'}, 400
    try:
        file = request.files['file']
        filebytes = file.read()
        strings = extract_strings(filebytes)
        
        matches = []
        
        for string in strings:
            match = trie.search_in_tree(string.strip().lower())
            if match:
                matches.append(match)
        
        if matches: # If malware is found, then we return a different status code
            return {'result': matches}, 201
        
        return {'result': matches}, 200
    except Exception as e:
        return {'error': str(e)}, 500
        
        
        
        
    

