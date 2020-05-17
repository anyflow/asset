# ASSET

## www.quandl.com
api key : bJvt_r-GM7vxthXak2dE

## fix zipline JSONDecodeError

current : https://github.com/quantopian/zipline/issues/2480
alternative : https://duzi077.tistory.com/320

## For zipline

1. Use requirements_for_zipline.txt


## For backtrader

1. for tkinter issue : https://github.com/pyenv/pyenv/issues/1375
   1. PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I/usr/local/opt/tcl-tk/include' --with-tcltk-libs='-L/usr/local/opt/tcl-tk/lib -ltcl8.6 -ltk8.6'" pyenv install 3.7.7