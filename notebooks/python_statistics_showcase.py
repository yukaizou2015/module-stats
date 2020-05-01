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

# # Statistics in Python
#
# In this notebook, we will cover how you can use Python for statistics, ranging from data exploration and inspection over testing of assumptions to divers models. There are many packages to do so, but we will focus on four:
#
# - [pandas](https://pandas.pydata.org/)
# - [scipy's stats module](https://docs.scipy.org/doc/scipy/reference/stats.html)
# - [statsmodels](http://www.statsmodels.org/stable/index.html)
# - [seaborn](seaborn.pydata.org).
#
# This notebook is strongly based on the [scipy-lectures.org](http://www.scipy-lectures.org/packages/statistics/index.html) section about statistics.

# # Data representation and interaction
#
# ## Data as a table
#
# The setting that we consider for statistical analysis is that of multiple *observations* or *samples* described by a set of different *attributes* or *features*. The data can than be seen as a 2D table, or matrix, with columns giving the different attributes of the data, and rows the observations. For instance, the data contained in `brain_size.csv`:

# !head ../data/brain_size.csv

# ## The pandas data-frame
#
# ### Creating dataframes: reading data files or converting arrays
#  
# #### Reading from a CSV file
# Using the above CSV file that gives observations of brain size and weight and IQ (Willerman et al. 1991), the data are a mixture of numerical and categorical values::

import pandas as pd
data = pd.read_csv('../data/brain_size.csv', sep=';', na_values=".")
data

# #### Creating from arrays
# A `pandas.DataFrame` can also be seen as a dictionary of 1D 'series', eg arrays or lists. If we have 3 ``numpy`` arrays:

import numpy as np
t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)

# We can expose them as a `pandas.DataFrame`:

pd.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t}).head()

# **Other inputs**: [pandas](http://pandas.pydata.org) can input data from SQL, excel files, or other formats. See the [pandas documentation](http://pandas.pydata.org).

# ### Manipulating data
#
# `data` is a `pandas.DataFrame`, that resembles R's dataframe:

data.shape    # 40 rows and 8 columns

data.columns  # It has columns

print(data['Hair'].head())  # Columns can be addressed by name

# Simpler selector
data[data['Hair'] == 'light']['VIQ'].mean()

# **Note:** For a quick view on a large dataframe, use `describe`: `pandas.DataFrame.describe`.

data.describe()

# Frequency count for a given column
data['Height'].value_counts()

# Dummy-code # of hair color (i.e., get N-binary columns)
pd.get_dummies(data['Hair'])[:15]

# #### The [split-apply-combine](https://www.jstatsoft.org/article/view/v040i01/v40i01.pdf) pattern
# * A very common data processing strategy is to...
#     * Split the dataset into groups
#     * Apply some operation(s) to each group
#     * (Optionally) combine back into one dataset
#
# Pandas provides powerful and fast tools for this. For example the `groupby` function.

# **groupby**: splitting a dataframe on values of categorical variables:

groupby_hair = data.groupby('Hair')
for hair, value in groupby_hair['VIQ']:
     print((hair, value.mean()))

# `groupby_hair` is a powerful object that exposes many operations on the resulting group of dataframes:

groupby_hair.mean()

# + [markdown] solution2="hidden" solution2_first=true
# ### Exercise 1
#
# * What is the mean value for VIQ for the full population?
# * How many dark/light haired people were included in this study?
# * What is the average value of MRI counts expressed in log units, for people with dark and light hair?

# + solution2="hidden"
data['VIQ'].mean()

# + solution2="hidden"
groupby_hair['Hair'].count()

# + solution2="hidden"
np.log(groupby_hair.MRI_Count.mean())

# +
# Create solution here
# -

# ### Plotting data
#
# Pandas comes with some plotting tools (`pandas.tools.plotting`, using
# matplotlib behind the scene) to display statistics of the data in
# dataframes.
#
# For example, let's use `boxplot` (in this case even `groupby_hair.boxplot`) to better understand the structure of the data.

# %matplotlib inline
groupby_hair.boxplot(column=['FSIQ', 'VIQ', 'PIQ']);

# #### Scatter matrices

pd.plotting.scatter_matrix(data[['Weight', 'Height', 'FSIQ']]);

