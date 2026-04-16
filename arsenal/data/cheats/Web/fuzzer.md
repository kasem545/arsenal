# ffuf

% fuzzer, fuzz, ffuf
#plateform/linux #target/remote #cat/ATTACK/FUZZ
## ffuf fuzz keyword in url
```
ffuf -u '<URL>/FUZZ' -w <WORDLIST> -ac -ic
```

## ffuf fuzz Host filter response size
```
ffuf -u <URL> -H 'Host: FUZZ.domain' -w <WORDLIST> -ac
```

## ffuf GET parameter fuzzing
```
ffuf -u '<URL>?<param>=FUZZ' -w <WORDLIST> -ac
```

## ffuf GET parameter fuzzing
```
ffuf -u '<URL>?FUZZ=1' -w <WORDLIST> -ac
```

## ffuf POST parameter fuzzing
```
ffuf -X POST -u <URL> -d '<post-data>' -w <WORDLIST> -H 'Content-Type: application/x-www-form-urlencoded' -fr <filter-expression>
```
