import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

def determine_sensor_paths():
    sensor_folder_pattern = "28-00000*"
    devices_base_dir = "/sys/bus/w1/devices/"
    sensor_path_glob = glob.glob(os.path.join(devices_base_dir, sensor_folder_pattern))
    return [os.path.join(p, "w1_slave") for p in sensor_path_glob]

def get_file_contents(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temperature(path):
    lines = get_file_contents(path)

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = get_file_contents(path)

    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

sensor_paths = determine_sensor_paths()

while True:
    for sp in sensor_paths:
        print("%s %s" % sp, read_temperature(sp))
        time.sleep(1)
