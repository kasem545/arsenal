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
for i in <ports|3300,3231,3999>;do nmap -Pn -p $i --host-timeout 201 --max-retries 0 <target-ip>;done
```