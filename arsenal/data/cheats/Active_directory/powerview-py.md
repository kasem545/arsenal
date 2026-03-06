# powerview-py

#plateform/windows #target/remote #cat/RECON #tag/scan

## connect

METHODS = [--use-ldap | --use-ldaps | --use-gc | --use-gc-ldaps | --use-adws | --use-channel-binding | --use-sign-and-seal | --use-simple-auth]
```
powerview <DOMAIN>/<USERNAME>:'<PASSWORD>'@<IP> <METHOD>
```

## Start web interface

```
powerview <DOMAIN>/<USERNAME>:'<PASSWORD>'@<IP> --web --web-host <host|0.0.0.0> --web-port <port|3000> --web-auth <user>:<password>
```

## Connect with pfx

```
powerview <IP> --pfx <PFX>
```
## Relay mode

```
powerview 10.10.10.10 --relay [--relay-host] [--relay-port] [--use-ldap | --use-ldaps]
```