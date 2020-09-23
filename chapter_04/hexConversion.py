# -*- coding: utf-8 -*-


class HexConversion:
    # any hex converison

    baseConversionStr = "0123456789ABCDEF"
    
    def hexConversion(self, number, base):
        if number < base:
            return self.baseConversionStr[number]
        else:
            return self.hexConversion(number//base, base) + self.baseConversionStr[number%base]

if __name__ == "__main__":
    hexConversion = HexConversion()
    print(hexConversion.hexConversion(1231323124125412, 2))
    print(hexConversion.hexConversion(1231323124125412, 3))
    print(hexConversion.hexConversion(1231323124125412, 5))
    print(hexConversion.hexConversion(1231323124125412, 7))