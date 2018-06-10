---
title: "The positive Predictive Value"
teaching: 10 
exercises: 20 
questions: 
- "What is the positive Predictive Value (PPV) ?"
objectives:
- "After this lesson, you should understand what is the PPV"
keypoints:
- A significant (say at the 0.05 level) may have a low chance of replication. 
- The PPV estimates the probability that the alternative hypothesis $$H_1$$ is true given that the test is significant at some $$\alpha$$ level.
- This probability depends on several factors such as power $$\beta$$, $$\alpha$$ level, but also the **prior chance** that $$H_1$$ is true.
---

## Definitions: remiders

* $$H_0$$ : null hypothesis: The hypotheis that the effect we are testing for is null

* $$H_A$$ : alternative hypothesis : Not $$H_0$$, so there is some signal

* $$T$$ : The random variable that takes value "significant" or "not significant"

* $$T_S$$ : Value of T when test is significant (eg $$T = T_S$$)

* $$T_N$$ : Value of T when test is not significant (eg $$T = T_N$$)

* $$\alpha$$ : false positive rate - probability to reject $$H_0$$ when $$H_0$$ is true ($$H_A$$ is false) $$ = P(T_S \mid H_0) $$ 

* $$\beta$$ : false negative rate - probability to accept $$H_0$$ when $$H_A$$ is true ($$H_0$$ is false) $$ = P(T_N \mid H_A) $$

* power = $$1-\beta$$ 

## PPV : definition and some exercices 

### Marginalization

Let's consider that the hypotheses are *random events*, i.e. they have associate probabilities. For instance, the probability of $$H_0$$ to be true could be 50%. $$P(H_A = True) + P(H_0 = False) = 1$$.

We simply note 

$$P(H_A = True)$$ as $$P(H_A)$$  

for 
$$H \in (H_A, H_0)$$ 


We are interested in updating the probability of $$H_A$$ and $$H_0$$ as a result of a test on some collected data.  

This updated probability is $$P(H_A \mid T=t), t \in (T_S, T_N)$$,  

the probability of $$H_A$$ **given** the result $$t$$ of the test.

$$P(H_A \mid T)$$ is called the *posterior* probability because it is the probability after the test result.

The marginalization theorem is simply that 

 $$P(A) = \sum_{b_i} P(A,B = b_i) $$

Here:

 $$P(H) = P(H, T=T_S) + P(H, T=T_N)$$

 $$ = \sum_{t = T_S, T_N} P(H, T=t) $$


In the future, to simplify the notation, we note $$P(B=b)$$ as $$P(b)$$


## Bayes theorem

