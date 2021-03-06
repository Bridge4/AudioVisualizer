
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def get_fractal_data(MAX_ITERATIONS):

    # This is the part of the code where im going to put the fractal equation
    # The fractal equation is going to determine the real and imaginary data points to be plotted
    # fc(z) = z^2 +c where c is a complex number
    # we iterate z by c starting at z = 0
    # start at c = 0, increment, if z is bounded, add c to data file
    # In this case c is the 'imaginary' part of the complex number

    data_file = open("example.txt", 'w')
    bounded = False
    for x in [float(j) / 100 for j in range(-100, 101, 1)]:
        for y in [float(j) / 100 for j in range(-100, 101, 1)]:
            c = complex(x, y)
            z = 0
            i = 0
            while i <= MAX_ITERATIONS:
                z = (z**2) + c.real
                if (abs(complex(z, y))) <= 2:
                    data_file.write(str(c.real) + ' + ' + str(c.imag) + 'i' + '\n')
                    break
                i += 1
            y = y + 0.1
        x = x + 0.1
    data_file.close()


def bifurcation_data(factor, current_pop):
    data_file = open("example.txt", "a")
    for i in range(0, 20000):
        n_year_pop = factor*n_year_pop(1 - n_year_pop)
        data_file.write(str(population) + ', ' + str(factor) + '\n')
        factor += 0.01
        x += 0.01
    data_file.close()

def animate(i):
    graph_data = open('example.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)
    ax1.plot(xs, ys)


def main():
    bifurcation_data(1, 1)
    ani = animation.FuncAnimation(fig, animate, interval=20)
    plt.show()

main()

















































