# WPSCAN

% wpscan, wordpress

#plateform/linux #target/remote #cat/RECON 
## wpscan BruteForce User
```
wpscan --url <URL> -U '<USER>' -P '<WORDLIST>' -t <threads>
```
#plateform/linux #target/remote #cat/RECON 
## wpscan Enumerate Users
```
wpscan --url <URL> -e u --random-user-agent
```

#plateform/linux #target/remote #cat/RECON 
## wpscan Vulnerable themes,plugins with api key
```
wpscan --url <URL> -e u,vp,vt --api-token '<YOUR_API_TOKEN>' --random-user-agent
```
