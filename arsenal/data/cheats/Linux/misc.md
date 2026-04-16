# QR code

% qr code

## Create a QR code with some content
#plateform/linux #target/local #cat/UTILS 

```
echo <CONTENT> | curl -F-=\<- qrenco.de
```

# json

% json

## convert JSON to YAML
#plateform/linux #target/local #cat/UTILS
```
cat <FILE> | ruby -ryaml -rjson -e 'puts YAML.dump(JSON.load(ARGF))'
```

# linux

% misc, linux

## Convert multi line to one line
#plateform/linux #target/local #cat/UTILS 
```
grep <PATTERN> <FILE> | tr '\n' ' '
```

## grep nmap protocol from file and get ips in one line
#plateform/linux #target/local #cat/UTILS 
```
grep <PATTERN> <FILE>.gnmap|cut -d ' ' -f 2 | tr '\n' ' '
```

% scanner

## find service on port
#plateform/linux #target/remote #cat/RECON 
```
amap -d <IP> <PORT>
```