The famous theorem [Bayes theorem](http://en.wikipedia.org/wiki/Bayes'_theorem#Derivation):

$$P(A, B) = P(A \mid B) P(B)$$

and therefore

$$P(A \mid B) = \frac{P(B, A)}{P(B)} = \frac{P(B \mid A) P(A)}{P(B)}$$

Putting these two together we have : 

$$P(A) = \sum_{b_i} P(A \mid B=b_i) P(B=b_i)$$

## Apply this to our question:

Now, apply this to the probability of the test results $$T$$. 

The test takes a value either under  $$H_A$$ or $$H_0$$.

The probability of a *significant* result of the test $$T=T_S$$ is :

$$ P(T_S) = P(T_S \mid H_A) P(H_A) + P(T_S \mid H_0) P(H_0)$$


What is the posterior probability of $$H_A$$ given that the test is significant?

$$P(H_A \mid T_S) = \frac{P(T_S \mid H_A) P(H_A)}{P(T_S)} = \frac{P(T_S \mid H_A) P(H_A)}{P(T_S \mid H_A) Pr(H_A) + Pr(T_S \mid H_0) Pr(H_0)}$$

We have $$P(T_S \mid H_A)$$, $$P(T_S \mid H_0)$$ from the first column of the table above. Substituting into the equation.

And we know that 

$$ P(T_S \mid H_A) = 1 - P(T_N \mid H_A) = 1 - \beta $$

Substituting:

$$ P(H_A \mid T_S) = \frac{(1 - \beta) P(H_A)}{(1 - \beta) P(H_A) + \alpha P(H_0)} $$

Defining:

$$ \pi := Pr(H_A)$$, hence: $$1 - \pi = Pr(H_0) $$

we have:

$$ P(H_A \mid T_S) = \frac{(1 - \beta) \pi}{(1 - \beta) \pi + \alpha (1 - \pi)} $$

Defining  $$ R = \frac{\pi}{1-\pi} $$  the odd ratio of the alternative over the null and $$ W = 1 - \beta $$ as power we get

$$ P(H_A \mid T_S) = \frac{W R}{W R  + \alpha} $$

## Some exercises  


> ## Task: Play with the PPV - understand the impact of the parameters 
>
>  
>     Pick a recent study that you have done in fMRI or using anatomical data.  
>     try to propose values for power, alpha, and prior
>     Vary power from .1 to .9 and print or plot results
> 
>     First define a function to compute the PPV from power, odd ratio and alpha
>     The solution below is in Python, but feel free to do it in your favorite scripting language
>
> > ## Solution
> > ~~~
> > 
> > def PPV_OR(odd_ratio, power, alpha, verbose=True):
> >     """
> >     returns PPV from odd_ratio, power and alpha
> >     
> >     parameters:
> >     -----------
> >     odd_ratio: float
> >         P(H_A)/(1-P(H_A))
> >     power: float
> >         Power for this study
> >     alpha: float
> >         type I risk of error
> >         
> >     Returns:
> >     ----------
> >     float
> >         The positive predicted value
> >     
> >     """
> >     
> >     ppv = (power*odd_ratio)/(power*odd_ratio + alph)
> >     if verbose:
> >         print("With odd ratio=%3.2f, "
> >                "Power=%3.2f, alpha=%3.2f, "
> >                "We have PPV=%3.2f" %(odd_ratio,power,alph,ppv))
> >     return ppv
> > ~~~
> > {: .python}
> {: .solution}
>  
>     Second define a function to display easily the results 
> 
> > ## Solution
> > ~~~
> > def plot_ppv(xvalues, yvalues, xlabel, ylabel, title):
> >    '''
> >    simply plot yvalues against xvalues, with labels and title
> >    
> >    Parameters:
> >    -----------
> >    xvalues, yvalues : iterables of numbers 
> >    labels and title : string
> >    '''
> >    
> >    fig = plt.figure();
> >    axis = fig.add_subplot(1, 1, 1)
> >    axis.plot(xvalues, yvalues, color='red', marker='o', linestyle='dashed',
> >            linewidth=2, markersize=14);
> >    axis.set_xlabel(xlabel,fontsize=20);
> >    axis.set_ylabel(ylabel,fontsize=20);
> >    axis.set_title(figure_title, fontsize=20);
> >    return fig, axis
> > ~~~
> > {: .python}
> {: .solution}
>
>     Last play with parameters : first, let's vary power
> 
> > ## Solution
> > ~~~
> >
> > #-----------------------------------------------------------------
> > # An example
> > R = 1./5.
> > Pw = .5
> > alph = .05
> > ppv = PPV_OR(R, Pw, alph)
> > 
> > #-----------------------------------------------------------------
> > # Vary power:
> > Pw = np.arange(.1,1,.2)
> > ppvs = [PPV_OR(R, pw, alph, verbose = False) for pw in Pw]
> > xlabel = 'Power'
> > ylabel = 'PPV'
> > figure_title = 'With an odd ratio of {odd_ratio}'.format(odd_ratio=R)
> > 
> > #-----------------------------------------------------------------
> > # print
> > plot_ppv(Pw, ppvs, xlabel, ylabel, figure_title);
> > ~~~
> > {: .python}
> {: .solution}
>
>     Then, let's vary odd ratio 
> 
> > ## Solution
> > ~~~
> > #-----------------------------------------------------------------
> > # Vary odd ratio:
> > Pw = .5
> > alph = .05
> > odd_ratios = np.arange(.05,.5,.05)
> > ppvs = [PPV_OR(R, Pw, alph, verbose = False) for R in odd_ratios]
> > 
> > #-----------------------------------------------------------------
> > # print
> > figure_title = 'With a power of {power}'.format(power=Pw)
> > xlabel = 'odd_ratios'
> > ylabel = 'PPV'
> > plot_ppv(odd_ratios, ppvs, xlabel, ylabel, figure_title);
> > 
> > ~~~
> > {: .python}
> {: .solution}
>
>     Last, let's vary alpha, remember that p-hacking may give us large type I risk of errors 
> 
> > ## Solution
> > ~~~
> > 
> > #-----------------------------------------------------------------
> > # Vary alpha:
> > Pw = .5
> > R = 1/5
> > alphas = np.arange(0, .2, 0.01)# [0.001, .005, 0.01, 0.05, 0.1] #, 0.2, 0.3, 0.4, 0.5]
> > ppvs = [PPV_OR(R, Pw, alph, verbose = False) for alph in alphas]
> > 
> > #-----------------------------------------------------------------
> > # print
> > xlabel = 'alpha'
> > ylabel = 'PPV'
> > figure_title = 'With a power of {power} and odd ratio of {odd_ratio}'.format(
> >                                         power=Pw, odd_ratio=R)
> > plot_ppv(alphas, ppvs, xlabel, ylabel, figure_title);
> > #-----------------------------------------------------------------
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

## This is also in a python notebook 

The notebook is : 
[PPV](https://github.com/ReproNim/module-stats/blob/gh-pages/notebooks/Positive-Predictive-Value.ipynb)


### How to work with the notebooks ? 

There are two cases.

1. You do not really know python, and how to install the jupyter notebook. You
   can still read the notebook, skipping the code sections. The notebook will
introduce some definitions, and then play with different settings. But the true
benefit comes if you can install the jupyter project [see
here](http://jupyter.readthedocs.io/en/latest/install.html) and actually play
with the code, for instance changing the sample size or effect size to
understand better what power is.

2. Download the notebook, and try to understand the concepts and the code. If
   the code is unclear, please make an issue on the repronim [github
site](https://github.com/ReproNim/module-stats/tree/gh-pages/notebooks)

