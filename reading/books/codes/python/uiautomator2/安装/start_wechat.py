import uiautomator2 as u2

ph = u2.connect_usb(serial='JGU30LND62JF9D9H')  # 通过 adb devices 可以查看设备码

ph.app_start('com.tencent.mm')
