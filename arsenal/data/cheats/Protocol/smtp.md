# SMTP

% smtp, 25
#plateform/linux  #target/remote  #protocol/smtp #port/25

## smtp nmap enumeration
#cat/RECON 
```
nmap -p25 --script smtp-commands <IP>
```

## smtp nmap ntlm information disclosure
#cat/RECON 
```
nmap -p25 --script smtp-ntlm-info <IP>
```

## nmap - smtp user enum
#cat/ATTACK/BRUTEFORCE-SPRAY  
```
nmap –script smtp-enum-users.nse <IP>
```

## smtp user enum
#cat/ATTACK/BRUTEFORCE-SPRAY 
```
smtp-user-enum -M VRFY -U <USER_FILE> -t <IP>
```

## msf - smtp user enum
#cat/ATTACK/BRUTEFORCE-SPRAY 
```
msfconsole -x 'use auxiliary/scanner/smtp/smtp_enum; set RHOSTS <IP>; exploit'
```
