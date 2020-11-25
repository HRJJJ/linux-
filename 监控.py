import datetime
import psutil


def linux_monitor(time):
    """系统监控"""
    # 定义变量保存cpu的使用率
    cpu_per = psutil.cpu_percent(interval=time)

    # 定义变量保存内存的使用率
    mem_info = psutil.virtual_memory()

    # 定义变量保存硬盘的使用率
    disk_info = psutil.disk_usage("/")

    # 定义变量保存网络的信息
    net_info = psutil.net_io_counters()

    # 获取系统当前时间
    current_time = datetime.datetime.now().strftime("%F %T")

    # 拼接字符串现实内容
    log_str = "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|      监控时间      |  CPU使用率  |   内存使用率  |   硬盘使用率  |          网络收发量          |\n"
    log_str += "|                   | (共%d核CPU)  |  (总计%dG内存) | (总计%dG硬盘)|                            |\n" % (
    psutil.cpu_count(logical=False), mem_info.total / 1024 / 1024 / 1024, disk_info.total / 1024 / 1024 / 1024)
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|%s|    %s%%   |    %s%%    |    %s%%    |   收:%s/发:%s  |\n" % (
    current_time, cpu_per, mem_info.percent, disk_info.percent, net_info.bytes_recv, net_info.bytes_sent)
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    print(log_str)

    # 创建日志保存
    f = open("log.txt", "a")
    f.write(log_str + "\n\n")
    f.close()


def main():
    """程序入口"""
    while True:
        linux_monitor(5)


if __name__ == '__main__':
    main()
