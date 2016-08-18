# Debugging

1. [Getting started with python debugger](https://pythonconquerstheuniverse.wordpress.com/category/python-debugger/)

## Timing code

You can time code in ipython using the [`%time`](https://ipython.org/ipython-doc/3/interactive/magics.html#magic-time) and [`%timeit`](https://ipython.org/ipython-doc/3/interactive/magics.html#magic-timeit) magics. You can also time sections of code using system clock, for example

```python
import numpy as np
import time

init_time = time.clock()  # start clock
x = np.linspace(0,100,1000000)
y = np.sqrt(x)

elap_time = time.clock() - init_time  # finds difference

print "Time elapsed is %0.3f ms" % (elap_time*1000)  # converts to ms
```
