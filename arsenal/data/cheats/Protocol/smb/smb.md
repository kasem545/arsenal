# smb
% smb, samba

## nbtscan - scan network looking for hosts
#plateform/linux #target/remote #port/445 #protocol/smb #cat/RECON 
```
nbtscan -r <ip_range>
```

## smbclient with username and password
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
```
smbclient \\\\<IP>\\<share> -U '<USER>%<PASSWORD>'
```

## smbclient with domain username and password
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
```
smbclient \\\\<IP>\\<share> -U '<DOMAIN>/<USER>%<PASSWORD>'
```

## smbclient sessions without password
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
```
smbclient \\\\<IP>\\<share> -U '<USER>%'
```

## smbclient null session
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
```
smbclient \\\\<IP>\\<share> -U '%'
```

## smb - find not signed  smb
#plateform/linux #target/remote #port/445 #protocol/smb #cat/RECON 
```
nmap -Pn -sS -T4 --open --script smb-security-mode -p445 <IP>
```

## smb mount folder
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
```
mount -t cifs //<IP>/C\$ /tmp/mnttarget/ -o username=<USER> -o domain=<DOMAIN>
```
