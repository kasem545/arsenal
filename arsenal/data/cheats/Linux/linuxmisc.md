# linux miscs

## Check port usage
```
sudo lsof -i :<port>
```

## Kill process on port
```
sudo kill -9 <PID>
```

## Port Knocking
```
for i in <ports>;do nmap -Pn -p $i --host-timeout 201 --max-retries 0 <target-ip>;done
```

## ROT13
```
echo '<ciphertext>' | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

# mkpasswd 

## mkpasswd - Basic Usage
```
mkpasswd '<string-to-hash>'
```

## mkpasswd - Generate a SHA-512 hashed password
```
mkpasswd -m sha-512 '<string-to-hash>'
```

## mkpasswd - Generate an MD5 hashed password
```
mkpasswd -m md5 '<string-to-hash>'
```

## mkpasswd - Generate a bcrypt hashed password
```
mkpasswd -m bcrypt '<string-to-hash>'
```

## mkpasswd - Generate a password with a specific salt
```
mkpasswd -m sha-512 -S <salt> '<string-to-hash>'
```