# <img src="https://github.com/raphaelvallat/pingouin/blob/master/docs/pictures/logo_pingouin.png?raw=true" height="300" width="700"/>
#
#
#
# ### _Pingouin is an open-source statistical package written in Python 3 and based mostly on Pandas and NumPy._
#
#
# - ANOVAs: one- and two-ways, repeated measures, mixed, ancova
# - Post-hocs tests and pairwise comparisons
# - Robust correlations
# - Partial correlation, repeated measures correlation and intraclass correlation
# - Linear/logistic regression and mediation analysis
# - Bayesian T-test and Pearson correlation
# - Tests for sphericity, normality and homoscedasticity
# - Effect sizes and power analysis
# - Parametric/bootstrapped confidence intervals around an effect size or a correlation coefficient
# - Circular statistics
# - Plotting: Bland-Altman plot, Q-Q plot, etc...
#
# **Pingouin is designed for users who want simple yet exhaustive statistical functions.**
#
#
# ##### **material scavenged from [10 minutes to Pingouin](https://pingouin-stats.org/index.html) and [the pingouin docs](https://pingouin-stats.org/api.html)

import pingouin as pg

# [Measures of correlation](https://pingouin-stats.org/generated/pingouin.corr.html#pingouin.corr)
#
# "In the broadest sense correlation is any statistical association, though in common usage it most often refers to how close two variables are to having a linear relationship with each other" - [Wikipedia](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
#
# When talking about correlation, we commonly mean the Pearson correlation coefficient, also referred to as Pearson's r:
#
# <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/93185aed3047ef42fa0f1b6e389a4e89a5654afa"/>
#
#

pearson_correlation = pg.corr(data['FSIQ'], data['VIQ'])
display(pearson_correlation)
cor_coeeficient = pearson_correlation['r']
n =  len(data) # sample size

# ### Test summary
#
# - `n` : Sample size (after NaN removal)
# - `outliers` : number of outliers (only for `shepherd` or `skipped`)
# - `r` : Correlation coefficient
# - `CI95` : [95% parametric confidence intervals](https://en.wikipedia.org/wiki/Confidence_interval)
# - `r2` : [R-squared](https://en.wikipedia.org/wiki/Coefficient_of_determination)
# - `adj_r2` : [Adjusted R-squared](https://en.wikipedia.org/wiki/Coefficient_of_determination#Adjusted_R2)
# - `p-val` : one or two tailed p-value
# - `BF10` : Bayes Factor of the alternative hypothesis (Pearson only)
# - `power` : achieved power of the test (= 1 - type II error)

# ### Pairwise correlations between columns of a dataframe

# +
np.random.seed(123)
mean, cov, n = [170, 70], [[20, 10], [10, 20]], 30
x, y = np.random.multivariate_normal(mean, cov, n).T
z = np.random.normal(5, 1, 30)
data_pairwise = pd.DataFrame({'X': x, 'Y': y, 'Z': z})

# Pairwise correlation sorted from largest to smallest R2
pg.pairwise_corr(data_pairwise, columns=['X', 'Y', 'Z']).sort_values(by=['r2'], ascending=False)
# -

# ### Before we calculate:  `Testing statistical premises`
#
# Statistical procedures can be classfied into either [`parametric`](https://en.wikipedia.org/wiki/Parametric_statistics) or `non parametric` prcedures, which require different necessary preconditions to be met in order to show consistent/robust results. 
# Generally people assume that their data follows a gaussian distribution, which allows for parametric tests to be run.
# Nevertheless it is essential to first test the distribution of your data to decide if the assumption of normally distributed data holds, if this is not the case we would have to switch to non parametric tests.

# ### [Shapiro Wilk normality  test](https://pingouin-stats.org/generated/pingouin.normality.html#pingouin.normality)
#
# Standard procedure to test for normal distribution. Tests if the distribution of your data deviates significtanly from a normal distribution.
# Returns:
# - `normal` : boolean
#     True if x comes from a normal distribution.
#
# - `p` : float
#     P-value.
#

# +
# Return a boolean (true if normal) and the associated p-value
 
pg.normality(data, method='normaltest')
# -

# ### [Henze-Zirkler multivariate normality test](https://pingouin-stats.org/generated/pingouin.multivariate_normality.html#pingouin.multivariate_normality)
#
# Same procedure for [multivariate normal distributions](https://en.wikipedia.org/wiki/Multivariate_normal_distribution)
#
# returns 
#
# - `normal` : boolean
#     True if X comes from a multivariate normal distribution.
#
# - `p` : float
#     P-value.

