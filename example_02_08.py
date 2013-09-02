import argparse

def run_expt(m, n):
    pw = []
    for k in range(n+2):
        p = 0
        for i in range(k+1):
            t = 1.0
            for j in range(i):
                t = t * (n - j) / (m + n - j)
            p = p + t * m / (m+n-i)
        pw.append(p)
    return pw
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enter two integers.")
    parser.add_argument('-m', help='Number of white balls', type=int)
    parser.add_argument('-n', help='Number of black balls', type=int)
    args = parser.parse_args()
    print args
    m = args.m
    n = args.n
    pw = run_expt(m, n)
    f = open('example_02_08.dat', 'w')
    for i, v in enumerate(pw):
        data = str(i) + ' ' + str(v) + '\n'
        f.write(data)
    f.close()
