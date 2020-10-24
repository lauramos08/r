import os

# list = [866037040488871, 869819042192529, 869819042192560, 868384048926066]
# schedule = []
#
# for idx, imei in enumerate(list):
#     print(idx)
#     returned_value = os.system("curl http://bart.betstream.betgenius.com/fixture-info?venue={}".format(imei))
#     print('')

list = [7303659, 7345394, 7345395, 7214956]
fixtures = ''
for fixture in list:
    fixtures += '{}|'.format(fixture)

battery = 'max by(fixture_id, device_id)(battery_level{{fixture_id=~"{}"}})'.format(fixtures[:-1])
temperature = 'max by(fixture_id, device_id)(battery_temperature{{fixture_id=~"{}"}})'.format(fixtures[:-1])
battery_plugged = 'max by(fixture_id, device_id)(battery_plugged{{fixture_id=~"{}"}})'.format(fixtures[:-1])
is_streaming = 'max by(fixture_id, device_id)(is_streaming{{fixture_id=~"{}"}})'.format(fixtures[:-1])
upload_speed = 'max by(fixture_id, device_id)(wlan_bandwidth_upload{{fixture_id=~"{}"}})'.format(fixtures[:-1])

print(battery)
print(temperature)
print(battery_plugged)
print(is_streaming)
print(upload_speed)
