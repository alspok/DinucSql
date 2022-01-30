class StringToFloat():
    
    def stringToFloat(self, string_list: list) -> list:
        float_list = []
        for item in string_list:
            tmp_list = [float(itm) for itm in item.split(',')]
            float_list.append(tmp_list)
            
        return float_list