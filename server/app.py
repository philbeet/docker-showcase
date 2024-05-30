from flask import Flask, send_file
import hashlib
import random
import os
import string

app = Flask(__name__)

def generate_string(kilobytes):
    return "".join(random.choices(string.ascii_letters, k=kilobytes))

def generate_text(name, size=1):
    with open(name, "w") as f:
        f.write(generate_string(size * 1024))
        f.close()

def checksum(name):
    hash_obj = hashlib.md5()
    with open(name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_obj.update(chunk)
    checksum = hash_obj.hexdigest()
    return checksum

@app.route('/')
def hello():
    filename = '/serverdata/random_text.txt'
    os.makedirs("/serverdata", exist_ok=True)
    generate_text(filename, 1)

    cs = checksum(filename)

    return send_file(filename, as_attachment=True), 200, {"Checksum": cs}
if __name__ == '__main__':
    app.run()