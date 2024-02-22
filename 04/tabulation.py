from matplotlib import pyplot as plt

def func(x: list[float], N: int) -> list[float]:
    """
    Calculate function values for passed array of arguments
    """
    return [1 - ((t - N/2) / (N/2))**2 for t in x]

def tabulate(a: float, b: float, n: int, N: int) -> tuple[list[float], list[float]]:
    x = [a + i*(b - a)/n for i in range(n)]
    y = func(x, N)
    return x, y

def main():
    N = 17
    res = tabulate(0, 25, 1000, N)

    plt.plot(res[0], res[1])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
