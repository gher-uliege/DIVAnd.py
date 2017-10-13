# Python 3

On Ubuntu, the default python interpreter (`/usr/bin/python3`) produces a segmentation fault because it is linked statically to libpython3.x.so. As a work-around, one can use the python interpreter from e.g.  miniconda available from https://conda.io/miniconda.html
In the following, miniconda is installed in `/home/abarth/opt/miniconda2` and a conda environement `mytest` is created.

```bash
export PATH="/home/abarth/opt/miniconda2/bin/:$PATH"
export PYTHONNOUSERSITE=1
conda create --name mytest python=3
source activate mytest
```

The command `which python3` should return somthing like `/home/abarth/opt/miniconda2/envs/mytest/bin/python3`.

* Install the dependencies

```bash
conda install pytest
conda install numpy
conda install netCDF4
export PYTHONPATH="$HOME/src/divand.py/divand:$PYTHONPATH"
export JULIA_PKGDIR=$HOME/Test/julia-v0.6-dev
```

Setting the variable `JULIA_PKGDIR` is only necessary if you installed `divand.jl` in a non-standard location.

* Install pyjulia

```bash
git clone https://github.com/JuliaPy/pyjulia
cd pyjulia/
python setup.py clean # unless it is a clean check-out
python setup.py install
cd -
```

* Re-build the julia package `PyCall` with the python interpreter from miniconda.

```bash
export PYTHON=$(which python3)
julia --eval 'Pkg.build("PyCall")'
```

The command `python -c 'import julia'` should return no error.

Run the test suite:

```bash
$ pytest
```

It should return no error:

```
=============================== test session starts ===============================
platform linux -- Python 3.6.2, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
rootdir: /home/abarth/src/divand.py, inifile:
collecting 0 items

collected 4 items

tests/test_divand.py ..
tests/test_divand_run.py ..

============================ 4 passed in 49.99 seconds ============================
```
