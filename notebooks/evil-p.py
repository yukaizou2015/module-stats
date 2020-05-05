# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Compute a p-value - look at the effect size

# +
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import scipy.stats as sst

from IPython.display import Image as Image
from IPython.display import display as display

# -

# ## Create a normal distribution

np.random.seed(42) # 42 is arbitrary 

# define the normal 0,1 object
norm01 = sst.norm(0,1)
# Let's fix the seed of the random generator
sample_size = (30,)
sample = norm01.rvs(size=sample_size)


# +
# compute mean and corrected standard deviation
sample_mean = sample.mean()
#sample_std_biased = sample.std()
sample_std = np.sqrt(np.var(sample, ddof=1))
# print(sample_std,sample_std_biased)
N = len(sample)

print("sample mean: ",sample_mean, "sample_std: ", sample_std)
# -

# ## compute the t-value and corresponding p-value

t_value = sample_mean / (sample_std/np.sqrt(N))
print(t_value)


def t_value_from_sample(sample):
    """
    """
    N = len(sample)
    sample_mean = sample.mean()
    sample_std = np.sqrt(np.var(sample,ddof=1))
    t_val = sample_mean / (sample_std/np.sqrt(N))
    return t_val
    


print(t_value_from_sample(sample))

N = len(sample)
p_val = sst.t.sf(t_value_from_sample(sample), df=N-1)
print(p_val)

# ## Do this for a number of experiments

# +
sample_size = 16
distrib = sst.norm(.22, 1)
nb_of_experiments = 20
alpha = 0.05

effect_size = []

for idx in range(nb_of_experiments):
    sample =  distrib.rvs(size=(sample_size,))
    t_val = t_value_from_sample(sample)
    p_val = sst.t.sf(t_value_from_sample(sample), df=sample_size-1)
    signif = int(p_val <= alpha)
    print(t_val, "\t\t", p_val,"\t",  "*"*signif, )
    if signif:
        effect_size.append(sample.mean())

print('\n Effect_size corresponding to "significant" p-values: \n', effect_size) 
# -

print(np.asanyarray(effect_size).mean(), np.asanyarray(effect_size).std())

# ## Relate this to bias and file drawer effect

# # The p-hacking problem

img = Image('./figures/simons_table.png')
display(img)

# # Revise alpha 

# ### Recent and less recent attempts to change the standard alpha

print("Johnson, V.E. (2013). Revised standards for statistical evidence. " + 
                             "PNAS 110, 19313–19317.")
Image('./figures/johnson_PNAS_2013_significance.png')


# ### Make $\alpha$ adapted to the problem at hand

# This is going to be hard : cultural shift 

# ## Confidence intervals

# $$ P\left(\bigg|\frac{\bar{Y} - \mu}{\hat\sigma/\sqrt{n}}\bigg| \leq t_{0.025}\right) = 0.05 $$ 

# $$ P\left( -t_{0.025}\hat\sigma/\sqrt{n} + \bar{Y}  \leq \mu \leq t_{0.025}\hat\sigma/\sqrt{n} + \bar{Y}   \right) = 0.05 $$ 

def confidence_intervals(Nexp, CI = .95, **prmtrs):
    """
    Nexp: the number of experiments done
    CI: confidence interval
    
    prmtrs: a dictionary with our parameters, 
        example: prmtrs = {'n':16, 'mu':.3, 'sigma': 1., 'alpha': 0.05}
        
    returns arrays of size Nexp with:
    effect: the estimated effect
    detect: an array of 0 or 1, 1 when the effect is detected at alpha
    lCI: lower bound of confidence interval
    uCI: upper bound of confidence interval
    """
    # unpack parameters:
    n = prmtrs['n']
    mu = prmtrs['mu']; 
    alpha = prmtrs['alpha']; 
    sigma = prmtrs['sigma']
    df = n-1
    theta = mu*np.sqrt(n)/sigma
    
    # initialize arrays
    t = np.zeros((Nexp,))
    effect = np.zeros((Nexp,))
    lCI = np.zeros((Nexp,))
    uCI = np.zeros((Nexp,))

    # compute random variables and thresholds
    norv = sst.norm(0., sigma)
    strv = sst.t(df)
    # get the 0.05 t value *under the null* to construct confidence interval
    
    t_ci = strv.isf((1-CI)/2)
    # get the alpha level t value *under the null* to detect 
    t_alph = strv.isf(alpha)

    for experim in range(Nexp):
        # get n sample
        sample = norv.rvs(size=(n,)) + mu
        # effect and normalized effect size
        effect[experim] = sample.mean()
        std_error_data = np.std(sample, ddof=1) 
        std_error_mean = std_error_data/np.sqrt(n) # np.std takes ddof as 
                                                    # the df of freedom lost, here: 1.
        t[experim] = effect[experim]/std_error_mean
        # confidence interval :
        CI_ = t_ci*std_error_mean
        lCI[experim] = effect[experim] - CI_ # t_alph # 
        uCI[experim] = effect[experim] + CI_ # t_alph # 

    # number of detection:
    detect = t>t_alph
