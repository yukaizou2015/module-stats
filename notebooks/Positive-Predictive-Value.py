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

# + [markdown] slideshow={"slide_type": "slide"}
# # The positive predictive value
# -

# ## Let's see this notebook in a better format :
# ### [HERE](http://www.reproducibleimaging.org/module-stats/05-PPV/)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Some Definitions 

# + [markdown] slideshow={"slide_type": "subslide"}
# * $H_0$ : null hypothesis: The hypotheis that the effect we are testing for is null
#
# * $H_A$ : alternative hypothesis : Not $H_0$, so there is some signal
#
# * $T$ : The random variable that takes value "significant" or "not significant"
#
# * $T_S$ : Value of T when test is significant (eg $T = T_S$) - or, the event "the test is significant"
#
# * $T_N$ : Value of T when test is not significant (eg $T = T_N$) or, the event "the test is not significant"
#
# * $\alpha$ : false positive rate - probability to reject $H_0$ when $H_0$ is true ($H_A$ is false)
#
# * $\beta$ : false negative rate - probability to accept $H_0$ when $H_A$ is true ($H_0$ is false)
#

# + [markdown] slideshow={"slide_type": "subslide"}
# power = $1-\beta$ 
#
# where $\beta$ is the risk of *false negative*
#
# So, to compute power, *we need to know what is the risk of false negative*, ie, the risk to not show a significant effect while we have some signal (null is false).
# -

# ## Some standard python imports

# + slideshow={"slide_type": "skip"}
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import scipy.stats as sst
import matplotlib.pyplot as plt
from __future__ import division #python 2.x legacy
# -

# ## A function to plot nicely some tables of probability

# + slideshow={"slide_type": "skip"}
from sympy import symbols, Eq, solve, simplify, lambdify, init_printing, latex
init_printing(use_latex=True, order='old')
from sympy.abc import alpha, beta # get alpha, beta symbolic variables
from IPython.display import HTML
# Code to make HTML for a probability table
def association_table(assocs, title):
    latexed = {'title': title}
    for key, value in assocs.items():
        latexed[key] = latex(value)
    latexed['s_total'] = latex(assocs['t_s'] + assocs['f_s'])
    latexed['ns_total'] = latex(assocs['t_ns'] + assocs['f_ns'])
    return """<h3>{title}</h3>
              <TABLE><TR><TH>$H/T$<TH>$T_S$<TH>$T_N$
              <TR><TH>$H_A$<TD>${t_s}$<TD>${t_ns}$
              <TR><TH>$H_0$<TD>${f_s}$<TD>${f_ns}$
              <TR><TH>Total<TD>${s_total}$<TD>${ns_total}$
              </TABLE>""".format(**latexed)
assoc = dict(t_s = 1 - beta, # H_A true, test significant = true positives
             t_ns = beta, # true, not significant = false negatives
             f_s = alpha, # false, significant = false positives
             f_ns = 1 - alpha) # false, not sigificant = true negatives
HTML(association_table(assoc, 'Not considering prior'))

# + slideshow={"slide_type": "skip"}


# + [markdown] slideshow={"slide_type": "slide"}
# ## Derivation of Ionannidis / Button positive prediction value : PPV

# + [markdown] slideshow={"slide_type": "slide"}
# ### Recall some important statistic concepts: Marginalization and Baye theorem

# + [markdown] slideshow={"slide_type": "slide"}
# #### Marginalization
# -

# $\newcommand{Frac}[2]{\frac{\displaystyle #1}{\displaystyle #2}}$
#
# We now consider that the hypotheses are *random events*, so we have a probability associated to these events. 
#
# Let's define some new terms:
#
# * $P(H_A)$ - prior probability of $H_A$ - probability of $H_A$ before the experiment.
# * $P(H_0)$ - prior probability of $H_0$ = $1 - Pr(H_A)$ - probability of null hypothesis before the experiment
#
# We are interested in updating the probability of $H_A$ and $H_0$ as a result of a test on some collected data.  
# This updated probability is $P(H_A | T)$ - the probability of $H_A$ given the test  result $T$. $P(H_A | T)$ is called the *posterior* probability because it is the probability after the test result is known.
#
# Lets imagine that the event A occurs under the events b1, b2, .., bn, these events bi are mutually exclusive and they represent all possibilities. For instance, the event "the test is significant" occurs under "H0" and "H1". 
# The marginalization theorem is simply that 
#
# $$ P(A) = \sum_{b_i} P(A,B=b_i) $$
#
# In our previous example, 
#
# $$ P(T_S) = \sum_{h=H_0, H_1} P(T_S, h) = P(T_S, H_0) + P(T_S, H_1) $$
#
#
# Throughout $P(A, B)$ reads "Probability of A AND B". To simplify the notation, we note $P(B=b)$ as $P(b)$

