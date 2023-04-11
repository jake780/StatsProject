from random import choice
import matplotlib.pyplot as plt

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
            formattedStr += f"{item}{' '*(9-len(item))} : {self.tempDict[item]}°F\n"
        return formattedStr

    def analyzeData(self):
        """Displays a summary of all possible Statistical methods"""
        # Sample Mean
        print(f"Sample Mean: {'%.2f' % self.sampleMean()}\n")

        # Sample Median
        print(f"Sample Median: {self.sampleMedian()}\n")

        # Sample Modes
        print(f"Same Modes: {self.sampleMode()}\n")

        # Sample Variance
        print(f"Sample Variance: {'%.2f' % self.sampleVariance()}\n")

        # Sample Standard Deviation
        print(f"Sample Standard Dev: {'%.2f' % self.sampleStandardDeviation()}\n")

        # Simple Random Sample of 20
        print("Simple Random Sample of size 20")
        sample = self.randomSample(20)
        print(f"Sample Mean: {'%.2f' % sample[0]}\nSample Variance: {'%.2f' % sample[1]}\n")

        # 5%, 10%, 20% Trimmed mean
        print(f"5% Trimmed Mean: {'%.2f' %self.trimmedMean(5)}\n")
        print(f"10% Trimmed Mean: {'%.2f' %self.trimmedMean(10)}\n")
        print(f"20% Trimmed Mean: {'%.2f' %self.trimmedMean(20)}\n")

        # First and Third Quartiles
        print(f"First Quartile: {self.quartile(0.25)}\n")
        print(f"Third Quartile: {self.quartile(0.75)}\n")

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

    def sampleMode(self):
        """Returns the mode temperature"""
        # Count occurences of each value
        tempCounts = {}
        for t in self.sortedTemps:
            if t not in tempCounts:
                tempCounts[t] = 1
            else:
                tempCounts[t] += 1
        # Find the largest amount of occurences
        maxVal = 0
        for t in tempCounts:
            if tempCounts[t] > maxVal:
                maxVal = tempCounts[t]
        # Return a list of all temps with the most occurences
        tempList = []
        for t in tempCounts:
            if tempCounts[t] == maxVal:
                tempList.append(t)
        return tempList


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

    def trimmedMean(self, percent):
        """Returns the percent trimmed mean"""
        """percent should be given as a whole number"""
        percent = percent / 100
        edge = round(percent * len(self.sortedTemps))
        slicedTemps = self.sortedTemps[edge:-edge]
        # Calculate mean
        sum = 0
        for t in slicedTemps:
            sum += t
        return (sum/len(slicedTemps))
        
    def quartile(self, num):
        """Returns the num percentile/quartile"""
        """num should be given as a value < 1"""
        index = num * len(self.sortedTemps)
        
        if (index % 1) != 0:
            index = int(index - (index % 1))
            return ((self.sortedTemps[index] + self.sortedTemps[index+1])/2)
        else:
            return self.sortedTemps[index]

    def histogram(self):
        """Creates a Pyplot Histogram of the data"""
        plt.hist(self.sortedTemps, bins=20)
        plt.title("Average Daily Temperature (Jan-Mar) for Provo, Utah")
        plt.minorticks_on()
        plt.xlabel("Temperature")
        plt.ylabel("Frequency")
        plt.show()

def main():
    # Create and instance of the Temperature Stats Class
    T = TempStats()
    # Display a table of the population data
    print(T)
    # Run the statistics methods and display the analysis
    T.analyzeData()

    # Graph the data onto a histogram
    T.histogram()

if __name__ == "__main__":
    main()