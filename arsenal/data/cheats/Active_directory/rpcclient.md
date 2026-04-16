# rpcclient

% rpcclient, rpc, windows

## rpcclient - enumdomusers
#plateform/linux #target/remote #cat/RECON 
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'enumdomusers;quit'
```

## rpcclient - srvinfo
#plateform/linux #target/remote #cat/RECON 
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'srvinfo;quit'
```

## rpcclient - get user sid
#plateform/linux #target/remote #cat/RECON 
```
rpcclient <IP> -c 'lookupnales <NAME>; wmic useraccount get name,sid; quit'
```

## rpcclient - querydominfo
#plateform/linux #target/remote #cat/RECON 
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'querydominfo;quit'
```

## rpcclient - getdompwinfo  (password policy)
#plateform/linux #target/remote #cat/RECON 
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'getdompwinfo;quit'
```

## rpcclient - netshareenum  (password policy)
#plateform/linux #target/remote #cat/RECON 
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'netshareenum;quit'
```

## Trying all username as password from list of users
#plateform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY  
```
for u in `cat <FILE>`; do echo -n 'user: $u ' && rpcclient -U '$u%$u' -c 'getusername;quit' <IP>; done
```

## rpcclient - enum (Enum commands list)
#plateform/linux #target/remote #cat/RECON
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'enum;quit'
```

## rpcclient - enumdomains (Current domain)
#plateform/linux #target/remote #cat/RECON
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'enumdomains;quit'
```

## rpcclient - enumdomgroups (Enum Domain groups)
#plateform/linux #target/remote #cat/RECON
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'enumdomgroups;quit'
```

## rpcclient - querygroup (Enum Group Information)
#plateform/linux #target/remote #cat/RECON
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'querygroup <RID>;quit'
```

## rpcclient - querygroupmem (Enum Group Membership)
#plateform/linux #target/remote #cat/RECON
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'querygroupmem <RID>;quit'
```

## rpcclient - queryuser (Enumerate specific User/ computer information by RID)
#plateform/linux #target/remote #cat/RECON
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'queryuser <RID>;quit'
```

## rpcclient - getusrdompwinfo (User password policies)
#plateform/linux #target/remote #cat/RECON
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'getusrdompwinfo <RID>;quit'
```

## rpcclient - lsaenumsid (Local Users LSA Enum SID)
#plateform/linux #target/remote #cat/RECON
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'lsaenumsid;quit'
```

## rpcclient - lookupsid (Local Users Lookup SID)
#plateform/linux #target/remote #cat/RECON
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'lookupsid <SID>;quit'
```

## rpcclient - setuserinfo2 (Reset AD user password)
#plateform/linux #target/remote #cat/EXPLOIT
```
rpcclient <IP> -U '<USER>%<PASSWORD>' -c 'setuserinfo2 <LOGIN> 23 '<NEWPASSWORD>';quit'
```

