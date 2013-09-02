import argparse

def run_expt(m, n):
    pa = []
    even_n = int(n / 2)  # expt can run only for an even number of black balls if player A is to win
    for k in range(even_n+1):
        x = 1.0 * m
        for l in range(2 * k):
            x = x * (n - l)
        y = 1.0
        for s in range(2 * k + 1):
            y = y * (m + n - s)
        p = x / y
        if pa:
            p = p + pa[-1]
        pa.append(p)
    pb = []
    for k in range(even_n+1):
        x = 1.0 * m
        for l in range(2*k+1):
            x = x * (n-l)
        y = 1.0
        for s in range(2*k+2):
            y = y * (m+n-s)
        p = x / y
        if pb:
            p = p + pb[-1]
        pb.append(p)
    return zip(pa, pb)
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Runs simulation to determine the probability that the player who starts a game to pick a white ball wins.")
    parser.add_argument('-m', help='Number of white balls', type=int)
    parser.add_argument('-n', help='Number of black balls', type=int)
    args = parser.parse_args()
    print args
    m = args.m
    n = args.n
    pw = run_expt(m, n)
    f = open('example_02_09.dat', 'w')
    for i, v in enumerate(pw):
        data = str(i) + ' ' + str(v[0]) + ' ' + str(v[1]) + '\n'
        f.write(data)
    f.close()
