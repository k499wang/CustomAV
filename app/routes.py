from flask import Flask, Blueprint, request, current_app
from core.antiHashMap import AntiHashMap
from core.trieNode import Trie, insert_trie
from core.utils import extract_strings  

anti = Blueprint('anti', __name__)

@anti.route('/')
def hello_world():
    return 'Hello, World!'

@anti.route('/check_string', methods=["POST"])
def check_string():
    db = current_app.config['db']
    trie = current_app.config['trie']
    
    data = request.get_json()
    
    if 'string' not in data:
        return {'error': 'No string provided'}, 400
    
    string = data['string']
    match = trie.search_in_tree(string.strip().lower())
    
    if match:
        return {'result': match}, 201
    
    return {'result': None}, 200



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
        
        
        
        
    

