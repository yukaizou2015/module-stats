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

## P-value

Again, [wikipedia](https://en.wikipedia.org/wiki/P-value) is a great resource. You can also read the short blog from [realClearScience](http://www.realclearscience.com/blog/2016/11/07/httpwwwrealclearsciencecomblog20161107httpwwwrealclearsciencecomblog20161102httpwwwrealclearsciencecomblog201610the_biggest_myth_about_the_p-value.html) to make sure you have the main idea right. 


## Multiple Comparison problem:

[Multiple Comparisons](https://en.wikipedia.org/wiki/Multiple_comparisons_problem#Classification_of_multiple_hypothesis_tests)

## p-value and base rate fallacy:

1. This blog concerns number of drugs tested, but could easily generalize to number of voxels or ROIs tested. It introduces to very important concepts, read carefully and make sure you understand what is the base rate fallacy.  After reading, you should know of Type I and Type II errors. 

[p-values](http://www.statisticsdonewrong.com/p-value.html)

The blogs includes the famous XKCD cartoon on [multiple testing](http://xkcd.com/882/)


## Understanding statistical power and significance testing:

- interactive visualization for NHST:
[NHST](http://rpsychologist.com/d3/NHST/)

- Confidence intervals:
[Confidence intervals:](http://rpsychologist.com/d3/CI/)



## Distributions 

Please make sure you understand what is a distribution. some links on distributions and CDFs. 

[Definition of distributions](https://en.wikipedia.org/wiki/Probability_distribution)

There is also this link that will tell you about statistical distributions: 

[this link](http://mathworld.wolfram.com/StatisticalDistribution.html)


We need to be able to use the [Cumulative Density function](https://en.wikipedia.org/wiki/Cumulative_distribution_function) : CDF and its Complementary cumulative distribution function (also called tail distribution, or survival function :  $$ SF(x) =  1 - CDF(x) $$. 

The cumulative density function of a random variable X is often noted $F_X$ or simply $F$ when there is no ambiguity. 

An interesting fact is that p-values, which are random variable because they are just a function of the data, and the data are random (since you got these specific data by sampling eg subjects, right ?).

So, say you sample from a normal N(0,1) distribution, what is the distribution of a p-value for a test T (for instance the test T is simply a z-score for a sample of N(0,1) variables. 

Let's take T as your random variable. Note, the definition of a [random variable](https://en.wikipedia.org/wiki/Random_variable) is not straightforward, but roughly speaking it is a function that "maps from an outcome of the events (that is, from a point in a probability space) to a mathematically convenient outcome label, usually a real number." 

Let's $$ P = F(T) $$ Where $$ F $$ is the CDF of $$ T $$ i.e. $$ F(t) \equiv F_T(t) \equiv Pr(T <= t) $$. 

$$ Pr(P < p) = Pr(F(T) < p) $$

If F is invertible, and for continuous random variable with strictly monotonic cumulative density function this is the case, we have 

$$ F(T) <= p \equiv F{-1}F(T) <= F^{-1}(p) $$

hence, 

$$ Pr(P < p) = Pr(T < F^{-1}(p)) \equiv F(F^{-1}(p)) = p $$

So, 

$$ Pr( P <= p) = F_p(p) = p $$

Therefore, the CDF of $$P$$ is the identity function $$ CDF(x)=x $$. The probability function is simply the derivative of the CDF (when this derivative exists) here $$ PDF(x) = f(x) = 1 $$.  This is a uniform variable !_


## Notion of model comparison : BIC/Akaike

Model comparison is **fundamental**. 

## Notion of bayesian statistics  

Bayesian statistics are *rarely* used, because researchers don't really know how. But, in 
fact, they  most likely have a better theoretical ground and should be used in practice. 

The problems are :
	- the inertia of the community to adopt better frameworks
	- the reason for this inertia is that reviewers would need some training 
	- the training is not provided

 

