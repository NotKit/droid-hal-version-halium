# rpm_device is the name of the ported device
%define rpm_device x86
# rpm_vendor is used in the rpm space
%define rpm_vendor generic
# Manufacturer and device name to be shown in UI
%define vendor_pretty Generic
%define device_pretty x86
# See ../droid-hal-version/droid-hal-device.inc
%define have_ffmemless 1
#define have_led 0
%define native_build 1
%include droid-hal-version/droid-hal-version.inc
