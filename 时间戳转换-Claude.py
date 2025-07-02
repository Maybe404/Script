#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
时间戳转换工具
支持Unix时间戳与北京时间的相互转换
"""

import datetime
import pytz
import time

def timestamp_to_beijing(timestamp):
    """
    将Unix时间戳转换为北京时间
    
    Args:
        timestamp: Unix时间戳（秒或毫秒）
    
    Returns:
        str: 格式化的北京时间字符串
    """
    try:
        # 判断是秒级还是毫秒级时间戳
        if len(str(int(timestamp))) == 13:
            timestamp = timestamp / 1000
        elif len(str(int(timestamp))) == 10:
            timestamp = timestamp
        else:
            return "时间戳格式错误，请输入10位或13位数字"
        
        # 创建UTC时间
        utc_time = datetime.datetime.fromtimestamp(timestamp, tz=pytz.UTC)
        
        # 转换为北京时间
        beijing_tz = pytz.timezone('Asia/Shanghai')
        beijing_time = utc_time.astimezone(beijing_tz)
        
        return beijing_time.strftime('%Y-%m-%d %H:%M:%S')
    
    except Exception as e:
        return f"转换失败: {str(e)}"

def beijing_to_timestamp(time_str):
    """
    将北京时间转换为Unix时间戳
    
    Args:
        time_str: 时间字符串，格式如 '2025-07-02 18:04:11'
    
    Returns:
        int: Unix时间戳（秒级）
    """
    try:
        # 解析时间字符串
        dt = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        
        # 设置为北京时区
        beijing_tz = pytz.timezone('Asia/Shanghai')
        beijing_time = beijing_tz.localize(dt)
        
        # 转换为时间戳
        timestamp = int(beijing_time.timestamp())
        
        return timestamp
    
    except Exception as e:
        return f"转换失败: {str(e)}"

def get_current_timestamp():
    """获取当前时间戳"""
    return int(time.time())

def get_current_beijing_time():
    """获取当前北京时间"""
    beijing_tz = pytz.timezone('Asia/Shanghai')
    now = datetime.datetime.now(beijing_tz)
    return now.strftime('%Y-%m-%d %H:%M:%S')

def main():
    """主函数 - 交互式命令行界面"""
    print("=" * 50)
    print("时间戳转换工具")
    print("=" * 50)
    
    while True:
        print("\n请选择操作:")
        print("1. 时间戳转北京时间")
        print("2. 北京时间转时间戳")
        print("3. 获取当前时间戳")
        print("4. 获取当前北京时间")
        print("5. 退出")
        
        choice = input("\n请输入选项 (1-5): ").strip()
        
        if choice == '1':
            timestamp = input("请输入时间戳: ").strip()
            try:
                timestamp = float(timestamp)
                result = timestamp_to_beijing(timestamp)
                print(f"北京时间: {result}")
            except ValueError:
                print("输入的时间戳格式错误")
        
        elif choice == '2':
            time_str = input("请输入北京时间 (格式: YYYY-MM-DD HH:MM:SS): ").strip()
            result = beijing_to_timestamp(time_str)
            if isinstance(result, int):
                print(f"时间戳: {result}")
            else:
                print(result)
        
        elif choice == '3':
            timestamp = get_current_timestamp()
            print(f"当前时间戳: {timestamp}")
        
        elif choice == '4':
            beijing_time = get_current_beijing_time()
            print(f"当前北京时间: {beijing_time}")
        
        elif choice == '5':
            print("感谢使用!")
            break
        
        else:
            print("无效选项，请重新选择")

if __name__ == "__main__":
    # 演示用法
    print("演示:")
    print(f"时间戳 1751424117 -> {timestamp_to_beijing(1751424117)}")
    print(f"北京时间 '2025-07-02 18:04:11' -> {beijing_to_timestamp('2025-07-02 18:04:11')}")
    print(f"当前时间戳: {get_current_timestamp()}")
    print(f"当前北京时间: {get_current_beijing_time()}")
    
    # 启动交互界面
    main()