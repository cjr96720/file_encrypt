import sys

from utils import parse_args
from AESCipher import AESCipher

if __name__ == '__main__':

    # parsing arguments
    args = parse_args()
    
    # check if user provided key for decrypting
    if args.key is None and args.action == 'decrypt':
        print('Key is needed for decrypting the file.')
        sys.exit(1)
    
    worker = AESCipher(args.key)
    actions = {
        'encrypt': worker.encrypt,
        'decrypt': worker.decrypt
    }
    
    if args.key is None:
        print('Key generated!')
        worker.get_key()
    
    actions.get(args.action)(args.file_selected, args.output)
    


    