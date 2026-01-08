# Impacket

% impacket, windows, smb, 445

## lookupsid - SID User Enumeration,  extract the information about what users exist and their data. 
#plateform/linux #target/remote #cat/RECON 

```
impacket-lookupsid <domain>/<user>:<password>@<ip>
```

## reg - query registry info remotely
#plateform/linux #target/remote #cat/RECON 
```
impacket-reg <domain>/<user>:<password>@<ip> query -keyName HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows -s
```

## rpcdump - Dump RPC endpoints
#plateform/linux #target/remote #cat/RECON 
```
impacket-rpcdump <domain>/<user>:<password>@<ip>
```

## rpcdump - Dump RPC endpoints
#plateform/linux #target/remote #cat/RECON 
```
impacket-rpcdump -hashes <hash> <domain>/'<username>':'<password>'@<target>
```

## impacket-services - (start, stop, delete, read status, config, list, create and change any service) remote
#plateform/linux #target/remote #cat/RECON  #cat/ATTACK/EXPLOIT  
```
impacket-services <domain>/<user>:<password>@<ip> <action>
``` 

## getarch - find target architecture (64 or 32 bits)
#plateform/linux #target/remote #cat/RECON 
```
impacket-getArch -target <ip>
```

## netview - enumeration tool (ip/shares/sessions/logged users) - need dns set
#plateform/linux #target/remote #cat/RECON 
```
impacket-netview <domain>/<user> -target <ip> -users <users_file>
```


