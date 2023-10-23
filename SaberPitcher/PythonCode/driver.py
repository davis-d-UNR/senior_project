from ExcelParser import excelParser
import csv

class driver:
    
    def main():
        pitcher = excelParser()
        pitcher.printAverageSpeed()
        pitcher.printPitchType()
    if __name__ == "__main__":
        main()
        
        
        