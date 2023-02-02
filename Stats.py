class TempStats():
    """Loads and Analyzes average temperature data"""
    def __init__(self):
        self.tempDict = {}
        self.sortedTemps = []
        self.loadData()

    def loadData(self):
        """Load the temperature data into tempDict from the csv file"""
        with open("archive.csv", "r") as tempData:
            for line in tempData:
                line = line.split(",")
                self.tempDict[line[0]] = float(line[1])
                self.sortedTemps.append(float(line[1]))

        # Sort the list of temperatures
        self.sortedTemps.sort()

    def __str__(self):
        """Displays a table of the average temperature data"""
        formattedStr = f"\nDate     : Average Temp(F)\n"
        for item in self.tempDict:
            formattedStr += f"{item} : {self.tempDict[item]}\n"
        return formattedStr

    def analyzeData(self):
        """Displays a summary of all possible Statistical methods"""

        # Sample Mean
        print(f"Sample Mean: {'%.2f' % self.sampleMean()}\n")

        # Sample Median
        print(f"Sample Median: {self.sampleMedian()}\n")

    def sampleMean(self):
        """Returns the average temperature"""
        sum = 0
        for item in self.tempDict:
            sum += self.tempDict[item]
        return (sum/len(self.tempDict))

    def sampleMedian(self):
        """Returns the median temperature"""
        n = len(self.sortedTemps)
        if  (n % 2) == 0:
            #Even
            nLeft = int(n/2)
            nRight = int((n/2)+1)
            return (self.sortedTemps[nLeft] + self.sortedTemps[nRight])/2
        else:
            #Odd
            return self.sortedTemps[n]
            

def main():
    T = TempStats()

    print(T)

    T.analyzeData()

if __name__ == "__main__":
    main()