from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import sys, os, struct, random


class AESCipher:

    '''
    chunk_size: the size of encrypt data per round
    mode: encryption mode -> set to CBC

    '''

    def __init__(self, key, chunk_size=1024**2, mode='CBC'):
        assert chunk_size % 16 == 0, 'Invalid chunk size, must be multiple of 16'
        
        self.chunk_size = chunk_size
        self.mode = mode
        
        if self.mode.lower() not in ['cbc']:
            raise NotImplementedError(f'This encryption method {mode} has not been implemented')
        
        self.generate_key(key)


    def encrypt(self, file_in, file_out=None):
        print('Encrytping...')
        
        # initialization vector
        iv = Random.new().read(AES.block_size)
        
        # creating an encryptor object
        encryptor = AES.new(self.key, AES.MODE_CBC, iv)
        
        # getting filesize
        filesize = os.path.getsize(file_in)
        
        if not file_out:
            file_out = file_in + '.enc'
        
        # turning original content into a bytes object
        with open(file_in, 'rb') as infile:
            with open(file_out, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv)
                
                while True:
                    chunk = infile.read(self.chunk_size)
                    
                    if len(chunk) == 0:
                        break
                    else:
                        chunk += b' ' * (16-len(chunk)%16)
                    
                    outfile.write(encryptor.encrypt(chunk))
        

    def decrypt(self, file_in, file_out):
        pass


    def generate_key(self, key=None):
        '''
        Generate random key
        '''
        if key == None: 
            self.key = get_random_bytes(32)
        else:
            pass


    def get_key(self):
        '''
        Save key for the user
        '''
        key_path = 'my_key.bin'
        with open(key_path, 'wb') as f:
            f.write(self.key)






