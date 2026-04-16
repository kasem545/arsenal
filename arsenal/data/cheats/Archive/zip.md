# zip

% archive, compress

#plateform/linux #target/local #cat/UTILS 

## create zip file
```
zip <FILE>.zip <files_to_zip>
```

## zip all the files of current directory
```
zip <FILE>.zip *
```

## zip folder
```
zip -r <FILE>.zip <folder>
```

## add file to a zip archive
```
zip -u <FILE>.zip <file_to_add>
```

## view zip content
```
zipinfo <FILE>.zip
```

## create zip file with symlink (useful for path traversal)
```
zip --symlinks <FILE>.zip <symlink_file>
```

## list detailed zip file content
```
unzip -Z <FILE>.zip
```

## unzip file
```
unzip <FILE>.zip
```

## unzip file to directory
```
unzip <FILE>.zip -d <destination_folder>
```