# #### Baye theorem

# + [markdown] slideshow={"slide_type": "fragment"}
# Remembering [Bayes theorem](http://en.wikipedia.org/wiki/Bayes'_theorem#Derivation):
#
# $$P(A, B) = P(A | B) P(B)$$
#
# and therefore
#
# $$P(A | B) = \Frac{P(B, A)}{P(B)} = \Frac{P(B | A) P(A)}{P(B)}$$
#
# Putting marginalization and Bayes together we have : 
#
# $$P(A) = \sum_{b_i} P(A|B=b_i) P(B=b_i)$$
#
# Now, apply this to the probability of the test results $T$. The test takes a value either under  $H_A$ or $H_0$.
# The probability of a *signficant* result of the test $T=T_S$ is :
#
# $Pr(T=T_S) = P(T_S) = Pr(T_S | H_A) Pr(H_A) + Pr(T_S | H_0) Pr(H_0)$

# + [markdown] slideshow={"slide_type": "fragment"}
#
# What is the posterior probability of $H_A$ given that the test is significant?
#
# $P(H_A | T_S) = \Frac{P(T_S | H_A) P(H_A)}{P(T_S)} = \Frac{P(T_S | H_A) P(H_A)}{P(T_S | H_A) Pr(H_A) + Pr(T_S | H_0) Pr(H_0)}$
#
# We have $P(T_S | H_A)$, $P(T_S | H_0)$ from the first column of the table above. Substituting into the equation:
#
# $P(H_A | T_S) = \Frac{(1 - \beta) P(H_A)}{(1 - \beta) P(H_A) + \alpha P(H_0)}$

# + [markdown] slideshow={"slide_type": "slide"}
# Defining:
#
# $\pi := Pr(H_A)$, hence: $1 - \pi = Pr(H_0)$
#
# we have:
#
# $P(H_A | T_S) = \Frac{(1 - \beta) \pi}{(1 - \beta) \pi + \alpha (1 - \pi)}$
#

# + slideshow={"slide_type": "fragment"}
from sympy.abc import pi # get symbolic variable pi
post_prob = (1 - beta) * pi / ((1 - beta) * pi + alpha * (1 - pi))
post_prob

# + slideshow={"slide_type": "fragment"}
assoc = dict(t_s = pi * (1 - beta),
             t_ns = pi * beta,
             f_s = (1 - pi) * alpha,
             f_ns = (1 - pi) * (1 - alpha))
HTML(association_table(assoc, r'Considering prior $\pi := P(H_A)$'))


# + [markdown] slideshow={"slide_type": "slide"}
# ## Retrieving the Ioannidis / Button et al formula

# + [markdown] slideshow={"slide_type": "fragment"}
# Same as Ioannidis - do the derivation starting with odd ratios 
#
# From Button et al., we have the positive predictive value PPV defined as :
#
# $$
# PPV = \frac{(1-\beta)R}{(1-\beta)R + \alpha},\textrm{ with } R = P(H_1)/P(H_0) = P_1/P_0 = \pi / (1-\pi)
# $$
#
# Hence, 
#
# $$
# PPV = \frac{(1-\beta)P_1}{P_0}\frac{P_0}{(1-\beta)P_1 + \alpha P_0} 
# $$
#
# $$
# = \frac{(1-\beta)P_1}{(1-\beta)P_1 + \alpha P_0} 
# $$
#
# $$
# = P(H_1, T_S) / P(T_S) = P(H_1 | T_S) 
# $$

