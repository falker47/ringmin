"""Bounded falsification diagnostic; mpmath values are not certificates."""

import mpmath as mp


def edges(k, c):
    n = 4*k+c
    size = n-k+1
    h = size//2
    result = [(k, n)]
    if size % 2 == 0:
        result.append((k+h-1, k+h))
        result += [(i, n+k-1-i) for i in range(k, k+h-1)]
        result += [(i, n+k+1-i) for i in range(k+1, k+h)]
    else:
        result += [(i, n+k-1-i) for i in range(k, k+h)]
        result += [(i, n+k+1-i) for i in range(k+1, k+h+1)]
    return result


def values(k, c):
    pairs = edges(k, c)
    def residual(r):
        return mp.fsum(mp.asin(mp.sqrt(mp.mpf(a)*b/((r+a)*(r+b))))
                       for a, b in pairs)-mp.pi
    root = mp.findroot(residual, (2*mp.mpf(k)**2, 3*mp.mpf(k)**2))
    t = mp.mpf(1)/k
    a, b, g = 4+c*t, 4+(c-1)*t, 9+(2*c-1)*t
    u = a*b+a+b
    h = (32*(2*c-1)+(48*c*(c-1)+9)*t
         + 6*c*(c-1)*(2*c-1)*t**2+c*c*(c-1)**2*t**3)
    threshold = k*k*a*b*(u+2*mp.sqrt(a*b*g))/h
    return root, threshold, root-threshold


def main():
    mp.mp.dps = 80
    print('diagnostic_only=true dps=80 range=6..20 stop=first_failure')
    previous = {c: values(6, c) for c in (5, 6)}
    for k in range(6, 21):
        failed = False
        for c in (5, 6):
            current = values(k+1, c)
            delta = current[2]-previous[c][2]
            expected = delta < 0 if c == 5 else delta > 0
            print(f'k={k} c={c} delta={mp.nstr(delta, 45)} expected={expected}')
            if not expected:
                failed = True
                for index, row in ((k, previous[c]), (k+1, current)):
                    print(f'k={index} c={c} R={mp.nstr(row[0], 65)} '
                          f'T={mp.nstr(row[1], 65)} D={mp.nstr(row[2], 65)}')
            previous[c] = current
        if failed:
            return


if __name__ == '__main__':
    main()
