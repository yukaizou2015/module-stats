---
title: "Effect size and variation of effect sizes in brain imaging"
teaching: 60 
exercises: 120 
questions: 
- "Variance explained "
- "What is an effect size, statistical versus biological or medical relevance"
- "The variation of effect sizes: "
- "Sampling, Models, Processing parameters, Population, effect of unknown parameters"
- "Other measures of effect size"
objectives:
- "After this lesson, you should have a good knowledge of what is an effect size, and why it is important to report it and assess it. "
keypoints:
- "Effect sizes come in many forms"
- "Significance is not relevance"
- "Difference between the raw effect size and the cohen's d effect size"
- "How can the effect size vary ? Why is it important to know about this?"

- Effect sizes are under reported, not well understood, and are crucial for our scientific understanding. Let's fix this.

---

### Effect sizes: first basics.  

Here, we start with an explanation of the effect size using a t-test. First, have a look at the [wikipedia](https://en.wikipedia.org/wiki/Effect_size) page on effect size. Please read carefully the Overview section. 

Is the overview clear to you? Just to orient you a bit more if it is not, say we want to test the difference of the means of two populations, for instance the brain activity in the visual cortex for the normal versus patient population. We *sample* 30 normals and 30 patients, and we compute *estimated* means of the two populations using our *samples* of 30 + 30 participants. Let's measure the BOLD response in the visual cortex for all participants. The average of the 30 participants in the control group (CG) is 5\%. The average of the 30 participants in the patient group (PG) is 8\%. The standard deviation of the data (not of the average that we just referred to) in the CG is 1\%  and the standard deviation of the CG is 2\%. 

Now, let's say we are studying the activity of the visual cortex in the CG. You want to know if this is different from zero. The *estimated* effect size for the CG is 5%. The **normalized** effect size will be 5/1 = 5 for CG, and 8/2=4 for the PG, while the corresponding t-test will be t=5/(1/sqrt(30-1)) and t=8/(2/sqrt(30-1))

Now, how would you define the *estimated* effect size of the difference of the two population? The "raw" / "not normalized" effect size would simply be 8-5\%. To define the **normalized** is not directly possible because here there is no variability of one population: we have two populations. One possibility is to use the [Welch's](https://en.wikipedia.org/wiki/Welch%27s_t-test) statistics and degrees of freedom, and define the normalized effect size as t times the estimated degrees of freedom. 

The advantage of using a normalized effect size is that it makes comparisons possible. 


Questions: 	
	- Is the coefficient of correlation an effect size ? 
	- Can I always compare normalized effect sizes?

### Variance explained, using the example of the general linear model

There are many good introductions to the GLM. Here, we propose that you use the pages from this course. The course takes you through the very basics of the GLM and shows you some implementation with python.  

Assignment: Read [this web page](https://matthew-brett.github.io/teaching/glm_intro.html). Use a terminal and python to go through the code and understand what is being done. If you do not know about python, you can go through the same page with R or Matlab, it will not take you long to translate it. However, we recommend that you learn enough python to be able to follow. If you need a python introduction, please follow the [beginners course](https://www.python.org/about/gettingstarted/) of Python. 

Now that you have a first  understanding of the GLM, make sure you follow easily [this page](https://bic-berkeley.github.io/psych-214-fall-2016/mean_test_example.html) that walk you through an other example. 

The next step is to understand the notion of variance explained. With your new (or refreshed) knowledge of the GLM, you can now go to [this page](https://bic-berkeley.github.io/psych-214-fall-2016/hypothesis_tests.html) that explains the t and F tests. When you have gone through this page, understand what is the R2 in multiple regression. Again, [wikipedia](https://en.wikipedia.org/wiki/Coefficient_of_determination) is a great resource, and you should now read and understand up to section "Interpretation".

Coming back to the effect size, we now can understand the Cohen's f2 effect size in [wikipedia](https://en.wikipedia.org/wiki/Effect_size).

Exercise: 
	- Is the R2 a "normalized effect size" ?
	- If you have an experiment with three samples of different populations, and some other covariables . Can you write what would be the R2 for the part of the model that corresponds to the difference of the means of the three groups ?  Can you generalize the wikipedia page on R2 to account for the case of an F test ? See how this is explained in a non-simple linear model in [wikipedia](https://en.wikipedia.org/wiki/Coefficient_of_determination). 


###  Effect size: statistical versus biological or medical relevance

In this section, we want to stress the difference between a significant effect and an important one. 

See for instance this [paper](http://onlinelibrary.wiley.com/doi/10.1111/j.1469-185X.2007.00027.x/full)

Please read it till the end: please go up to the end. This should take you around one hour. Try then to answer the following:

	- 


###  The variation of effect sizes 

####	    Variation with sampling, or variation because we are using a slightly different population 

####	    variation of effect size with a different model

####	    with workflow / pre-processing or over analysis choices parameters

### Unknown parameters

## Other measures of effect sizes

### 	can "prediction rate" be used ?

### 	can mutual information be used ?

- What is mutual information ? 
- Use as effect size ?


