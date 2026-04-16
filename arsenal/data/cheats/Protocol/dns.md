# DNS

% dns, host, 53

## host find name server
#plateform/linux  #target/remote  #cat/RECON  
```
host -t ns <DOMAIN>
```

## host find mail server
#plateform/linux  #target/remote  #cat/RECON
```
host -t mx <DOMAIN>
```

% dns, dig, 53

## dig dns lookup
#plateform/linux  #target/remote  #cat/RECON
```
dig <DOMAIN> @1.1.1.1
```

## dig any information
#plateform/linux  #target/remote  #cat/RECON
```
dig ANY <DOMAIN> @<dns_ip>
```

## dig reverse lookup
#plateform/linux  #target/remote  #cat/RECON
```
dig -x <IP> @<dns_ip>
```

## dig zone transfer
#plateform/linux  #target/remote  #cat/RECON
```
dig axfr <DOMAIN> @<name_server>
```

## dig, find external, public IP address
#plateform/linux  #target/remote  #cat/RECON
```
dig +short <DOMAIN> @resolver1.opendns.com
```

## dig, find domains file ip address value
#plateform/linux  #target/remote  #cat/RECON
```
dig -f <FILE> +noall +answer
```

## dig, find domains file MX ip record
#plateform/linux  #target/remote  #cat/RECON
```
dig -f <FILE> MX +noall +answer
```

% dns, dnsrecon, 53

## dnsrecon standard enum on domain
#plateform/linux  #target/remote  #cat/RECON
```
dnsrecon -d <DOMAIN>
```

## dnsrecon zone transfer
#plateform/linux  #target/remote  #cat/RECON
```
dnsrecon -d <DOMAIN> -t axfr
```

## dnsrecon reverse lookup start/end ip
#plateform/linux  #target/remote  #cat/RECON
```
dnsrecon -r <startip>-<endip> -n <domain_name_server>
```

## dnsrecon reverse lookup network range ip
#plateform/linux  #target/remote  #cat/RECON
```
dnsrecon -r <ip_with_network_mask> -n <domain_name_server>
```

## dnsrecon domain bruteforce
#plateform/linux  #target/remote  #cat/RECON
```
dnsrecon -d <DOMAIN> -D <WORDLIST> -t brt
```

% dns, dnsenum, 53
#plateform/linux  #target/remote  #cat/RECON
```
dnsenum <DOMAIN>
```

% dns, nmap, 53

## nmap grab banner
#plateform/linux  #target/remote  #cat/RECON
```
nmap -sV -p 53 --script dns-nsid <IP>
```

## nmap dns tcp
#plateform/linux  #target/remote  #cat/RECON
```
nmap -n -sV --script '(*dns* and (default or (discovery and safe))) or dns-random-txid or dns-random-srcport' -p 53 <IP>
``` 

## nmap dns udp
#plateform/linux  #target/remote  #cat/RECON
```
nmap -n -sV -sU --script ''(*dns* and (default or (discovery and safe))) or dns-random-txid or dns-random-srcport' -p 53 <IP>
``` 

## nmap activedirectory enum
#plateform/linux  #target/remote  #cat/RECON
```
nmap --script dns-srv-enum --script-args 'dns-srv-enum.domain='<DOMAIN>''
```

## nmap dnssec 
#plateform/linux  #target/remote  #cat/RECON
```
nmap -sSU -p53 --script dns-nsec-enum --script-args dns-nsec-enum.domains=<DOMAIN> <IP>
```

% dns, msf, 53

## dns metasploit enumeration
#plateform/linux  #target/remote  #cat/RECON
```
msfconsole -x 'use auxiliary/gather/enum_dns; set domain <DOMAIN>; set ns <dns_server>; exploit'
```

% dns, sublist3r , 53

## dns sublist3r - subdomain enumeration
#plateform/linux  #target/remote  #cat/RECON
```
sublist3r -d <DOMAIN> -v
```

## dns sublist3r - subdomain enumeration with bruteforce module enabled
#plateform/linux  #target/remote  #cat/RECON
```
sublist3r -b -d <DOMAIN>
```
