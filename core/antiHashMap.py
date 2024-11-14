import hashlib

class AntiHashMap:
    def __init__(self):
        self.hashMapDB = {}
    
    def insert(self, key, value):
        self.hashMapDB[key] = value
    
    def search(self, key):
        if key in self.hashMapDB:
            return self.hashMapDB[key]
        return None

    def output(self):
        for key, value in self.hashMapDB.items():
            print(f"{key} : {value}")

    def insert_file(self, filename, value):
        hash_function = hashlib.new("sha256")
        
        try:
            with open(filename, "rb") as i:
                while chunk := i.read(8192):
                    hash_function.update(chunk)
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

        self.insert(hash_function.hexdigest(), value)
        
        return True
        
    def insert_database(self, filename):
        try:
            with open(filename, "r") as i:
                for line in i:
                    key, value = line.split(":")
                    self.insert(key, value)
                    
        except Exception as e:
            return False