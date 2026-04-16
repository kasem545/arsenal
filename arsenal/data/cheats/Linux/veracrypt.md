# veracrypt

% veracrypt

#plateform/linux

## Create veracrypt volume for Linux
```
veracrypt -t --create <FILE> --hash sha512 --encryption AES --filesystem ext4 --volume-type normal -k '' --pim 0 --size <size>
```

## Open veracrypt volume
```
veracrypt <FILE> <mount>
```

## Lock veracrypt volume
```
veracrypt -d <FILE>
```


## Lock all veracrypt volume
```
veracrypt -d
```
