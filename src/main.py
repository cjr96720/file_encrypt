from utils import parse_args
from AESCipher import AESCipher

if __name__ == '__main__':

    args = parse_args()
    
    worker = AESCipher(args.key)
    if args.key is None:
        worker.get_key()
        print(f'Key generated')