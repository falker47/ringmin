"""Separate symbolic cross-check; imports SymPy, no task or production code.

The primary certificate checker is stdlib-only. This optional audit uses
the pre-existing SymPy installation to check the algebra independently.
"""

import sympy as s


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    t = s.symbols('t', positive=True)
    for c in (5, 6):
        a, b, g = 4+c*t, 4+(c-1)*t, 9+(2*c-1)*t
        z, u = s.expand(a*b*g), s.expand(a*b+a+b)
        h = (32*(2*c-1)+(48*c*(c-1)+9)*t
             +6*c*(c-1)*(2*c-1)*t*t+c*c*(c-1)**2*t**3)
        p, j = a*b*u, 2*a*b
        f = (p+j*s.sqrt(z))/h
        p1 = 2*h*p-t*h*s.diff(p, t)+t*s.diff(h, t)*p
        j1 = 2*h*j-t*h*s.diff(j, t)+t*s.diff(h, t)*j
        den, nr = 2*z*h*h, 2*z*p1
        ns = 2*z*j1-t*h*j*s.diff(z, t)
        require(s.simplify(2*f-t*s.diff(f, t)-(nr+ns*s.sqrt(z))/den) == 0,
                'threshold derivative')
        require(s.expand(u*u-4*z-t*h) == 0, 'conjugate identity')
        leading = s.Rational(24, 2*c-1)
        linear = {5: s.Rational(61, 36), 6: s.Rational(2447, 1452)}[c]
        gates = [ns]
        for sign in (-1, 1):
            m = (2*leading+(linear+sign*s.Rational(1, 8))*t)*den-nr
            gates += [m, sign*(m*m-ns*ns*z)]
        for index, gate in enumerate(gates):
            p = s.Poly(gate, t)
            degree = p.degree()
            values = [sum(p.nth(i)*s.binomial(degree-i, j-i)/6**i
                          for i in range(j+1)) for j in range(degree+1)]
            require(all(v > 0 for v in values[1:]), 'positive coefficients')
            require(values[0] == 0 if index in (2, 4) else values[0] > 0,
                    'constant coefficient')
            require(values[-1] == p.eval(s.Rational(1, 6)) > 0,
                    'closed endpoint')
        print(f'symbolic_threshold_derivative_conjugate_and_five_gates=PASS c={c}')

    x = s.symbols('x', positive=True)
    a = 3*s.sqrt(4+x)+s.Rational(5, 2)*(5+x)*s.asin((3+x)/(5+x))
    b = (8+x)/(2*s.sqrt(4+x))
    require(s.simplify(s.diff(a, x, 2)-x/(2*(5+x)*(4+x)**s.Rational(3, 2))) == 0,
            'A second derivative')
    require(s.simplify(s.diff(b, x)-x/(4*(4+x)**s.Rational(3, 2))) == 0,
            'B first derivative')
    k, c = s.symbols('k c', positive=True)
    n, length, distance = 4*k+c, 5*k+c, 3*k+c
    w = s.sqrt(k*n)
    integral = distance*w/2+length**2*s.asin(distance/length)/4
    expected = 3*w+5*length*s.asin(distance/length)/2+(8*k+c)/(2*w)
    require(s.simplify(s.diff(integral+w, k)-expected) == 0, 'F derivative')
    y, ell, m = s.symbols('y ell m')
    # If g=sqrt(q)>0 then g''=(2q q''-(q')^2)/(4q^(3/2)).
    # Clear this positive denominator to avoid symbolic branch ambiguity.
    q = (y+m)*(ell-y+m)
    require(s.expand(2*q*s.diff(q, m, 2)-s.diff(q, m)**2+(ell-2*y)**2) == 0,
            'g second derivative numerator')
    q = y*(ell-y)
    require(s.expand(2*q*s.diff(q, y, 2)-s.diff(q, y)**2+ell**2) == 0,
            'w second derivative numerator')
    print('symbolic_F_A_B_w_g_derivatives=PASS')
    print(f'sympy={s.__version__} exact_arithmetic=YES checker_imports=0 diagnostic_imports=0')


if __name__ == '__main__':
    main()
