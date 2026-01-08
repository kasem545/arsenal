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
echo "<ciphertext>" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

# mkpasswd 

## mkpasswd - Basic Usage
```
mkpasswd "Password123"
```

## mkpasswd - Generate a SHA-512 hashed password
```
mkpasswd -m sha-512 "Password123"
```

## mkpasswd - Generate an MD5 hashed password
```
mkpasswd -m md5 "Password123"
```

## mkpasswd - Generate a bcrypt hashed password
```
mkpasswd -m bcrypt "Password123"
```

## mkpasswd - Generate a password with a specific salt
```
mkpasswd -m sha-512 -S <salt> "Password123"
```

# uv

## uv - Install package from PyPI
```
uv tool install <package-name>
```
## uv - Install from GitHub
```
uv tool install git+<github-repo-url>
```
## uv - Upgrade all tools
```
uv tool upgrade --all
```
## uv - List installed tools
```
uv tool list
```

## uv - inject missing modules
```
uv add --script <script-path> <package-name>
```