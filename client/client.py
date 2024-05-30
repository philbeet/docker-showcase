import requests
import hashlib
import os

def check_checksum(data):
    hash_mod = hashlib.md5()
    hash_mod.update(data)
    return hash_mod.hexdigest()

def main():
    response = requests.get("http://server:5000/")

    if response.status_code == 200:
        file = response.content
        

        checksum = check_checksum(file)

        server_checksum = response.headers.get("Checksum")

        if checksum == server_checksum:
            print("Checksums match!")
            print("file: ", file)
            #only write file to memory if checksums match
            os.makedirs("/clientdata", exist_ok=True)
            with open("/clientdata/random_text.txt", "w") as f:
                f.write(file.decode("utf-8"))
                f.close()
        else:
            print("WARNING: Checksums do not match.")
    else:
        print("error. failed to download file.", response.status_code)

if __name__ == "__main__":
    main()
    while True:
        pass
        #this will keep the client running so you can shell in and check data