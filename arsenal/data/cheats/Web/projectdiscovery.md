# nuclei

## nuclei - Single target scan
```
nuclei -target <URL>
```

## nuclei - Scanning multiple targets
```
nuclei -list <urls-file>
```

## nuclei - Network scan
```
nuclei -target <IP>
```

## nuclei - Scanning with your custom template
```
nuclei -u <URL> -t <file.yaml>
```

# subfinder 

## subfinder - basic scan
```
subfinder -d <DOMAIN> 
```

## subfinder - basic scan all sources
```
subfinder -d <DOMAIN> -all
```

# katana 

## katana - URL Input
```
katana -u <URL>
```

## katana - List Input
```
katana -list <FILE>
```

## katana - display all the urls with query parameter 
```
katana -u <URL> -f qurl -silent
```

## katana - Running katana using custom field 
```
katana -u <URL> -f <param|param,paramN>
```
