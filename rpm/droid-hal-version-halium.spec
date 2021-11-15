# rpm_device is the name of the ported device
%define rpm_device halium
# rpm_vendor is used in the rpm space
%define rpm_vendor halium
# Manufacturer and device name to be shown in UI
%define vendor_pretty Halium
%define device_pretty Generic Device
# See ../droid-hal-version/droid-hal-device.inc
%define have_ffmemless 1
%define have_led 1
%define native_build 1
%include droid-hal-version/droid-hal-version.inc
