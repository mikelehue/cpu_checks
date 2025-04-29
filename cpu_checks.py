#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This script checks the CPU and Disk usage of the system.
# It uses the psutil library to get the CPU usage and shutil to get the disk usage.
# The script checks if the disk usage is less than 20% and CPU usage is less than 75%.
# If either of these conditions is not met, it prints an error message.
# Otherwise, it prints a success message.
# The script is designed to be run as a standalone script.
# It can be used as a simple monitoring tool to check the system's resource usage.

import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR: CPU or Disk usage is too high!")
else:
    print("Everything is OK!")
