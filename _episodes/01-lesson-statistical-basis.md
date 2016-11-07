---
title: "Statistical basis for neuroimaging analyses: the basics"
teaching: 60 
exercises: 120 
questions: 
- "Sampling, notion of estimation : estimates of mean and variances"
- "Distributions, relation to frequency, PDF, CDF, SF, ISF "
- "Hypothesis testing: the basics H0 versus H1"
- "Confidence intervals "
- "Notion of model comparison : BIC/Akaike"
- "Notion of bayesian statistics " 
objectives:
- "After this lesson, you should have the statistical basis for 
understanding this course. You will know what is sampling, the 
fundamentals of statistical testing, etc.  "
keypoints:
- Some keypoints

- This is in line with our overall goal of making science (including scientific training) more open.

---


## Introduction: why do I need to know all this ? 


## Sampling

-sample vs population
-generalizability
-notion of sufficient sample

Please read these: 

[sampling-1](http://www.socialresearchmethods.net/kb/sampstat.php)
[sampling-2](http://www.socialresearchmethods.net/kb/external.php)

## Multiple Comparison problem:

[Multiple Comparisons](https://en.wikipedia.org/wiki/Multiple_comparisons_problem#Classification_of_multiple_hypothesis_tests)

## p-value and base rate fallacy:

1. This blog concerns number of drugs tested, but could easily generalize to number of voxels or ROIs tested.
Type I and Type II errors.

[p-values](http://www.statisticsdonewrong.com/p-value.html)

2. XKCD cartoon on multiple testing:
[xkcd](http://xkcd.com/882/)


## Understanding statistical power and significance testing:

- interactive visualization for NHST:
[NHST](http://rpsychologist.com/d3/NHST/)

- Confidence intervals:
[Confidence intervals:](http://rpsychologist.com/d3/CI/)








## Distributions 

Here some links on distributions and CDFs. 

[Definition of distributions](https://en.wikipedia.org/wiki/Probability_distribution)

There is also this link that will tell you about statistical distributions: 

[this link](http://mathworld.wolfram.com/StatisticalDistribution.html)






An interesting fact is that p-values, which are random variable because they are 
just a function of the data, and the data are random (since you got these specific
data by sampling some subjects, right ?)

So, say you sample from a normal (0,1) distribution, what is the distribution of a p-value ?

So, let's take Y your random variable. The definition of a [random variable](https://en.wikipedia.org/wiki/Random_variable) is not straightforward, but roughly speaking it is a function that "maps from an outcome of the events (that is, from a point in a probability space) to a mathematically convenient outcome label, usually a real number." 

Let's work with Y, a random variable with CDF : F(y) = P(Y <= y). Let's q = 1- p where p is the p-value, of the random variable Y to be less than y  

$$ q = 1-p = P(Y <= y) = F_Y(y)  $$

Let's find the cdf of $$ p $$ ...

inline $$ P ( p <= t) = P( F(y) <= t) ) $$

But F is a monotonic function, so we can say: 

$$
 P( F(y) < t) ) = P( F^{-1}F(y) < F^{-1}(t) )  
$$

but that is simply

$$  
	P( y < F^{-1}(t) )  
$$

which, by definition, is $$F(F^{-1}(t)) = t$$.

So, 
$$ 
	P( p < t) = F_{p-value}(t) =  t 
$$
This is a uniform variable !_


## Hypothesis testing: the basics: H0 versus H1

 
## confidence intervals

Confidence intervals are confusing. 

## Notion of model comparison : BIC/Akaike

Model comparison is **fundamental**. 


## Notion of bayesian statistics  

Bayesian statistics are *rarely* used, because researchers don't really know how. But, in 
fact, they  most likely have a better theoretical ground and should be used in practice. 

The problems are :
	- the inertia of the community to adopt better frameworks
	- the reason for this inertia is that reviewers would need some training 
	- the training is not provided

 



