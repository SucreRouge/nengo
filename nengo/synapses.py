class Synapse(object):
    pass


class LinearFilter(Synapse):
    """General linear time-invariant (LTI) system synapse.

    Parameters
    ----------
    num : array_like
        Numerator coefficients of continuous-time transfer function.
    den : array_like
        Denominator coefficients of continuous-time transfer function.
    """

    def __init__(self, num, den):
        import scipy.signal  # Fail early (instead of at builder)
        assert scipy.signal
        self.num = num
        self.den = den

    def __repr__(self):
        return "%s(%s, %s)" % (self.__class__.__name__, self.num, self.den)


class Lowpass(Synapse):
    """Standard first-order lowpass filter synapse.

    Parameters
    ----------
    tau : float
        The time constant of the filter in seconds.
    """
    def __init__(self, tau):
        self.tau = tau

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.tau)


class Alpha(Synapse):
    """Alpha-function filter synapse.

    The impulse-response function is given by

        alpha(t) = (t / tau) * exp(-t / tau)

    and was found by [1]_ to be a good basic model for synapses.

    Parameters
    ----------
    tau : float
        The time constant of the filter in seconds.

    References
    ----------
    .. [1] Mainen, Z.F. and Sejnowski, T.J. (1995). Reliability of spike timing
        in neocortical neurons. Science (New York, NY), 268(5216):1503-6.
    """
    def __init__(self, tau):
        import scipy.signal  # Fail early (instead of at builder)
        assert scipy.signal
        self.tau = tau

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.tau)