"""Noncertified diagnostics for the continuous boundary family; writes no files.

Implicit baseline parameters are recomputed from their defining equations.
Bisections and quadrature are numerical observations, never proof premises.
"""
import mpmath as m

m.mp.dps = 70
R = lambda p, q=1: m.mpf(p)/q
STEPS = 180


def bisect(f, lo, hi):
    assert f(lo) < 0 < f(hi)
    for _ in range(STEPS):
        mid = (lo+hi)/2
        if f(mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def branches(A, u, e, s):
    t, X, Y = u+s, A+u+s, A+u+e-s
    return (m.sqrt(X*Y), m.sqrt(t)*(m.sqrt(X)+m.sqrt(Y)),
            max(X, 2*m.sqrt(t*X)))


def cut(A, u, e, raw=False):
    if e == 0:
        return e
    if raw:
        gap = lambda s: branches(A,u,e,s)[1]-branches(A,u,e,s)[0]
    else:
        gap = lambda s: m.sqrt((u+s)/(A+u+s))+m.sqrt((u+s)/(A+u+e-s))-1
    if gap(e) <= 0:
        return e
    return bisect(gap, R(0), e)


def H(T, t):
    return T*m.atan(m.sqrt(t/(T-t)))-m.sqrt(t*(T-t))


def F(t, A):
    return ((2*t+A)*m.sqrt(t*(t+A))
            -A*A*m.log((m.sqrt(t)+m.sqrt(t+A))/m.sqrt(A)))/4


def J(v, radius):
    return (v*m.sqrt(radius*radius-v*v)
            +radius*radius*m.asin(v/radius))/2


def closed(A, u, e):
    if e == 0:
        return R(0), R(0)
    B, z = A+u, cut(A,u,e)
    M, T = B+e/2, B+u+e
    value = (J(z-e/2,M)-J(-e/2,M)
             +F(u+e,A)-F(u+z,A)
             +J(u+e-T/2,T/2)-J(u+z-T/2,T/2)-B*e-e*e/2)
    I = H(2*B+e,B+z)-H(2*B+e,B)
    I += H(T,u+e)-H(T,u+z)
    c0 = m.sqrt(B*(B+e))
    p = m.sqrt(u+e)*(m.sqrt(B+e)+m.sqrt(B))
    return value, max(c0,p)-(B+e)+I/2


def raw_cost(A, u, e):
    z = cut(A,u,e,raw=True)
    w = min(e,max(R(0),A/3-u))
    cuts = sorted(set([R(0),z,w,e]))
    if len(cuts) == 1:
        return R(0)
    def integrand(s):
        c,k,d = branches(A,u,e,s)
        return max(c,k)-d
    return m.quad(integrand,cuts)


# E'(x) from the defining normalized prefix integral, not the new checker.
def prefix_slope(x):
    z = cut(R(1),R(0),x,raw=True)
    I = m.quad(lambda t:m.sqrt((1+t)/(1+x-t)),[0,z])
    I += m.quad(lambda t:m.sqrt(t/(1+x-t)),[z,x])
    return m.sqrt(x)*(m.sqrt(1+x)+1)-(1+x)+I/2


x = bisect(prefix_slope,R(719,2500),R(2877,10000))
saving = raw_cost(R(1),R(0),x)


def alpha_equation(alpha):
    A, b = 1+alpha,1-alpha
    a = A/3
    shift = (a/2+m.quad(lambda t:m.sqrt(t/(t+A)),[a,b])/2
             +m.quad(lambda t:m.sqrt(t/(t+alpha)),[b,1])/2
             -(m.sqrt(2)-1)*m.sqrt(b))
    return shift+A*saving


alpha = bisect(alpha_equation,R(1093,10000),R(10931,100000))
A, u = 1+alpha,(1+alpha)*x
B, h = A+u,A/3-u
tau = bisect(lambda e:branches(A,u,e,e)[1]-branches(A,u,e,e)[0],R(0),h)
slope = lambda e:closed(A,u,e)[1]
eb = bisect(slope,tau,h)
zero = bisect(lambda e:raw_cost(A,u,e),eb,h)
assert R(43,1000)<tau<R(87,2000)
assert tau<eb<tau+tau*tau/(8*B)<R(44,1000)
assert eb<zero<h

probes = [tau/2,tau,(tau+eb)/2,eb,(eb+h)/2,h]
errors = []
for e in probes:
    errors.append(abs(raw_cost(A,u,e)-closed(A,u,e)[0]))
assert len(errors)==6 and max(errors)<R(1,10**48)

step = R(1,10**13)
smooth = [tau/2,(tau+eb)/2,eb,(eb+h)/2]
fd_errors, curvature_errors = [],[]
for e in smooth:
    fd = (raw_cost(A,u,e+step)-raw_cost(A,u,e-step))/(2*step)
    fd_errors.append(abs(fd-slope(e)))
    if e>tau:
        z = cut(A,u,e)
        t, X, Y = u+z,B+z,B+e-z
        zp = t/(A*(Y/X)**R(3,2)+Y+t)
        j = m.quad(lambda s:m.sqrt(B+s)/(B+e-s)**R(3,2),[0,z])
        j += m.quad(lambda s:m.sqrt(u+s)/(B+e-s)**R(3,2),[z,e])
        q = u+e
        pp = (A+2*q)/(2*m.sqrt(q*(A+q)))+m.sqrt(B)/(2*m.sqrt(q))
        curvature = pp-1+m.sqrt(q/B)/2-j/4+zp*(m.sqrt(X)-m.sqrt(t))/(2*m.sqrt(Y))
        curvature_errors.append(abs((slope(e+step)-slope(e-step))/(2*step)-curvature))
        assert curvature>1
assert len(fd_errors)==4 and max(fd_errors)<R(1,10**23)
assert len(curvature_errors)==3 and max(curvature_errors)<R(1,10**23)

tie_error = abs((raw_cost(A,u,tau+step)-raw_cost(A,u,tau-step))/(2*step)-slope(tau))
upper_error = abs((raw_cost(A,u,h)-raw_cost(A,u,h-step))/step-slope(h))
assert tie_error<R(1,10**12) and upper_error<R(1,10**12)
assert slope(tau)<0<slope(h)
assert raw_cost(A,u,h)>11*h*h/1440
assert slope(h)>11*h/280
small = h/R(10**6)
assert abs(raw_cost(A,u,small)/small**3+1/(24*B))<R(1,10**8)
assert (slope(tau)-slope(tau-step))/step<0
assert (slope(tau+step)-slope(tau))/step>1

print('PASS 70-digit diagnostics: baseline x and alpha recomputed from defining equations; 180 bisections per root')
print('PASS 6 raw-full-max/primitive identities <1e-48; 4 smooth central differences <1e-23')
print('PASS 3 mixed curvature identities <1e-23 and values >1; entry C1 and upper one-sided differences <1e-12')
print('PASS endpoint bounds, cubic limit, entry curvature jump, root ordering and analytic distance bound')
for label,value in [('x_star',x),('alpha_hat',alpha),('lambda',u),('h',h),
                    ('tau_b',tau),('epsilon_b',eb),('epsilon_b-tau_b',eb-tau),
                    ('D_b_min',raw_cost(A,u,eb)),('D_b_h',raw_cost(A,u,h)),('positive_zero',zero)]:
    print('DIAGNOSTIC',label,m.nstr(value,26))
print('NOTE: all printed decimals, numerical roots, quadratures and sampled checks are noncertified')
print('mpmath',m.__version__)
