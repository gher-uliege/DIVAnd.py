# divand.py

[![Build Status](https://travis-ci.org/gher-ulg/divand.py.svg?branch=master)](https://travis-ci.org/gher-ulg/divand.py)

`divand` performs an n-dimensional variational analysis of arbitrarily located observations (python interface).<br>
This package is a python interface to `divand`, written in Julia.


## Installation

Besides Python and [NumPy](http://www.numpy.org/) you need to:

* Install [Julia](http://julialang.org/downloads/)
* Install the Julia package `PyCall`

```julia
Pkg.add("PyCall")
```

* Install the Julia package `divand`

```julia
Pkg.clone("https://github.com/gher-ulg/divand.jl")
```

* Install python package [pyjulia](https://github.com/JuliaPy/pyjulia)

`divand.py` is tested with Python 2.7 but should also work with Python 3 once `pyjulia` is installed properly.

```bash
git clone https://github.com/JuliaPy/pyjulia
cd pyjulia/
python setup.py install
```

* Clone this package

```bash
git clone https://github.com/gher-ulg/divand.py
```

## Testing

You are advised to try one of these examples in the directory `examples`:

* [divand_argo.py](https://github.com/gher-ulg/divand.py/blob/master/examples/divand_argo.py)
* [divand_small.py](https://github.com/gher-ulg/divand.py/blob/master/examples/divand_small.py)

The environment variable `PYTHONPATH` should contain the directory with the file `divand.py`.

You can set this variable for the current shell and then run the example:

```bash
export PYTHONPATH="$HOME/src/divand.py/divand:$PYTHONPATH"
python divand_argo.py
```

or just for a single call of the python script (the following command should be on one line):

```bash
PYTHONPATH="$HOME/src/divand.py/divand:$PYTHONPATH" python divand_argo.py
```

Note that you should adapt the path in the previous example (`$HOME/src/divand.py/divand`) to match the installation location of `divand.py`.


## Troubleshooting

### Segmentation fault at initialization of pyjulia

On Ubuntu, the default python interpreter (`/usr/bin/python`) produces a segmentation fault because it is linked statically to libpython2.7.so. As a work-around, use the python interpreter from e.g. Conda after installing the julia package `Conda.jl`. The python interpreter is located at `$HOME/.julia/v0.6/Conda/deps/usr/bin/python2.7`.

### C++ runtime library error

If you see the following error:

```
OSError: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.20' not found (required by /home/abarth/opt/julia-3c9d75391c/bin/../lib/libjulia.so.0.5)
```

Define the variable `LD_PRELOAD` before starting python or (ipython)

```bash
export LD_PRELOAD="$HOME/opt/julia-3c9d75391c/lib/julia/libstdc++.so.6"
```

You should adapt the path in the previous command to match the installation location of Julia.

### Python crash

On some systems, python crashes on `j = julia.Julia()` (https://github.com/JuliaPy/pyjulia/issues/66). Rebuilding `PyCall` after installing `juliapy` seems to solve this issue. In Julia, run the following command:

```julia
Pkg.build("PyCall")
```

### Exception 'UVError'

```
could not spawn `/home/abarth/.local/lib/python2.7/site-packages/julia-0.1.1-py2.7.egg/julia/../fake-julia/julia -Cx86-64 -J/home/abarth/opt/julia-0.6.0/lib/julia/sys.so --compile=yes --depwarn=yes -O0 --output-ji /home/abarth/Test/julia-v0.6-dev/lib/pyjulia2-v0.6/PyCall.ji --output-incremental=yes --startup-file=no --history-file=no --color=no --eval 'while !eof(STDIN)
    eval(Main, deserialize(STDIN))
end
'`: no such file or directory (ENOENT)Traceback (most recent call last):
  File "test_simple_module.py", line 2, in <module>
    j = julia.Julia()
  File "/home/abarth/.local/lib/python2.7/site-packages/julia-0.1.1-py2.7.egg/julia/core.py", line 361, in __init__
    self._call(u"using PyCall")
  File "/home/abarth/.local/lib/python2.7/site-packages/julia-0.1.1-py2.7.egg/julia/core.py", line 403, in _call
    self.check_exception(src)
  File "/home/abarth/.local/lib/python2.7/site-packages/julia-0.1.1-py2.7.egg/julia/core.py", line 423, in check_exception
    .format(exception_type, src))
julia.core.JuliaError: Exception 'UVError' occurred while calling julia code:
using PyCall
```

```julia
Pkg.build("PyCall")
using PyCall
```

### Julia exception: MethodError

If you optain the following error by running one of the examples, consider to upgrade `PyCall` (to a version later than 1.14 or using the git version)

```
WARNING: redefining constant JULIA_HOME
Traceback (most recent call last):
  File "divand_small.py", line 25, in <module>
    va = divand(mask, (pm, pn), (xi, yi), (x, y), v, (lenx, leny), epsilon2)
  File "/home/abarth/src/divand.py/divand/divand.py", line 14, in divand
    x, f, corlen, epsilon2)
RuntimeError: Julia exception: MethodError(divand.divandrunfi, (Bool[true true true true; true true true true; true true true true], ([2.0 2.0 2.0 2.0; 2.0 2.0 2.0 2.0; 2.0 2.0 2.0 2.0], [3.0 3.0 3.0 3.0; 3.0 3.0 3.0 3.0; 3.0 3.0 3.0 3.0]), ([0.0 0.0 0.0 0.0; 0.5 0.5 0.5 0.5; 1.0 1.0 1.0 1.0], [0.0 0.333333 0.666667 1.0; 0.0 0.333333 0.666667 1.0; 0.0 0.333333 0.666667 1.0]), ([1.0e-10 0.5 1.0; 1.0e-10 0.5 1.0; 1.0e-10 0.5 1.0], [1.0e-10 1.0e-10 1.0e-10; 0.5 0.5 0.5; 1.0 1.0 1.0]), [6.0e-10 0.14112 -0.279415; -5.93995e-10 -0.139708 0.276619; 5.76102e-10 0.135499 -0.268286], (0.15, 0.15), 0.05), 0x000000000000553e)
```




<!--  LocalWords:  divand py variational PyCall pyjulia cd argo LD
 -->
<!--  LocalWords:  PYTHONPATH PRELOAD runtime
 -->
