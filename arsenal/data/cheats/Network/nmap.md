# nmap

#plateform/linux #target/remote #cat/RECON #tag/scan

## nmap - hosts alive
```
nmap -sn <ip_range>
```

## nmap - classic scan
```
nmap -sVC <IP>
```

## nmap - read targets from a file
```
nmap -iL <TARGETS_FILE>
```

## nmap - classic scan + save
```
nmap -sVC -oN <OUTFILE> <IP>
```

## nmap - quick scan top ports 100
```
nmap --top-ports 100 --open -sV <IP>
```

## nmap - big top ports 5000
```
nmap --top-ports 5000 --open -sV <IP>
```

## nmap - full port
```
nmap -p- -sV <IP>
```

## nmap - host with a given port
```
nmap <IP> -p<port_list> --open
```

## nmap - FULL
```
IP=<IP>;
ports=$(nmap -p- --min-rate=1000 -n -T4 $IP | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//);
nmap -Pn -sC -sV -p$ports $IP -oN scan.txt --reason --script=vuln
```

## nmap - udp scan
```
nmap -sU <IP>
```

## nmap - low rate Classic
```
nmap --max-rate 100 -sC -sV <IP>
```

## massscan - full port
```
masscan -p 1-65535 <IP> -e <dev> --rate=1000
```

## nmap - SMB signing disabled
```
nmap -Pn -sS -T4 --open --script smb-security-mode -p445 <IP>
```

## nmap behind proxy - tcp connect (-sT) - no dns (-n)
```
proxychains nmap -n -sT -sV -Pn --open -oA <OUTFILE> -iL <TARGETS_FILE>
```
