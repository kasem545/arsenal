# chisel

% chisel

## chisel server (server on local machine)
#plateform/linux  #target/remote  #cat/PIVOT 
```
chisel server -p <server-port|8080> --socks5 --reverse
```

## chisel socks proxy (client on remote machine)
#plateform/windows  #target/remote  #cat/PIVOT 
```
chisel client --fingerprint <FINGERPRINT> <server-ip>:<server-port> R:1080:socks
```


## chisel reverse port forwarding (client on remote machine) - forward client port on server
#plateform/linux  #target/remote  #cat/PIVOT 
```
chisel client <server-ip>:<server-port> R:<server-lport>:<client-ip>:<client-port>
```

## chisel remote port forwarding (client on remote machine) - forward server port on client
#plateform/linux  #target/remote  #cat/PIVOT 
```
chisel client -v <server-ip>:<server-port|8000> <client-ip|0.0.0.0>:<client-port>:<server-ip|127.0.0.1>:<server-port>
```

# sshuttle

## sshuttle - Forwarding traffic through
```
sshuttle -r <user>@<target-ip> <IP|IP/CIDR>
```

## sshuttle - Auto detect networks
```
sshuttle -vNr <user>@<target-ip>
```