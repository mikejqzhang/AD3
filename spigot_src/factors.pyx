from ad3.base cimport Factor, GenericFactor, PGenericFactor

cdef extern from "FactorTreeFast.h" namespace "sparsemap":
    cdef cppclass FactorTreeFast(GenericFactor):
        FactorTreeFast()
        void Initialize(int length)

