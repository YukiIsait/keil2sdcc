# keil2sdcc

Python实现的脚本将Keil头文件的C51特殊语句转为SDCC的宏

**转换后的文件应添加`#include <compiler.h>`**

compiler.h在SDCC的include/mcs51下

它用宏判断了编译器环境, 使头文件能在SDCC/Keil/IAR等多种编译器使用
