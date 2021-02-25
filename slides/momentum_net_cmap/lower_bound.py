import numpy as np
import matplotlib.pyplot as plt

rc = {"pdf.fonttype": 42, 'text.usetex': True, 'font.size': 14,
      'xtick.labelsize': 12, 'ytick.labelsize': 12, 'text.latex.preview': True}

plt.rcParams.update(rc)


def f(eps, w):
    return np.exp(-.5 / eps) * (np.cos(w) + np.sinc(w) /eps)



eps_grid = np.logspace(-2, 2, 100)

w_grid = np.linspace(0, np.pi, 1000)

vals = [np.min(f(eps, w_grid)) for eps in eps_grid]

plt.figure(figsize=(3, 1.5))
plt.semilogx(eps_grid, vals)
x_ = plt.xlabel(r'$\varepsilon$')
y_ = plt.ylabel(r'$\alpha_{min}(\varepsilon)$')
plt.savefig('images/lower_bound.png', bbox_extra_artists=[x_, y_], bbox_inches='tight', dpi=400)
