import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/dgfd.pyx'))

with open(fpath, 'w') as f:
    f.write("""'''
First derivatives of the generalized Fermi-Dirac integrals.

This file was generated by `scripts/gen_gdfd_pyx.py`, and should not
be edited directly.
'''
""")
    f.write('from fdint cimport _fdint\n')
    f.write('import numpy\n')
    for i in xrange(-1,6,2):
        k2 = str(i).replace('-','m')
        f.write('''
def dgfd{k2}h(phi, beta, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(beta, numpy.ndarray) and beta.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _fdint.vdgfd{k2}h(phi, beta, out)
        return out
    else:
        assert not isinstance(beta, numpy.ndarray)
        return _fdint.dgfd{k2}h(phi, beta)
'''.format(k2=k2))
