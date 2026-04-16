# smbmap
% smb, samba

## smbmap
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT 

```
smbmap -H <IP> -u '<USER>%<PASSWORD>'
```

## smbmap - null access
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT 

```
smbmap -u '' -p '' -P 445 -H <IP>
```

## smbmap - guest access
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT 
```
smbmap -u 'guest' -p '' -P 445 -H <IP>
```

## smbmap - list root of all shares
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT 
```
smbmap -H <IP> -u <USER> -p <PASSWORD> -d <DOMAIN> -r
```

## smbmap - recursively list dirs, and files
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT 
```
smbmap -H <IP> -u <USER> -p <PASSWORD> -d <DOMAIN> -R <PATH> --depth 1
```

= ip: 192.168.1.0/24