#    print 'number of detections:', xd.shape

    return (effect, detect, lCI, uCI, t)


# +
#---------------------- parameters ------------------#
prmtrs = {'n':30, 'mu': .30, 'sigma': 1., 'alpha': 0.05}

theta = prmtrs['mu']*np.sqrt(prmtrs['n'])/prmtrs['sigma']
print('Theta value %.3f \n' %theta)
#Pw = stat_power(prmtrs['n'], prmtrs['mu'], alpha=prmtrs['alpha'])


#--------------  simulate Nexp experiments ---------#
Nexp = 1000
effect, detect, lCI, uCI, t = confidence_intervals(Nexp, CI=.95, **prmtrs)
print('Average t {:.3f} \n'.format(t.mean()))


#print("Compare power {:.3} and rate of detection {:.3} ".format(Pw, detect.sum()/Nexp))

print("Mean effect {:.3f} compared to average detected effect {:.3f} \n".format(
                    effect.mean(), effect[detect].mean()))

print("-- # of exp. where lower bound > mu: {}".format((lCI[detect]>prmtrs['mu']).sum()))
print("-- # of exp. where upper bound < mu: {}".format((uCI[detect]<prmtrs['mu']).sum()))
not_in_CI = (uCI[detect]<prmtrs['mu']).sum() + (lCI[detect]>prmtrs['mu']).sum()
print("-- Not in CI = {:.3f}".format(not_in_CI))
print("-- over {} of detections".format(detect.sum()))
print("-- percentage = {:.3f}".format(not_in_CI/detect.sum()))


print("-------------- all experiment, not only detected")

print("-- # of exp. where lower bound > mu: {}".format((lCI>prmtrs['mu']).sum()))
print("-- # of exp. where upper bound < mu: {}".format((uCI<prmtrs['mu']).sum()))
print("-- over {} experiments".format(Nexp))
print("-- percentage = {:.3f}".format(
      ((lCI>prmtrs['mu']).sum() + (uCI<prmtrs['mu']).sum())/Nexp))

# +
#--------------  plot ------------------------------#
mu = prmtrs['mu']
x = np.arange(Nexp)
xd = np.arange(detect.sum())
mu_line = np.ones((Nexp,))*prmtrs['mu']

# print the number of lower confidence interval values that are above the true mean:
# this should be about the risk of error/2
print("lCI > mu :  {:.3}, compare with {:.3} ".format( 
                (lCI > mu).sum() / (1.*detect.sum()),  prmtrs['alpha'])) #
print(Nexp)
# there should be none of these:
# print "(lCI < 0 ", (lCI[detect] < 0).sum() / detect.sum()

f = plt.figure(1).set_size_inches(12,4)
lines = plt.plot(xd, lCI[detect], 'g-', 
                 xd, effect[detect], 'b--',
                 xd, uCI[detect], 'r-',
                 xd, mu_line[detect], 'k');
plt.legend( lines, ('lower_bound','detected Effect', 'Upper bound', 'True effect'), 
                   loc='upper right', shadow=True)
plt.xlabel(" One x is one experiment where detection occured", fontdict={'size':14})
plt.ylabel(" Effect value and confidence interval ", fontdict={'size':14})
plt.title(" Detected effects and their confidence interval", fontdict={'size':16});
# -

# ## What happens if ...

# ### Type I error is stricter 
#

# ### sample size goes down


