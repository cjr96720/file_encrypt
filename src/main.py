from argparse import ArgumentParser
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import sys, os

class AESCipher:
    
    def __init__(self, key, chunk_size=1024**2, mode='CBC'):
        assert chunk_size % 16 == 0, 'Invalid chunk size'
        self.chunk_size = chunk_size
        self.mode = mode
        if self.mode.lower() not in ['cbc']:
            raise NotImplementedError(f'This encryption method {mode} has not been implemented')
        self.generate_key(key)

    def encrypt(self, file_in, file_out):
        pass

    def decrypt(self, file_in, file_out):
        pass

    def generate_key(self, key=None):
        if key == None: 
            self.key = get_random_bytes(32)
        else:
            pass


    def get_key(self):
        key_path = 'my_key.bin'
        with open(key_path, 'wb') as f:
            f.write(self.key)





def parse_args():
    
    '''
    Usage: python main.py action file_selected [OPTION]... 
    OPTIONS:
        -o, --out,      output filename
        -k, --key,      key to decrypt the file

    '''
    parser = ArgumentParser()
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='encrypt or decrypt')
    parser.add_argument('file_selected', help='file to be encrypted or decrypted')
    parser.add_argument('-o', '--output', default=None, nargs='?', help='output filename')
    parser.add_argument('-k', '--key', type=str, default=None, nargs='?', help='key to decrypt the file')
    args = parser.parse_args()

    return args

if __name__ == '__main__':

    args = parse_args()
    
    worker = AESCipher(args.key)
    if args.key is None:
        worker.get_key()
        print(f'Key generated')