# Return a boolean (true if normal) and the associated p-value
np.random.seed(123)
mean, cov, n = [4, 6], [[1, .5], [.5, 1]], 30
X = np.random.multivariate_normal(mean, cov, n)
normal, p = pg.multivariate_normality(X, alpha=.05)
print(normal, p)

# ### [Mauchly test for sphericity](https://pingouin-stats.org/generated/pingouin.sphericity.html#pingouin.sphericity)
#
# "Sphericity is the condition where the variances of the differences between all combinations of related groups (levels) are equal. Violation of sphericity is when the variances of the differences between all combinations of related groups are not equal." - https://statistics.laerd.com/statistical-guides/sphericity-statistical-guide.php
#
#
# returns 
#
# - `spher` : boolean
#     True if data have the sphericity property.
#
# - `W` : float
#     Test statistic
#
# - `chi_sq` : float
#     Chi-square statistic
#
# - `ddof` : int
#     Degrees of freedom
#
# - `p` : float
#     P-value.

pg.sphericity(data)

# ### [Testing for homoscedasticity](https://pingouin-stats.org/generated/pingouin.homoscedasticity.html#pingouin.homoscedasticity)
#
# "In statistics, a sequence or a vector of random variables is homoscedastic /ˌhoʊmoʊskəˈdæstɪk/ if all random variables in the sequence or vector have the same finite variance." - [wikipedia](https://en.wikipedia.org/wiki/Homoscedasticity)
#
# returns:	
# - `equal_var` : boolean
#     True if data have equal variance.
#
# - `p` : float
#     P-value.
#
#
# *Note:
# This function first tests if the data are normally distributed using the **Shapiro-Wilk test**. If yes, then the homogeneity of variances is measured using the **Bartlett test**. If the data are not normally distributed, the **Levene test**, which is less sensitive to departure from normality, is used.*

np.random.seed(123)
# Scale = standard deviation of the distribution.
data_array = [[4, 8, 9, 20, 14], np.array([5, 8, 15, 45, 12])]
pg.homoscedasticity(data_array, method="bartlett", alpha=.05)


# ## Parametric tests
# ## Student's t-test: the simplest statistical test
#
# ### 1-sample t-test: testing the value of a population mean
#
# Tests if the population mean of data is likely to be equal to a given value (technically if observations are drawn from a Gaussian distributions of given population mean).
#
#
# `pingouin.ttest` returns the T_statistic, the p-value, the 
# [degrees of freedom](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)), the [Cohen d effect size](https://en.wikiversity.org/wiki/Cohen%27s_d), the achieved [power](https://en.wikipedia.org/wiki/Power_(statistics)) of the test ( = 1 - type II error (beta) = [P(Reject H0|H1 is true)](https://deliveroo.engineering/2018/12/07/monte-carlo-power-analysis.html)), and the [Bayes Factor](https://en.wikipedia.org/wiki/Bayes_factor) of the alternative hypothesis
#
#
#
#

pg.ttest(data['VIQ'], 0)

# ### 2-sample t-test: testing for difference across populations
#
# We have seen above that the mean VIQ in the black hair and white hair populations
# were different. To test if this is significant, we do a 2-sample t-test:

light_viq = data[data['Hair'] == 'light']['VIQ']
dark_viq = data[data['Hair'] == 'dark']['VIQ']

pg.ttest(light_viq, dark_viq)

# ### Plot achieved power of a paired T-test
#
# Plot the curve of achieved power given the effect size (Cohen d) and the sample size of a paired T-test.

# +
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='ticks', context='notebook', font_scale=1.2)

d = 0.5  # Fixed effect size
n = np.arange(5, 80, 5)  # Incrementing sample size

# Compute the achieved power
pwr = pg.power_ttest(d=d, n=n, contrast='paired', tail='two-sided')

# Start the plot
plt.plot(n, pwr, 'ko-.')
plt.axhline(0.8, color='r', ls=':')
plt.xlabel('Sample size')
plt.ylabel('Power (1 - type II error)')
plt.title('Achieved power of a paired T-test')
sns.despine()
# -

