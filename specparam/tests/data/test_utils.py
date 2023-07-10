"""Tests for the specparam.data.utils."""

from copy import deepcopy

from specparam.data.utils import *

###################################################################################################
###################################################################################################

def test_get_periodic_labels():

    keys = ['cf', 'pw', 'bw']

    tdict1 = {
        'offset' : [1, 1],
        'exponent' : [1, 1],
        'error' : [1, 1],
        'r_squared' : [1, 1],
    }

    out1 = get_periodic_labels(tdict1)
    assert isinstance(out1, dict)
    for key in keys:
        assert key in out1
        assert len(out1[key]) == 0

    tdict2 = deepcopy(tdict1)
    tdict2.update({
        'cf_0' : [1, 1],
        'pw_0' : [1, 1],
        'bw_0' : [1, 1],
    })
    out2 = get_periodic_labels(tdict2)
    for key in keys:
        assert len(out2[key]) == 1
        for el in out2[key]:
            assert key in el

    tdict3 = deepcopy(tdict1)
    tdict3.update({
        'alpha_cf' : [1, 1],
        'alpha_pw' : [1, 1],
        'alpha_bw' : [1, 1],
        'beta_cf' : [1, 1],
        'beta_pw' : [1, 1],
        'beta_bw' : [1, 1],
    })
    out3 = get_periodic_labels(tdict3)
    for key in keys:
        assert len(out3[key]) == 2
        for el in out3[key]:
            assert key in el
