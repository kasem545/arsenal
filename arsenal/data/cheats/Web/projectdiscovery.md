# nuclei

## nuclei - Single target scan
```
nuclei -target <url>
```

## nuclei - Scanning multiple targets
```
nuclei -list <urls-file>
```

## nuclei - Network scan
```
nuclei -target <ip|192.168.0.1/24>
```

## nuclei - Scanning with your custom template
```
nuclei -u <url> -t <file.yaml>
```

# subfinder 

## subfinder - basic scan
```
subfinder -d <domain> 
```

## subfinder - basic scan all sources
```
subfinder -d <domain> -all
```

# katana 

## katana - URL Input
```
katana -u <url>
```

## katana - List Input
```
katana -list <file.txt>
```

## katana - display all the urls with query parameter 
```
katana -u <url> -f qurl -silent
```

## katana - Running katana using custom field 
```
katana -u <url> -f <param|param,paramN>
```
