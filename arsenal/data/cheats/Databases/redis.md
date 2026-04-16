# Redis

% databases
#plateform/linux #target/remote #cat/RECON #cat/ATTACK/CONNECT

## connect to the local server
```bash
redis-cli
```

## connect to a remote server on the default port (6379)
```bash
redis-cli -h <IP> -a <PASSWORD>
```

## connect remotely specifying a port
```bash
redis-cli -h <IP> -p <PORT> -a <PASSWORD>
```

## connect remotely over tls w/ server certificate
```bash
redis-cli -h <IP> --tls --cacert <redis_cert_path.pem>
```

## connect remotely over tls w/ server & client certificates
```bash
redis-cli -h <IP> --tls --cacert <redis_cert_path.pem> --cert <redis_user_path.crt> --key <redis_user_private_path.key>
```
