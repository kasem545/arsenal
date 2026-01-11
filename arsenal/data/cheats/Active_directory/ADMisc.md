# convert to NTLM

## string to ntlm hash
Convert Plaintext password to NTLM Hash
```bash
iconv -f ASCII -t UTF-16LE <(printf '<PASSWORD>') | openssl dgst -md4
```

## convert file to base64 one line
#plateform/linux #target/local #cat/UTILS 

```bash
iconv -f ASCII -t UTF-16LE <file_to_convert> | base64 | tr -d "\n"
```

## convert string to base64 one line
#plateform/linux #target/local #cat/UTILS 

```bash
printf '%s' '<string>' | iconv -f ASCII -t UTF-16LE | base64 | tr -d '\n'
```