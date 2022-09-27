import pandas as pd
import numpy as np

# mylist = list('abcedfghijklmnopqrstuvwxyz')
# myarr = np.arange(26)
# mydict = dict(zip(mylist, myarr))
# ser = pd.Series(mydict)
# ser1 = ser.to_frame()

# df = ser.to_frame().reset_index()
# print(df.tail())


#2
# ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
# ser2 = pd.Series(np.arange(26))
# mydict = dict(zip(ser1, ser2))
# ser = pd.Series(mydict)


# print(ser.head())

#3 
# ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
# ser.name = "Alphabet"

# print(ser.head())

#4

# ser1 = pd.Series([1, 2, 3, 4, 5])
# ser2 = pd.Series([4, 5, 6, 7, 8])

# ser = ser1[~ser1.isin(ser2)] #Muestra ser 1 reemplazando los valores iguales


# print(ser)

#5
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ser_u = pd.Series(np.union1d(ser1, ser2))  # union
ser_i = pd.Series(np.intersect1d(ser1, ser2))  # intersect
ser_u[~ser_u.isin(ser_i)]