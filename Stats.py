from random import choice

class TempStats():
    """Loads and Analyzes average temperature data"""
    def __init__(self):
        self.tempDict = {}
        self.sortedTemps = []
        self.loadData()
        self.n = len(self.tempDict)
        self.mean = self.sampleMean()


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
        formattedStr = f"\nDate      : Average Temp(F)\n"
        for item in self.tempDict:
            formattedStr += f"{item}{' '*(9-len(item))} : {self.tempDict[item]}\n"
        return formattedStr

    def analyzeData(self):
        """Displays a summary of all possible Statistical methods"""

        # Sample Mean
        print(f"Sample Mean: {'%.2f' % self.sampleMean()}\n")

        # Sample Median
        print(f"Sample Median: {self.sampleMedian()}\n")

        # Sample Variance
        print(f"Sample Variance: {'%.2f' % self.sampleVariance()}\n")

        # Sample Standard Deviation
        print(f"Sample Standard Dev: {'%.2f' % self.sampleStandardDeviation()}\n")

        # Simple Random Sample of 20
        print("Simple Random Sample of size 20\n")
        sample = self.randomSample(20)
        print(f"Sample Mean: {sample[0]}\nSample Variance: {sample[1]}")

    def sampleMean(self):
        """Returns the average temperature"""
        sum = 0
        for item in self.tempDict:
            sum += self.tempDict[item]
        return (sum/self.n)

    def sampleMedian(self):
        """Returns the median temperature"""
        if  (self.n % 2) == 0:
            #Even
            nLeft = int(self.n/2)
            nRight = int((self.n/2)+1)
            return (self.sortedTemps[nLeft] + self.sortedTemps[nRight])/2
        else:
            #Odd
            return self.sortedTemps[self.n]

    def sampleVariance(self):
        """Returns the sample variance of the data"""
        sum = 0
        for item in self.sortedTemps:
            sum += ((item - self.mean)**2)
        return sum/self.n

    def sampleStandardDeviation(self):
        """Returns the sample Standard Deviation"""
        return self.sampleVariance()**0.5

    def randomSample(self, amount):
        """Randomly chooses amount items out of the population and computes the mean and sample variance"""
        samples = []
        for _ in range(amount):
            samples.append(choice(self.sortedTemps))

        # Sample mean
        sum = 0
        for s in samples:
            sum += s
        mean = sum/amount

        # Sample Variance
        sum = 0
        for s in samples:
            sum += ((s-mean)**2)
        variance = sum/amount

        return mean, variance
        

def main():
    T = TempStats()
    #print(T)

    T.analyzeData()

if __name__ == "__main__":
    main()