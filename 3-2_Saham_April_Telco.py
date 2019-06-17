import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = 'darkgrid')

xl = pd.read_csv('DataSaham/EXCL.JK.csv', parse_dates = ['Date'])
xl_april = xl[(xl['Date'] > '2019-03-29') & (xl['Date'] < '2019-05-01')]

smartfren = pd.read_csv('DataSaham/FREN.JK.csv', parse_dates = ['Date'])
smartfren_april = smartfren[(smartfren['Date'] > '2019-03-29') & (smartfren['Date'] < '2019-05-01')]

indosat = pd.read_csv('DataSaham/ISAT.JK.csv', parse_dates = ['Date'])
indosat_april = indosat[(indosat['Date'] > '2019-03-29') & (indosat['Date'] < '2019-05-01')]

telkom = pd.read_csv('DataSaham/TLKM.JK.csv', parse_dates = ['Date'])
telkom_april = telkom[(xl['Date'] > '2019-03-29') & (telkom['Date'] < '2019-05-01')]

plt.figure('Harga Historis Saham Provider Telco Indonesia (April 2019)', figsize = (10,6))
plt.plot(xl_april['Date'], xl_april['Close'], color = 'green', label = 'PT XL Axiata Tbk')
plt.plot(smartfren_april['Date'], smartfren_april['Close'], color = 'cyan', label = 'PT Smartfren Telecom Tbk')
plt.plot(indosat_april['Date'], indosat_april['Close'], color = 'blue', label = 'PT Indosat Tbk')
plt.plot(telkom_april['Date'], telkom_april['Close'], color = 'red', label = 'PT Telekomunikasi Indonesia Tbk')

plt.suptitle('Historical Value Saham Provider Telco Indonesia (April 2019)')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.xticks(rotation = 50)

label = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(label, loc = 'upper center', bbox_to_anchor = (0.5, 1.075), ncol = 4, frameon = False)


plt.show()