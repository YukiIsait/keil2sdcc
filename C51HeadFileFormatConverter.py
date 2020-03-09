# encode: utf-8
import re

class FormatConversion:
    def __init__(self, text: str):
        self.__text: str = text
        self.__sfr_symbol_dict: dict = {}
        self.__get_sfr_symbol_dict()
        self.__replace_sfr_symbol()
        self.__replace_sbit_symbol()

    def get_text(self):
        return self.__text

    def __get_sfr_symbol_dict(self):
        find_list = re.findall(r"sfr\s*([^\s]+)\s*=\s*([^\s]+)\s*;", self.__text)
        for item in find_list:
            key = item[0]
            value = item[1]
            if key not in self.__sfr_symbol_dict: # 存在则不添加
                self.__sfr_symbol_dict[key] = value
    
    def __replace_sfr_symbol(self):
        def __replace_handler(matched):
            return "SFR(%s, %s);" % (matched.group(1), matched.group(2))
        self.__text = re.sub(r"sfr\s*([^\s]+)\s*=\s*([^\s]+)\s*;", __replace_handler, self.__text)

    def __replace_sbit_symbol(self):
        def __replace_handler(matched):
            addr = self.__sfr_symbol_dict[matched.group(2)]
            return "SBIT(%s, %s, %s);" % (matched.group(1), addr, matched.group(3))
        self.__text = re.sub(r"sbit\s*([^\s]+)\s*=\s*([^\s]+)\^(\d+)\s*;", __replace_handler, self.__text)

if __name__ == "__main__":

    KEIL_HEAD_FILE_NAME = "STC15F.H"
    NEW_HEAD_FILE_NAME = "STC15F_NEW.H"

    with open(KEIL_HEAD_FILE_NAME, "r", encoding="GB18030") as rf:
        fc = FormatConversion(rf.read())
        with open(NEW_HEAD_FILE_NAME, "w", encoding="UTF-8") as wf:
            wf.write(fc.get_text())
