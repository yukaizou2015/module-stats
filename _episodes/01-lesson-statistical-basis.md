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

You may hear a statistician talk about "a statistic". For instance, $$t$$ or $$F$$ values are statistics distributed according to a Student or a Snedecor distribution. But what is a "statistic" ? 
In simple words, a statistic is any function of the data. The data are generally randomly sampled, and their distribution is often modelled with known distribution. Let's immagine that you have measured something interesting on $$N$$ subject, say that the measures are the $$Y_1,Y_2, ..., Y_N$$, and you are interested in the mean of the $$Y$$. The mean is a function of the data. It is a statistics. So would be the product of the $$Y$$s, etc. Since the $$Y$$s are random in the sense that they are randomly sampled from a population, and that another sampling would yield different values, the statistic is a random variable as well. For some interesting statistics, such as the average divided by the standard deviation, the distribution of the statistic is known if we assume the distribution of the original data to be known (often, a normal distribution is assumed).

## P-value

If the distribution of a statistic is assumed (by assuming the distribution of the original data) it can be used to compute a p-value. For instance, if you assume that the distribution of the sum of the $$Y$$s is normal and has zero mean, and if we estimate the dispersion (the variance), we have a distribution under the hypothesis that the sum of the values has zero mean. We can then compare the *observed* statistic with its distribution under this (null) hypothesis. 

"Informally, a p-value is the *probability* under a specified statistical model that a statistical summary of the data (e.g., the sample mean difference between two compared groups) would be equal to or more extreme than its observed value." It requires that we know the distribution of the statistic (the "statistical summary") under a certain hypothesis. 
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

You should have now a good idea of what is a distribution, and what is the cumulative density function of a random variable.


An interesting fact is that p-values, which are random variable because they are just a function of the data, and the data are random (since you got these specific data by sampling eg subjects).

So, say you sample from a normal N(0,1) distribution, what is the distribution of a p-value for a test T (for instance the test T is simply a z-score for a sample of N(0,1) variables).

Let's take T as your random variable. Note, the definition of a [random variable](https://en.wikipedia.org/wiki/Random_variable) is not straightforward, but roughly speaking it is a function that "maps from an outcome of the events (that is, from a point in a probability space) to a mathematically convenient outcome label, usually a real number." 

We write *"equal by definition"* with the symbol $$\equiv$$. We note the random variables with capital letters and specific values taken by lower case letters. $$F_T$$ is the cumulative density function (CDF) of $$T$$, and $$F_P$$ is the CDF of $$P$$. 

We define our variable $$P$$ with:
$$ P \equiv F_T(T) $$ <!--- Where $$ F $$ is the CDF of $$ T $$ --->

This means that $$ F_T(t) \equiv Pr(T \leq t) $$. We have by definition of $$P$$: 

$$ Pr(P \leq p) = Pr(F_T(T) \leq p) $$

If F is invertible, and for continuous random variable with strictly monotonic CDF (CDF that are never "flat") it is the case,  $$F_T$$ has an inverse $$F_T^{-1}$$, and we can apply this function on both side of the inequality without changing the inequality: 

$$ F_T(T) \leq p \equiv F_T^{-1}F_T(T) \leq F_T^{-1}(p) $$

hence, 

$$ Pr(P \leq p) = Pr(T \leq F^{-1}(p)) \equiv F_T(F_T^{-1}(p)) = p $$

So, 

$$ Pr( P \leq p) \equiv F_p(p) = p $$

Therefore, the CDF of $$P$$ is the identity function $$ CDF(x)=x $$. As the probability distribution function (PDF) is simply the derivative of the CDF (when this derivative exists) we finally have that $$ PDF(P) =  1 $$, with $$P$$ taking values between 0 and 1.  This is a uniform random variable, each observed p is as likely as any other.

This fact is used latter in this course on for instance to demonstrate the presence in p-hacking in the litterature. See lesson on what is p-hacking.

## Bayesian statistics / 

Finding the right level of introduction for this topic is not easy. We propose to start with [this blog](https://www.analyticsvidhya.com/blog/2016/06/bayesian-statistics-beginners-simple-english/) which should give you a good introduction. 

Bayesian statistics are *rarely* used, because researchers are often unsure on how to use them, and because they sometimes can be used to include subjective knowledge. However, they have a better theoretical ground and in many cases they should be used. 

The inertia of the community to adopt the bayesian framework is clear.  One reason for this inertia is that researchers and reviewers would need some training, and the training -at the level required- is often missing. Another issue is that the computational tools are also sometimes missing.  

### Questions on Bayesian statistics and comparison with frequentist:
[TBD]

 
## Notion of model comparison : BIC/Akaike

Model comparison is **fundamental**. Something on that topic is [TBD]. 