# ### Non-parametric tests:
#
#
# Unlike the parametric test these do not require the assumption of normal distributions.
#
# "`Mann-Whitney U Test` (= Wilcoxon rank-sum test). It is the non-parametric version of the independent T-test.
# Mwu tests the hypothesis that data in x and y are samples from continuous distributions with equal medians. The test assumes that x and y are independent. This test corrects for ties and by default uses a continuity correction." - [mwu-function](https://pingouin-stats.org/generated/pingouin.mwu.html#pingouin.mwu)
#
# Test summary
#
# - 'W-val' : W-value
# - 'p-val' : p-value
# - 'RBC'   : matched pairs rank-biserial correlation (effect size)
# - 'CLES'  : common language effect size

pg.mwu(light_viq, dark_viq)

# "`Wilcoxon signed-rank test` is the non-parametric version of the paired T-test.
#
# The Wilcoxon signed-rank test tests the null hypothesis that two related paired samples come from the same distribution. A continuity correction is applied by default." - [wilcoxon - func](https://pingouin-stats.org/generated/pingouin.wilcoxon.html#pingouin.wilcoxon)
#

# example from the function definition
# Wilcoxon test on two related samples.
x = [20, 22, 19, 20, 22, 18, 24, 20]
y = [38, 37, 33, 29, 14, 12, 20, 22]
print("Medians = %.2f - %.2f" % (np.median(x), np.median(y)))
pg.wilcoxon(x, y, tail='two-sided')

# ### `scipy.stats` - Hypothesis testing: comparing two groups
#
# For simple [statistical tests](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing), it is also possible to use the `scipy.stats` sub-module of [`scipy`](http://docs.scipy.org/doc/).

from scipy import stats

# ### 1-sample t-test: testing the value of a population mean
#
# `scipy.stats.ttest_1samp` tests if the population mean of data is likely to be equal to a given value (technically if observations are drawn from a Gaussian distributions of given population mean). It returns the [T statistic](https://en.wikipedia.org/wiki/Student%27s_t-test), and the [p-value](https://en.wikipedia.org/wiki/P-value) (see the function's help):

stats.ttest_1samp(data['VIQ'], 100)

# With a p-value of 10^-28 we can claim that the population mean for the IQ (VIQ measure) is not 0.

# ### 2-sample t-test: testing for difference across populations
#
# We have seen above that the mean VIQ in the dark hair and light hair populations
# were different. To test if this is significant, we do a 2-sample t-test
# with `scipy.stats.ttest_ind`:

light_viq = data[data['Hair'] == 'light']['VIQ']
dark_viq = data[data['Hair'] == 'dark']['VIQ']
stats.ttest_ind(light_viq, dark_viq)

# ## Paired tests: repeated measurements on the same indivuals
#
# PIQ, VIQ, and FSIQ give 3 measures of IQ. Let us test if FISQ and PIQ are significantly different. We can use a 2 sample test:

stats.ttest_ind(data['FSIQ'], data['PIQ'])

# The problem with this approach is that it forgets that there are links
# between observations: FSIQ and PIQ are measured on the same individuals.
#
# Thus the variance due to inter-subject variability is confounding, and
# can be removed, using a "paired test", or ["repeated measures test"](https://en.wikipedia.org/wiki/Repeated_measures_design):

stats.ttest_rel(data['FSIQ'], data['PIQ'])

# This is equivalent to a 1-sample test on the difference::

stats.ttest_1samp(data['FSIQ'] - data['PIQ'], 0)

# T-tests assume Gaussian errors. We can use a [Wilcoxon signed-rank test](https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test), that relaxes this assumption:

stats.wilcoxon(data['FSIQ'], data['PIQ'])

# **Note:** The corresponding test in the non paired case is the [Mann–Whitney U test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U), `scipy.stats.mannwhitneyu`.

# + [markdown] solution2="hidden" solution2_first=true
# ### Exercise 2
#
# * Test the difference between weights in people with dark and light hair.
# * Use non-parametric statistics to test the difference between VIQ in people with dark and light hair.

# + solution2="hidden"
light_weight = data[data['Hair'] == 'light']['Weight']
dark_weight = data[data['Hair'] == 'dark']['Weight']
stats.ttest_ind(light_weight, dark_weight, nan_policy='omit')
stats.mannwhitneyu(light_viq, dark_viq)

# + solution2="hidden"


# + [markdown] solution2="hidden"
# **Conclusion**: we find that the data does not support the hypothesis that people with dark and light hair have different VIQ.

# +
# Create solution here
# -

