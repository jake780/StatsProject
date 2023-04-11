import matplotlib.pyplot as plt
from random import randint

def main():
    data = [randint(0,50) for _ in range(10)]
    plt.hist(data, bins=4)
    plt.show()

if __name__ == "__main__":
    main()