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

* $$\alpha$$ : false positive rate - probability to reject $$H_0$$ when $$H_0$$ is true ($$H_A$$ is false)

* $$\beta$$ : false negative rate - probability to accept $$H_0$$ when $$H_A$$ is true ($$H_0$$ is false)

* power = $$1-\beta$$ 

## PPV : definition and some exercices 

### Marginalization

Let's consider that the hypotheses are *random events*, i.e. they have associate probabilities. For instance, the probability of $$H_0$$ to be true could be 50%. $$Pr(H_A = True) + Pr(H_0 = False) = 1$$.

We simply note 

$$Pr(H_A = True)$$ as $$Pr(H_A)$$  

for 
$$H \in (H_A, H_0)$$ 


We are interested in updating the probability of $$H_A$$ and $$H_0$$ as a result of a test on some collected data.  

This updated probability is $$Pr(H_A \mid T=t), t \in (T_S, T_N)$$,  

the probability of $$H_A$$ **given** the result $$t$$ of the test.

$$Pr(H_A \mid T)$$ is called the *posterior* probability because it is the probability after the test result.

The marginalization theorem is simply that 

 $$P(A) = \sum_{b_i} P(A,B = b_i) $$

Here:

 $$P(H) = P(H, T=T_S) + P(H, T=T_N)$$

 $$ = \sum_{t = T_S, T_N} P(H, T=t) $$


In the future, to simplify the notation, we note $$P(B=b)$$ as $$P(b)$$

## Bayes theorem

[Bayes theorem](http://en.wikipedia.org/wiki/Bayes'_theorem#Derivation):

$$P(A, B) = P(A \mid B) P(B)$$

and therefore

$$P(A \mid B) = \Frac{P(B, A)}{P(B)} = \frac{P(B \mid A) P(A)}{P(B)}$$


Putting these two together we have : 


$$P(A) = \sum_{b_i} P(A \mid B=b_i) P(B=b_i)$$

Now, apply this to the probability of the test results $T$. The test takes a value either under  $H_A$ or $H_0$.
The probability of a *signficant* result of the test $T=T_S$ is :

$Pr(T=T_S) = P(T_S) = Pr(T_S \mid H_A) Pr(H_A) + Pr(T_S \mid H_0) Pr(H_0)$

## Some work on this notebook in python

First, we will be doing some work on this notebook:

[Power](https://github.com/ReproNim/module-stats/blob/gh-pages/notebooks/Positive-Predictive-Value.ipynb)

## Some exercises  

> Exercise: 
>        Pick a recent study that you have done in fMRI or using anatomical data.  
>        try to propose values for power, alpha, and prior
>        Vary prior and plot results 


## How to work with the notebooks ? 

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

