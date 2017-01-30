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

In our experience, you will not be able to think clearly about how "solid" the result you obtain without a sufficient background in statistics. Sometimes, you will think that this is taking you "too far". We truly do not think so, and if you bear with us long enough we hope that you will find this rewarding, and useful. 

## Sampling

In this unit, we would like you to fully understand the concept of a sample as a subset of a population.

It is critical that you master that concept, as it is at heart of most scientific studies. 
-sample vs population
-generalizability
-notion of sufficient sample

Please read the sections on this webpage: 
[Basics of sampling](http://www.socialresearchmethods.net/kb/sampling.php)

The key concepts are:

1. A sample is a subset of a population

2. The quality of the sample is related to the generalizability of the conclusions to the larger population of interest.

3. Most statistics are based on the assumption that, in the long run, statistics based on repeated samples from a population are distributed about the true (unobserved) population parameter.

### Exercise on sampling : [TBD]

## Statistics and random variables

Often, you will hear 


## P-value

"Informally, a p-value is the *probability* under a specified statistical model that a statistical summary of the data (e.g., the sample mean difference between two compared groups) would be equal to or more extreme than its observed value."
[ASA Statement on Statistical Significance and P-Values](http://amstat.tandfonline.com/doi/full/10.1080/00031305.2016.1154108)

Again, [wikipedia](https://en.wikipedia.org/wiki/P-value) is a great resource. You can also read the short blog from [realClearScience](http://www.realclearscience.com/blog/2016/11/07/httpwwwrealclearsciencecomblog20161107httpwwwrealclearsciencecomblog20161102httpwwwrealclearsciencecomblog201610the_biggest_myth_about_the_p-value.html) to make sure you have the main idea right. 

The key concepts and *limitations* are:

1. P-values can indicate how incompatible the data are with a specified statistical model.

2. P-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone.

3. Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold.

4. Proper inference requires full reporting and transparency. P-values and related analyses should not be reported selectively.

5. A p-value, or statistical significance, does not measure the size of an effect or the importance of a result.

6. By itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis.

### Exercise on p-values : [TBD]

### Multiple Comparison problem:

One of the best way to understand the problem is to look at the [xkcd view of it](https://xkcd.com/882/). The cartoon is great not only because it exposes the issue, but because it exposes the *consequence* of the issue in peer review publications. 


[Multiple Comparisons](https://en.wikipedia.org/wiki/Multiple_comparisons_problem#Classification_of_multiple_hypothesis_tests)

## p-value and base rate fallacy:

This [blog on p-values](http://www.statisticsdonewrong.com/p-value.html)
   concerns number of drugs tested, but could easily generalize to number of voxels or ROIs tested. It introduces to very important concepts, read carefully and make sure you understand what is the base rate fallacy.  After reading, you should know of Type I and Type II errors. 

### Exercise on multiple comparison issue : [TBD]

## Understanding statistical power and significance testing:

- interactive visualization for NHST:
[NHST](http://rpsychologist.com/d3/NHST/)

- Confidence intervals:
[Confidence intervals:](http://rpsychologist.com/d3/CI/)


## Distributions 

You need to understand what is a *distribution*. Here are some links on distributions and CDFs:

[Definition of distributions](https://en.wikipedia.org/wiki/Probability_distribution)

There is also this link that will tell you about statistical distributions: 

[this link](http://mathworld.wolfram.com/StatisticalDistribution.html)


Next, we need to be able to use the [Cumulative Density function](https://en.wikipedia.org/wiki/Cumulative_distribution_function). 

The CDF is related to its Complementary cumulative distribution function (also called tail distribution, or survival function :  $$ SF(x) =  1 - CDF(x) $$. 

The cumulative density function of a random variable X is often noted $$F_X$$ or simply $$F$$ when there is no ambiguity. 

### Questions on distribution, probability density function, and cumulative density function. 
[TBD]


### Going further : what is the distribution of a p-value?

You should have now an idea of what is a distribution, and what is the cumulative density function of a random variable.


An interesting fact is that p-values, which are random variable because they are just a function of the data, and the data are random (since you got these specific data by sampling eg subjects, right ?).

So, say you sample from a normal N(0,1) distribution, what is the distribution of a p-value for a test T (for instance the test T is simply a z-score for a sample of N(0,1) variables. 

Let's take T as your random variable. Note, the definition of a [random variable](https://en.wikipedia.org/wiki/Random_variable) is not straightforward, but roughly speaking it is a function that "maps from an outcome of the events (that is, from a point in a probability space) to a mathematically convenient outcome label, usually a real number." 

Let's $$ P = F(T) $$ Where $$ F $$ is the CDF of $$ T $$ i.e. $$ F(t) \equiv F_T(t) \equiv Pr(T \leq t) $$. 

$$ Pr(P < p) = Pr(F(T) < p) $$

If F is invertible, and for continuous random variable with strictly monotonic cumulative density function this is the case, we have 

$$ F(T) \leq p \equiv F^{-1}F(T) \leq F^{-1}(p) $$

hence, 

$$ Pr(P \leq p) = Pr(T \leq F^{-1}(p)) \equiv F(F^{-1}(p)) = p $$

So, 

$$ Pr( P \leq p) = F_p(p) = p $$

Therefore, the CDF of $$P$$ is the identity function $$ CDF(x)=x $$. The probability function is simply the derivative of the CDF (when this derivative exists) here $$ PDF(x) = f(x) = 1 $$.  This is a uniform random variable !

This fact is used latter on for instance to demonstrate the presence in p-hacking in the litterature. See lesson on what is p-hacking.

## Bayesian statistics / 

Finding the right level of introduction for this topic is not easy. We propose to start with [this blog](https://www.analyticsvidhya.com/blog/2016/06/bayesian-statistics-beginners-simple-english/) which should give you a good introduction. 

Bayesian statistics are *rarely* used, because researchers often know how to use them, and because they sometimes can be used to include subjective knowledge. However, they have a better theoretical ground and should be used in practice. 

The inertia of the community to adopt better frameworks is certain.  One reason for this inertia is that reviewers would need some training, and the training at the level required is often missing. Another issue is that the tools are also sometimes missing.  

### Questions on Bayesian statistics and comparison with frequentist:
[TBD]

 
## Notion of model comparison : BIC/Akaike

Model comparison is **fundamental**. 

