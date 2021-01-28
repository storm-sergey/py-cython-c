1. python setup.py build_ext --inplace
2. python call_cython_f.py

call_cython_f.py >> (int, int) >> cython_mod.pyx >> (int, int) >> c_file_example
c_file_example >> (return int sum) >> cython_mod.pyx >> (return int) call_cython_f.py