# # `statsmodels` - use "formulas" to specify statistical models in Python
#
# Use `statsmodels` to perform linear models, multiple factors or analysis of variance.
#
#
# ## A simple linear regression
#
# Given two set of observations, `x` and `y`, we want to test the hypothesis that `y` is a linear function of `x`.
#
# In other terms:
#
# $y = x * coef + intercept + e$
#
# where $e$ is observation noise. We will use the [statsmodels](http://statsmodels.sourceforge.net) module to:
#
# 1. Fit a linear model. We will use the simplest strategy, [ordinary least squares](https://en.wikipedia.org/wiki/Ordinary_least_squares) (OLS).
# 2. Test that $coef$ is non zero.
#
# First, we generate simulated data according to the model:

# +
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 20)
np.random.seed(1)

# normal distributed noise
y = -5 + 3*x + 4 * np.random.normal(size=x.shape)

# Create a data frame containing all the relevant variables
data = pd.DataFrame({'x': x, 'y': y})

plt.plot(x, y, 'o');
# -

# Then we specify an OLS model and fit it:

from statsmodels.formula.api import ols
model = ols("y ~ x", data).fit()

# **Note:** For more about "formulas" for statistics in Python, see the [statsmodels documentation](http://statsmodels.sourceforge.net/stable/example_formulas.html).

# We can inspect the various statistics derived from the fit::

print(model.summary())

# ### Terminology
#
# Statsmodels uses a statistical terminology: the `y` variable in statsmodels is called *endogenous* while the `x` variable is called *exogenous*. This is discussed in more detail [here](http://statsmodels.sourceforge.net/devel/endog_exog.html). To simplify, `y` (endogenous) is the value you are trying to predict, while `x` (exogenous) represents the features you are using to make the prediction.

# + [markdown] solution2="hidden" solution2_first=true
# ### Exercise 3
#
# Retrieve the estimated parameters from the model above.  
# **Hint**: use tab-completion to find the relevant attribute.

# + solution2="hidden"
model.params

# +
# Create solution here
# -

# ## Categorical variables: comparing groups or multiple categories
#
# Let us go back the data on brain size:

data = pd.read_csv('../data/brain_size.csv', sep=';', na_values=".")

# We can write a comparison between IQ of people with dark and light hair using a linear model:

model = ols("VIQ ~ Hair + 1", data).fit()
print(model.summary())

# ### Tips on specifying model
#  
# ***Forcing categorical*** - the 'Hair' is automatically detected as a categorical variable, and thus each of its different values is treated as different entities.
#
# An integer column can be forced to be treated as categorical using:
#
# ```python
# model = ols('VIQ ~ C(Hair)', data).fit()
# ```
#
# ***Intercept***: We can remove the intercept using `- 1` in the formula, or force the use of an intercept using `+ 1`.

# ### Link to t-tests between different FSIQ and PIQ
#
# To compare different types of IQ, we need to create a "long-form" table, listing IQs, where the type of IQ is indicated by a categorical variable:

data_fisq = pd.DataFrame({'iq': data['FSIQ'], 'type': 'fsiq'})
data_piq = pd.DataFrame({'iq': data['PIQ'], 'type': 'piq'})
data_long = pd.concat((data_fisq, data_piq))
print(data_long[::8])

model = ols("iq ~ type", data_long).fit()
print(model.summary())

# We can see that we retrieve the same values for t-test and corresponding p-values for the effect of the type of IQ than the previous t-test:

stats.ttest_ind(data['FSIQ'], data['PIQ'])

# ## Multiple Regression: including multiple factors
#
# Consider a linear model explaining a variable `z` (the dependent
# variable) with 2 variables `x` and `y`:
#
# $z = x \, c_1 + y \, c_2 + i + e$
#
# Such a model can be seen in 3D as fitting a plane to a cloud of (`x`,
# `y`, `z`) points (see the following figure).

# +
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-5, 5, 21)

# We generate a 2D grid
X, Y = np.meshgrid(x, x)

# To get reproducable values, provide a seed value
np.random.seed(1)

# Z is the elevation of this 2D grid
Z = -5 + 3*X - 0.5*Y + 8 * np.random.normal(size=X.shape)

# Plot the data
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.coolwarm,
                       rstride=1, cstride=1)
ax.view_init(20, -120)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# -

# ### Example: the iris data (`iris.csv`)
#
# Sepal and petal size tend to be related: bigger flowers are bigger! But is there, in addition, a systematic effect of species?

