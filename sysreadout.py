import psutil
import GPUtil
from tabulate import tabulate
import platform
from datetime import datetime, timedelta

def sysreadout():
    loadout = []

    def get_size(bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    loadout.append(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

    # let's print CPU information
    loadout.append(f"Total CPU Usage: {psutil.cpu_percent()}%")

    # Memory Information

    svmem = psutil.virtual_memory()
    loadout.append(f"Memory Percentage: {svmem.percent}%")

    # Disk Information
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        loadout.append(f"Disk Total Size: {get_size(partition_usage.total)}")
        loadout.append(f"Disk Usage Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()

    # Network information
    # print("="*40, "Network Information", "="*40)
    # # get all network interfaces (virtual and physical)
    # if_addrs = psutil.net_if_addrs()
    # for interface_name, interface_addresses in if_addrs.items():
    #     for address in interface_addresses:
    #         print(f"=== Interface: {interface_name} ===")
    #         if str(address.family) == 'AddressFamily.AF_INET':
    #             print(f"  IP Address: {address.address}")
    #             print(f"  Netmask: {address.netmask}")
    #             print(f"  Broadcast IP: {address.broadcast}")
    #         elif str(address.family) == 'AddressFamily.AF_PACKET':
    #             print(f"  MAC Address: {address.address}")
    #             print(f"  Netmask: {address.netmask}")
    #             print(f"  Broadcast MAC: {address.broadcast}")
    # # get IO statistics since boot
    # net_io = psutil.net_io_counters()
    # print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    # print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

    # GPU information

    # print("="*40, "GPU Details", "="*40)
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        # get the GPU id
        gpu_id = gpu.id
        # name of GPU
        gpu_name = gpu.name
        # get % percentage of GPU usage of that GPU
        gpu_load = f"{gpu.load*100}%"
        # get free memory in MB format
        gpu_free_memory = f"{gpu.memoryFree}MB"
        # get used memory
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        # get total memory
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))

    # print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
    #                                    "temperature", "uuid")))

    # doesn't seem to fire for inbuilt GPU for surface pro so i'll test that line on my desktop

    # to keep:

    # boot time
    # total cpu usage
    # memory usage (not probably listed with label)
    # disk space free percentage
    # bytes sent
    # bytes received
        
    lstr = ""
    for item in loadout:
        lstr += item
        lstr += "\n"
    
    return lstr[0:-1]

# print(sysreadout())

# alright now set it as an exporting function, incorporate it into the bot, and call it good
