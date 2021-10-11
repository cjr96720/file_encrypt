# Encrypt and Decrypt File with Python

> Note: Since we are running python program in docker, 
make sure to put the file you want to encrypt/decrypt 
and the key into the src folder.

### On Mac
#### Run docker
``` bash
cd file_encrypt
docker compose up -d
docker exec -it app bash
```
#### Encrypting file
```bash
python3 main.py encrypt sample.txt
```

#### Decrypting file
```bash
python3 main.py decrypt sample.txt.enc -k my_key.bin