# +
from pandas.plotting import scatter_matrix

#Load the data
data = pd.read_csv('../data/iris.csv')

# Express the names as categories
categories = pd.Categorical(data['Species'])

# The parameter 'c' is passed to plt.scatter and will control the color
scatter_matrix(data, c=categories.codes, marker='o')

# Plot figure
fig.suptitle("blue: setosa, green: versicolor, red: virginica", size=25)
plt.show()
# -

model = ols('SepalWidth ~ Species + PetalLength', data).fit()
print(model.summary())

# ## Post-hoc hypothesis testing: analysis of variance (ANOVA)
#
# In the above iris example, we wish to test if the petal length is different between versicolor and virginica, after removing the effect of sepal width. This can be formulated as testing the difference between the coefficient associated to versicolor and virginica in the linear model estimated above (it is an Analysis of Variance, [ANOVA](https://en.wikipedia.org/wiki/Analysis_of_variance). For this, we write a **vector of 'contrast'** on the parameters estimated: we want to test ``"name[T.versicolor] - name[T.virginica]"``, with an [F-test](https://en.wikipedia.org/wiki/F-test):

print(model.f_test([0, 1, -1, 0]))

# Is this difference significant?

# + [markdown] solution2="hidden" solution2_first=true
# ### Exercise 4
#
# Going back to the brain size + IQ data, test if the VIQ of people with dark and light hair are different after removing the effect of brain size, height, and weight.

# + solution2="hidden"
data = pd.read_csv('../data/brain_size.csv', sep=';', na_values=".")
model = ols("VIQ ~ Hair + Height + Weight + MRI_Count", data).fit()
print(model.summary())

# +
# Create solution here
# -

# # `seaborn` - use visualization for statistical exploration
#
# [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/) combines simple statistical fits with plotting on pandas dataframes.
#
# Let us consider a data giving wages and many other personal information on 500 individuals ([Berndt, ER. The Practice of Econometrics. 1991. NY:Addison-Wesley](http://lib.stat.cmu.edu/datasets/CPS_85_Wages)).

import pandas as pd
data = pd.read_csv('../data/wages.csv', sep=',')
data.head()

# ## Pairplot: scatter matrices
#
# We can easily have an intuition on the interactions between continuous variables using `seaborn.pairplot` to display a scatter matrix:

import seaborn
seaborn.set()
seaborn.pairplot(data, vars=['WAGE', 'AGE', 'EDUCATION'], kind='reg')

# Categorical variables can be plotted as the hue:

seaborn.pairplot(data, vars=['WAGE', 'AGE', 'EDUCATION'], kind='reg', hue='HAIR')

# ## lmplot: plotting a univariate regression
#
# A regression capturing the relation between one variable and another, e.g. wage and eduction, can be plotted using `seaborn.lmplot`:

seaborn.lmplot(y='WAGE', x='EDUCATION', data=data)

# ### Robust regression
# Given that, in the above plot, there seems to be a couple of data points that are outside of the main cloud to the right, they might be outliers, not representative of the population, but driving the regression.
#
# To compute a regression that is less sensitive to outliers, one must use a [robust model](https://en.wikipedia.org/wiki/Robust_statistics). This is done in seaborn using ``robust=True`` in the plotting functions, or in statsmodels by replacing the use of the OLS by a "Robust Linear Model", `statsmodels.formula.api.rlm`.

# # Testing for interactions
#
# Do wages increase more with education for people with dark hair than with light hair?

seaborn.lmplot(y='WAGE', x='EDUCATION', hue='HAIR', data=data)

# The plot above is made of two different fits. We need to formulate a single model that tests for a variance of slope across the population. This is done via an ["interaction"](http://statsmodels.sourceforge.net/devel/example_formulas.html#multiplicative-interactions).

from statsmodels.formula.api import ols
result = ols(formula='WAGE ~ EDUCATION + HAIR + EDUCATION * HAIR', data=data).fit()
print(result.summary())

# Can we conclude that education benefits people with dark hair more than people with light hair?

# # Take home messages
#
# * Hypothesis testing and p-value give you the **significance** of an effect / difference
#
# * **Formulas** (with categorical variables) enable you to express rich links in your data
#
# * **Visualizing** your data and simple model fits matters!
#
# * **Conditioning** (adding factors that can explain all or part of the variation) is an important modeling aspect that changes the interpretation.
