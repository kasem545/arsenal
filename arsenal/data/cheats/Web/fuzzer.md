# ffuf

% fuzzer, fuzz, ffuf
#plateform/linux #target/remote #cat/ATTACK/FUZZ
## ffuf fuzz keyword in url
```
ffuf -u '<url>/FUZZ' -w <wordlist> -ac -ic
```

## ffuf fuzz Host filter response size
```
ffuf -u <url> -H 'Host: FUZZ.domain' -w <wordlist> -ac
```

## ffuf GET parameter fuzzing
```
ffuf -u '<url>?<param>=FUZZ' -w <wordlist> -ac
```

## ffuf GET parameter fuzzing
```
ffuf -u '<url>?FUZZ=1' -w <wordlist> -ac
```

## ffuf POST parameter fuzzing
```
ffuf -X POST -u <url> -d '<post-data>' -w <wordlist> -H 'Content-Type: application/x-www-form-urlencoded' -fr <filter-expression>
```
