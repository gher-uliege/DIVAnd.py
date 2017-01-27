# divand.py
`divand` performs an n-dimensional variational analysis of arbitrarily located observations (python interface)


## Installation

Besides python and numpy you need:

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

`divand.py` is tested with python 2.7 but should also work with python 3 once `pyjulia` is installed properly.

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
export PYTHONPATH="$HOME/src/divand.py/src:$PYTHONPATH"
python divand_argo.py
```

or just for a single call of the python script (the following command should be on one line):

```bash
PYTHONPATH="$HOME/src/divand.py/src:$PYTHONPATH" python divand_argo.py
```

Note that you should adapt the path in the previous example to match the installation location of `divand.py`.


## Toubleshooting


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

<!--  LocalWords:  divand py variational PyCall pyjulia cd argo LD
 -->
<!--  LocalWords:  PYTHONPATH PRELOAD runtime
 -->
