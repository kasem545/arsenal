## Check port usage
```
sudo lsof -i :<port>
```

## Kill process on port
```
sudo kill -9 <PID>
```

## Port Knocking
```
for i in <ports>;do nmap -Pn -p $i --host-timeout 201 --max-retries 0 <target-ip>;done
```