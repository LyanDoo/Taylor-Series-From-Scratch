import CalcTrig as ct
# import sys
import pandas as pd
import numpy as np

pd.set_option('display.float_format',lambda x: '%.5f' % x)
x_test = [-180,-150,-135,-120,-90,-60,-45,-30,0,30,45,60,90,120,135,150,180]
y_test = []

for i in x_test:
  y_test.append(ct.sine(i))

result = pd.DataFrame({'Sudut Istimewa':x_test,'Sin x':y_test})
print(result)