# gpg

% gpg

#plateform/linux #target/local #cat/UTILS

## gpg version
```
gpg --version
```

## gpg generate key
```
gpg --gen-key
```

## list keys
```
gpg --list-keys
```

## distribute public key to key server
```
gpg --keyserver <KEY_SERVER> --send-keys <PUBLIC_KEY>
```

## export public key
```
gpg --output <FILE> --export <key_name>
```

## import public key
```
gpg --import <FILE>
```

## encrypt document
```
gpg --output <OUTFILE> --encrypt --recipient <PUBLIC_KEY> <input_filename>
```

## decrypt document
```
gpg --output <FILE> --decrypt <FILE>
```

## make a signature
```
gpg --output <FILE> --sign <FILE>
```

## verify signature
```
gpg --output <FILE> <FILE> --decrypt <FILE>
```

## clearsign documents
```
gpg --clearsign <FILE>
```

## detach signature
```
gpg --output <FILE> --detach-sig <FILE>
```
