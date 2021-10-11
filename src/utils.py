from argparse import ArgumentParser


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
