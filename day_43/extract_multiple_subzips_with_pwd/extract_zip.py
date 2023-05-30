# You have a Zip which contains some sub Zip files in depth. And each of the
# Zip files has a password which is their name. Our challenge is to unzip
# all the Zip until you reach the end.

import zipfile

def extract_zip(filename):
     with zipfile.ZipFile(filename, 'r') as parent_file:
        parent_file.extractall(pwd=generate_pswd(filename))
        next_child_file = parent_file.namelist()[0]
        return next_child_file

def generate_pswd(filename):
    return bytes(filename.split('.')[0], 'utf-8')   

        
if __name__ == '__main__':
    try:
        file = '000.zip'
        next_file = extract_zip(file)
        while True:
            if zipfile.is_zipfile(next_file):
                next_file = extract_zip(next_file)
            else:
                break
    
    except FileNotFoundError as err:
        print("File doesn't exist:", err)
