from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from scipy import stats

# plt.rcParams["font.family"] = "Times New Roman"
# plt.rcParams["mathtext.fontset"]

#==============================================Get data========================================================================
data = ascii.read('data/table2.dat', readme='data/ReadMe')


#===============================================plot data and save============================================================

#define aux comprehension list for special markers and color criteria
colors = ['k' if Type == 'BL' else 'b' if Type == 'NL' else 'r' for Type in data['Type']]
markers = ['+' if Type == 'BL' else 'D' if Type == 'NL' else 's' for Type in data['Type']]

fig, ax = plt.subplots()
ax.set_title('Accretion luminosity vs black hole mass log-log plot\n(logL vs logM) for the AGNs sample', fontweight = 'bold'), 
ax.set_xlabel(r'$log(M_{BH}[M_{\odot}])$', fontsize = 11)
ax.set_ylabel(r'$\log(L)[erg/s]$', fontsize = 11)
ax.tick_params(axis='both', which='major', labelsize=11)

xlow, ylow = np.array(data['e_logM']), np.array(data['e_logL'])
xup, yup  = np.array(data['E_logM']), np.array(data['E_logL'])
xerror, yerror = [xlow, xup], [ylow, yup]

for x, y, c, m in zip(data['logM'], data['logL'], colors, markers):
     ax.scatter(x, y, ec = c, marker = m, s = 25, lw = 0.8, fc = 'none')

ax.yaxis.set_minor_locator(AutoMinorLocator(10))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.errorbar(data['logM'], data['logL'], xerr = xerror, yerr = yerror, fmt = ' ', ecolor = 'darkslategray', elinewidth = 0.5, alpha = 0.6, capsize = 0)

plt.savefig('figures/log-log.png', dpi = 200)
plt.savefig('figures/log-log.pdf')

#==================================================statistical analysis========================================================

#get sample
sample = data[(data['Type'] == 'BL')]
#print(sample)

#analysis
mean = np.mean(sample['logM'])
var = np.var(sample['logM'])
std = np.std(sample['logM'])
skew = stats.skew(sample['logM'])
kurt = stats.kurtosis(sample['logM'])

# print(f'Arimethic mean: {mean:.4f}')
# print(f'Variance: {var:.4f}')
# print(f'Standard deviation: {std:.4f}')
# print(f'Skewness: {skew:.4f}')
# print(f'Kurtosis: {kurt:.4f}')

#histogram------------------------------------------------------------------------------------------------------------------------------------
fig1, ax1 = plt.subplots()
ax1.set_title(f'logM histogram of BL AGNs with 20 bins ({len(sample)} samples).\n$\mu = {mean:.4f}$, $std = {std:.4f}$, $skewnewss = {skew:.4f}$, $kurtosis = {kurt:.4f}$', fontweight = 'bold')
ax1.set_xlabel('$logM_{BH}[M_{\odot}]$', fontsize = 11)
ax1.set_ylabel('counts', fontsize = 11)
ax1.tick_params(axis='both', which='major', labelsize=11)
ax1.hist(data['logM'], bins = 20, fc = '#ffbf00', ec = 'k', lw = 0.6, alpha = 0.8)
ax1.grid(ls = (0,(1,4)), c = 'k', alpha = 0.7)

plt.savefig('figures/hist.png', dpi = 200)
plt.savefig('figures/hist.pdf')
plt.show()