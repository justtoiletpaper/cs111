import matplotlib.pyplot as plt


def plot_histogram():
    gpa = []
    sat = []
    with open('admission_algorithms_dataset.csv') as f:
        lines = f.readlines()
        lines = lines[1:]
        for line in lines:
            txt_lst = line.split(',')
            for txt in txt_lst:
                txt = txt.strip()
            sat.append(float(txt_lst[1]))
            gpa.append(float(txt_lst[2]))

    plt.hist(gpa)
    # plt.hist(gpa, [2, 2.5, 3, 3.5, 4, 4])
    # plt.title('Student GPAs')
    # plt.xlabel('GPA')
    # plt.ylabel('Count')
    plt.savefig('gpa.png')
    plt.clf()

    plt.hist(sat)
    # plt.hist(sat, [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1600])
    # plt.title('Student SATs')
    # plt.xlabel('SAT')
    # plt.ylabel('Count')
    plt.savefig('sat_score.png')
    plt.clf()

    return gpa, sat


def plot_scatter():
    scores = plot_histogram()
    gpa = scores[0]
    sat = scores[1]
    plt.scatter(gpa, sat)
    plt.savefig('correlation.png')
    plt.clf()


def plot_spectra():
    def retrieve(file):
        wave_lst = []
        flux_lst = []
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                txt_lst = line.split()
                wavelength = txt_lst[0]
                wave_lst.append(float(wavelength))
                flux = txt_lst[1]
                flux_lst.append(float(flux))
        return wave_lst, flux_lst

    dataset1 = retrieve('spectrum1.txt')
    dataset2 = retrieve('spectrum2.txt')
    plt.plot(dataset1[0], dataset1[1], 'b')
    plt.plot(dataset2[0], dataset2[1], 'g')
    plt.savefig('spectra.png')


def main():
    # plot_histogram()
    plot_scatter()
    plot_spectra()
    pass


if __name__ == "__main__":
    main()
