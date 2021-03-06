from sympy import cos, diag, sin, symbols

from einsteinpy.symbolic import constants
from einsteinpy.symbolic.metric import MetricTensor


def Schwarzschild(c=constants.c, sch=symbols("r_s")):
    """
    Schwarzschild exterior metric in curvature coordinates
    Schwarzschild, Sitz. Preuss. Akad. Wiss., p189, (1916)
    Stephani (13.19) p157

    Parameters
    ----------
    c : ~sympy.core.basic.Basic or int or float
        Any value to assign to speed of light. Defaults to ``c``.
    sch : ~sympy.core.basic.Basic or int or float
        Any value to assign to Schwarzschild Radius of the central object. 
        Defaults to ``r_s``.
    
    """
    coords = symbols("t r theta phi")
    t, r, theta, phi = coords
    val1, c2 = 1 - sch / r, c ** 2
    metric = diag(
        val1, -1 / (val1 * c2), -1 * (r ** 2) / c2, -1 * ((r * sin(theta)) ** 2) / c2
    ).tolist()
    return MetricTensor(metric, coords, "ll")


def Kerr(c=constants.c, sch=symbols("r_s"), a=symbols("a")):
    """
    Kerr Metric in Boyer Lindquist coordinates.

    Parameters
    ----------
    c : ~sympy.core.basic.Basic or int or float
        Any value to assign to speed of light. Defaults to ``c``.
    sch : ~sympy.core.basic.Basic or int or float
        Any value to assign to Schwarzschild Radius of the central object. 
        Defaults to ``r_s``.
    a : ~sympy.core.basic.Basic or int or float
        Spin factor of the heavy body. Usually, given by ``J/(Mc)``,
        where ``J`` is the angular momentum.
        Defaults to ``a``.

    """
    coords = symbols("t r theta phi")
    t, r, theta, phi = coords
    Sigma = r ** 2 + (a ** 2 * cos(theta) ** 2)
    Delta = r ** 2 - sch * r + a ** 2
    c2 = c ** 2

    metric = diag(
        1 - (sch * r / Sigma),
        -Sigma / (Delta * c2),
        -Sigma / c2,
        -(
            (r ** 2 + a ** 2 + (sch * r * (a ** 2) * (sin(theta) ** 2) / Sigma))
            * (sin(theta) ** 2)
        )
        / c2,
    ).tolist()
    metric[0][3] = metric[3][0] = sch * r * a * (sin(theta) ** 2) / (Sigma * c)
    return MetricTensor(metric, coords, "ll")


def KerrNewman(
    c=constants.c, G=constants.G, sch=symbols("r_s"), a=symbols("a"), Q=symbols("Q")
):
    raise NotImplementedError
