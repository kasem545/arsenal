# WPSCAN

% wpscan, wordpress

#plateform/linux #target/remote #cat/RECON 
## wpscan BruteForce User
```
wpscan --url <url> -U '<user>' -P '<wordlist>' -t <threads>
```
#plateform/linux #target/remote #cat/RECON 
## wpscan Enumerate Users
```
wpscan --url <url> -e u --random-user-agent
```

#plateform/linux #target/remote #cat/RECON 
## wpscan Vulnerable themes,plugins with api key
```
wpscan --url <url> -e u,vp,vt --api-token '<YOUR_API_TOKEN>' --random-user-agent
```
