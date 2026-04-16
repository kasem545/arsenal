# enum4linux

% smb, samba

#plateform/linux  #target/remote  #port/445 #protocol/smb #cat/RECON 

## enum4linux - all except dictionary based share name listing (default)
```
enum4linux -a <IP>
```

## enum4linux - verbose
```
enum4linux -v <IP>
```

## enum4linux - null access
```
enum4linux -u '' -p '' <IP>
```

## enum4linux - guest access
```
enum4linux -u 'guest' -p '' <IP>
```

## enum4linux - with authentication
```
enum4linux -u <USER> -p <PASSWORD> <IP>
```

## enum4linux - list Users
```
enum4linux -U <IP> |grep 'user:'
```
