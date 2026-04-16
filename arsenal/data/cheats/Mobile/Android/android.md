# Android Debug Bridge (adb)

% android, device, adb, bridge

#plateform/linux #target/local #cat/ANDROID

## Get property
adb -s <DEVICE> shell getprop <property>

## Install APK
adb -s <DEVICE> install -r <PATH>

## Uninstall package
adb -s <DEVICE> uninstall -r <PACKAGE>

## Clear user data for package
adb -s <DEVICE> shell pm clear <PACKAGE>

## Dispatch a deep-link / open URI
adb -s <DEVICE> shell am start <URI>

## Download apk
adb pull '$(adb shell pm path '$(adb shell pm list packages | grep <PACKAGE> | cut -d : -f 2)' | cut -d : -f 2)' .

## Sign apk with Uber-apk-signer
java -jar uber-apk-signer-1.1.0.jar -a <app>