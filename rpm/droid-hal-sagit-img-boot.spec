%define device sagit

%define mkbootimg_cmd mkbootimg --ramdisk %{initrd}  --kernel %{kernel} --base 0x00000000 --pagesize 4096 --cmdline \"androidboot.console=ttyMSM0 androidboot.hardware=qcom msm_rtb.filter=0x37 ehci-hcd.park=3 service_locator.enable=1 swiotlb=2048 loop.max_part=7\" --board '' --output

%define root_part_label userdata

%define display_brightness_path /sys/devices/soc/c900000.qcom,mdss_mdp/c900000.qcom,mdss_mdp:qcom,mdss_fb_primary/leds/lcd-backlight/brightness
%define display_brightness 1024

%define lvm_root_size 5000
%include initrd/droid-hal-device-img-boot.inc
