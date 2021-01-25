
cdef extern from "c_file_example.c":
    int sum(int, int)


cpdef int f(int a, int b):
    return sum(a, b)
