# flashrom

#plateform/linux #target/remote #cat/RECON

## Read from linux (e.g. Raspberry Pi)
```
flashrom -p linux_spi:dev=<spidev>,spispeed=<spispeed> -r <OUTFILE>
```

## Force read from linux (e.g. Raspberry Pi)
```
flashrom -p linux_spi:dev=<spidev>,spispeed=<spispeed> -r <OUTFILE> -f -c <chipname>
```

## Read from BusPirate
```
flashrom -p buspirate_spi:dev=<buspirate>,spispeed=<spispeed> -r <OUTFILE>
```

## Force read from BusPirate
```
flashrom -p buspirate_spi:dev=<buspirate>,spispeed=<spispeed> -r <OUTFILE> -f -c <chipname>
```

= spidev: /dev/spidev0.0
= spispeed: 1M
= buspirate: /dev/ttyUSB0
