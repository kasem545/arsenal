# Objection

% objection, android, ios, frida,
#plateform/linux #target/local #cat/ANDROID
## Patch the app
objection patchapk -s <PACKAGE>

## Patch the app without resource decoding
objection patchapk -D -s <PACKAGE>

## Patch the app with debug flag
objection patchapk -d -s <PACKAGE>

## Launch explore
objection explore

## Launch explore with startup command
objection explore -s <COMMAND>

## Launch explore without default ssl pinning bypass
objection explore -s 'android sslpinning disable'

## Launch explore with startup script
objection explore -S <patch_to_script>
