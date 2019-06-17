import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = 'darkgrid')

xl = pd.read_csv('DataSaham/EXCL.JK.csv', parse_dates = ['Date'])
smartfren = pd.read_csv('DataSaham/FREN.JK.csv', parse_dates = ['Date'])
indosat = pd.read_csv('DataSaham/ISAT.JK.csv', parse_dates = ['Date'])
telkom = pd.read_csv('DataSaham/TLKM.JK.csv', parse_dates = ['Date'])

plt.figure('Historical Value Provider Telco Indonesia', figsize = (12,8))
plt.plot(xl['Date'], xl['Close'], color = 'green', label = 'PT XL Axiata Tbk')
plt.plot(smartfren['Date'], smartfren['Close'], color = 'cyan', label = 'PT Smartfren Telecom Tbk')
plt.plot(indosat['Date'], indosat['Close'], color = 'blue', label = 'PT Indosat Tbk')
plt.plot(telkom['Date'], telkom['Close'], color = 'red', label = 'PT Telekomunikasi Indonesia Tbk')

plt.suptitle('Harga Historis Saham Provider Telco Indonesia')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.xticks(rotation = 50)

label = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(label, loc = 'upper center', bbox_to_anchor = (0.5, 1.00), ncol = 4, frameon = False)

plt.show()