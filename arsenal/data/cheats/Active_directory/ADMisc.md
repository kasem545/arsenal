# convert to NTLM

## string to ntlm hash
Convert Plaintext password to NTLM Hash
```bash
iconv -f ASCII -t UTF-16LE <(printf '<PASSWORD>') | openssl dgst -md4
```