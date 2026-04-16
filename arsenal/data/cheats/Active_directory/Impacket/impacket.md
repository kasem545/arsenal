# Impacket

% impacket, windows, smb, 445

## lookupsid - SID User Enumeration,  extract the information about what users exist and their data. 
#plateform/linux #target/remote #cat/RECON 

```
impacket-lookupsid <DOMAIN>/<USER>:<PASSWORD>@<IP>
```

## reg - query registry info remotely
#plateform/linux #target/remote #cat/RECON 
```
impacket-reg <DOMAIN>/<USER>:<PASSWORD>@<IP> query -keyName HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows -s
```

## rpcdump - Dump RPC endpoints
#plateform/linux #target/remote #cat/RECON 
```
impacket-rpcdump <DOMAIN>/<USER>:<PASSWORD>@<IP>
```

## rpcdump - Dump RPC endpoints
#plateform/linux #target/remote #cat/RECON 
```
impacket-rpcdump -hashes <HASH> <DOMAIN>/'<username>':'<PASSWORD>'@<target>
```

## impacket-services - (start, stop, delete, read status, config, list, create and change any service) remote
#plateform/linux #target/remote #cat/RECON  #cat/ATTACK/EXPLOIT  
```
impacket-services <DOMAIN>/<USER>:<PASSWORD>@<IP> <action>
``` 

## getarch - find target architecture (64 or 32 bits)
#plateform/linux #target/remote #cat/RECON 
```
impacket-getArch -target <IP>
```

## netview - enumeration tool (ip/shares/sessions/logged users) - need dns set
#plateform/linux #target/remote #cat/RECON 
```
impacket-netview <DOMAIN>/<USER> -target <IP> -users <users_file>
```