# + [markdown] slideshow={"slide_type": "fragment"}
# If we have 4 chances over 5 that $H_0$ is true, and one over five that $H_1$ true, then R = 1/5 / 4/5 = .25. If there's 30% power we have PPV = 50%. So, 50% chance that our result is indeed true. 80% power leads to 80% chance of $H_1$ to be true, knowing that we have detected an effect at the $\alpha$ risk of error. 
# -

# ### A small function to compute PPV

# + slideshow={"slide_type": "slide"}
def PPV_OR(odd_ratio, power, alpha, verbose=True):
    """
    returns PPV from odd_ratio, power and alpha
    
    parameters:
    -----------
    odd_ratio: float
        P(H_A)/(1-P(H_A))
    power: float
        Power for this study
    alpha: float
        type I risk of error
        
    Returns:
    ----------
    float
        The positive predicted value
    
    """
    
    ppv = (power*odd_ratio)/(power*odd_ratio + alpha)
    if verbose:
        print("With odd ratio=%3.2f, "
               "Power=%3.2f, alpha=%3.2f, "
               "We have PPV=%3.2f" %(odd_ratio,power,alpha,ppv))
    return ppv
    


# -

one4sure = PPV_OR(1, 1, 0, verbose=False)
assert one4sure == 1
zero4sure = PPV_OR(0, 1, 0.05, verbose=False)
assert zero4sure == 0
weird2think = PPV_OR(1, 1, 1, verbose=False)
assert weird2think == 0.5


# ### A small function for display

def plot_ppv(xvalues, yvalues, xlabel, ylabel, title):
    '''
    simply plot yvalues against xvalues, with labels and title
    
    Parameters:
    -----------
    xvalues, yvalues : iterables of numbers 
    labels and title : string
    '''
    
    fig = plt.figure();
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(xvalues, yvalues, color='red', marker='o', linestyle='dashed',
            linewidth=2, markersize=14);
    axis.set_xlabel(xlabel,fontsize=20);
    axis.set_ylabel(ylabel,fontsize=20);
    axis.set_title(figure_title, fontsize=20);
    return fig, axis


# ### Example from Button et al, 2013

# + slideshow={"slide_type": "fragment"}
# example from Button et al: P1 = 1/5, P0 = 4/5. R = 1/4
R = 1./5.
Pw = .4
alph = .05
ppv = PPV_OR(R, Pw, alph)
# -

# ### Vary power

# + slideshow={"slide_type": "fragment"}
#-----------------------------------------------------------------
# Vary power:
R = .2
Pw = np.arange(.1,.80001,.1)
alph = .20
ppvs = [PPV_OR(R, pw, alph, verbose = False) for pw in Pw]
xlabel = 'Power'
ylabel = 'PPV'
figure_title = 'With an odd ratio H1/H0 = {odd_ratio}'.format(odd_ratio=R)

#-----------------------------------------------------------------
# print
plot_ppv(Pw, ppvs, xlabel, ylabel, figure_title);

# -

# ### Vary odd ratio

# +
#-----------------------------------------------------------------
# Vary odd ratio:
Pw = .4
alph = .05
odd_ratios = np.arange(.05,.5,.05)
ppvs = [PPV_OR(R, Pw, alph, verbose = False) for R in odd_ratios]
xlabel = 'odd_ratios'
ylabel = 'PPV'
figure_title = 'With a power of {power}'.format(power=Pw)

#-----------------------------------------------------------------
# print
plot_ppv(odd_ratios, ppvs, xlabel, ylabel, figure_title);

# -

# ### Vary alpha

# +
#-----------------------------------------------------------------
# Vary alpha:
Pw = .5
R = 1/5
alphas = np.arange(0, .2, 0.01)# [0.001, .005, 0.01, 0.05, 0.1] #, 0.2, 0.3, 0.4, 0.5]
ppvs = [PPV_OR(R, Pw, alph, verbose = False) for alph in alphas]

#-----------------------------------------------------------------
# print
xlabel = 'alpha'
ylabel = 'PPV'
figure_title = 'With a power of {power} and odd ratio of {odd_ratio}'.format(
                                        power=Pw, odd_ratio=R)
plot_ppv(alphas, ppvs, xlabel, ylabel, figure_title);

# -

# # End of the PPV section




