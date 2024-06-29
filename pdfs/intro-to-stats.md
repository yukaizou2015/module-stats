---
title: ReproNim workshop - The use of p-values in brain imaging and statistical aspects in reproducibility 
shortitle: Evil p-values 
subtitle: A reproducibility perspective 
date:  Aug 2nd 2018
author: JB Poline \newline
institute: McGill University, UC Berkeley

header-include:
- \usefonttheme{professionalfonts}
- \usepackage{fontspec}
- \setsansfont[BoldFont = {Fira Sans Medium}]{Fira Sans}
- \setmonofont{Fira Mono}
- \usepackage{amsmath}
---

Plan
=================================================================================

- Issues of reproducibility in science, historical perspective
\pause
	- Was Ioannidis right?
\pause
	- Annecdotal evidence
\pause
- Where is the problem coming from?
	- computations, stats, sociology
	- cf everything matters 
\pause
- Emphasis on statistical issues
\pause
- Are there solutions ?

Issues of reproducibility in science 
========================================

![Stodden, 2014](./images/credibility-crisis.png){ height=320px }

<!--  still, many people do not take this seriously: this is only other researchers problem, not mine -->
<!--  evidence is growing, and funding agencies, institutions, journals, all working now -->

Issues of reproducibility in science 
========================================

- Data bias and specificities 
\pause
- Computational issues
\pause
- Statistical: p=0.05 is weak evidence 
\pause
- Ioannidis theoretical arguments "Why most research findings..."
\pause
- Statistics is about the **practice** of statistics
\pause
- Publication **pressure** is still immense

<!--   
- Study on the statistical practices 
	- Simmons and Simonsohn in psychology
	- Wang et al., 2018 in biomedical research
-->

Anecdotal evidence 1
=================================================================================

![Muller, 2017](./images/muller-jama-psy-unipolar-depression-meta-analysis.png){ height=100px }

\vspace{-1cm}

> \small{During the past 20 years, numerous neuroimaging experiments have investigated aberrant brain activation during cognitive and emotional processing in patients with unipolar depression.}
\pause

\pause
\vspace{-.2cm}
> \small{In total, 57 studies with 99 individual neuroimaging experiments comprising in total 1058 patients were included; 34 of them tested cognitive and 65 emotional processing. Overall analyses across cognitive processing experiments (P > .29) and across emotional processing experiments (P > .47) revealed **no significant results.** }

Anecdotal evidence 2: All foods cause cancer ? Schoenfeld 2013
=================================================================================

- Of 264 single-study assessments, 191 (72%) concluded that the tested food was associated with an increased (n = 103) or a decreased (n = 88) risk;
\pause
- 75% of the risk estimates had weak (0.05 > P > 0.001) or no statistical (P > 0.05) significance. 
\pause
- Meta-analyses presented more conservative results; only 13 (26%) reported an increased (n = 4) or a decreased (n = 9) risk  

Computational problems
=================================================================================

- OS can be a problem (same container, different segementation)
	- Glatard et al, 2015
\pause
- Version of librairies and software  
\pause
- Algorithms initialization  
\pause
- Algorithms sensitivity to noise (Kiar et al)
\pause
- Software variation 
<!--   -->

Evil p-values: Significance testing as perverse probabilistic reasoning
=================================================================================

![Westover, 2014](./images/westover-questions.png){ height=240px }

<!-- Here we first try to assess if we know what a p-value is  -->

Significance testing as perverse probabilistic reasoning
=================================================================================

![Westover, 2014](./images/westover-table-results.png){ height=200px }

- Westover, 2014
<!--   -->

P-value Definition 
=================================================================================

\Huge{Probability of observing a statistic equal to the one seen in the data, or one that is more “extreme”, when the null hypothesis is true}
<!--   -->

P-value requires:
=================================================================================

* Knowledge of the null hypothesis
\pause
* Choice of a statistic
\pause
* Concept of repeating the whole study in the same way 
	* Same study design
	\pause
	* Same sampling scheme
	\pause
	* Same definition of the statistic
<!--   -->

<!--   
Historical perspective
=================================================================================

- When did we start to talk of the problem? 
	- almost as soon as the time of the p-value was defined, 1925
\pause
- Fisher conception:
	- an indication of something about the data under H0
\pause
- Neyman-Pearson conception:
	- a decision making rule
	- it does not make sense to talk about "very significant / marginally significant"
\pause
- Which one is used today ?

-->

What happens if ... p is "significant" but study power is low ? 
=================================================================================

- Power : the probability of finding a significant p-value under H1
\pause
- Study in Button et al, 2013, more than half of the studies have less than 30% power
\pause
- Low Positive Predictive Value P($H_A$ true | test significant) 
\pause
- Inflated effect size
\pause
- Depends on the prior probability of $H_A$ and $H_0$ 
<!--   -->


Low Positive Predictive Value : P($H_A$ is true | test is significant) 
=================================================================================
 

![PPV = f(power)](./images/ppv-func-of-pwr-or-02-alph-05.png){ height=250px }

<!--   -->

Inflated effect size Effect-size = f(years, sample, ...)  
=================================================================================

![Molendijk, 2012, BDNF and hippocampal volume](./images/molendijk_2012_f4.png){ height=250px } 
\vspace{-.2cm}
- Molendijk, 2012, BDNF and hippocampal volume

<!--   
$\vspace{-1.2cm}$

![Mier, 2009, COMT & DLPFC](./images/mier_2009_f4.pdf)
-->


<!--   
Not everybody believes in power
=================================================================================

- Grant reviewer quote (grant on power rejected)

>  "... I am skeptical that searches of existing
>  studies have information that's relevant and targeted enough to assessing
>  power or reproducibility for scientifically *interesting new* designs."


Do we know how to compute some effect sizes ?
=================================================================================
- often *very hard* to find in the paper
\pause

![Hariri et al. Science, 2002](./images/hariri.png){ height=170px }
$\vspace{-0.10cm}$

* Authors report $m_1 = .28, m_2 = .03, \textrm{SDM}_1 = 0.08, \textrm{SDM}_2 = 0.05, N_1 = N_2 = 14$ 
* How do we compute the effect size ?  

-->


What happens if ... p is not significant? File drawer effect
=================================================================================

- Described by Rosenthal in **1979**
- Most publications accepted if p<.05 
- Hard to publish null results

>   "...  whether you would be able to review the manuscript "No Evidence
>   for an Effect of XXX on Hippocampal Volume in a YYY Sample", by  \emph{some-authors},
>   submited for consideration in ..."

![No evidence not published?](./images/no-evidence-papers.png){ height=100px }

Are we always testing/publishing at p=0.05 ? Incentive perversion 
=================================================================================

- Implies P-Hacking and Harking
	- Simmons and Simonsohn 2011, P-curves

![Simmons, 2011](./images/simmons-2011-table1.png){ height=180px }

<!--  \vspace{-.5cm} -->

Is p-hacking really happening ? 
=================================================================================

![Wang, 2018](./images/biostatistical-consulting.png){ height=200px }
\vspace{-.2cm}

- study gives **clear evidence** that researchers make requests of their
  biostatistical consultants that are not only rated as **severe violations**, but
  further that these requests occur quite **frequently**.

- P-curve: Simonsohn, U., Nelson, L.D., Simmons, J.P., 2014. 
	- Principle: literature should not have that many p close to .05 
	- p-values are uniformely distributed (how do you show that?)

Are we always testing/publishing at p=0.05 ? Incentive perversion 
=================================================================================

![Flexible analyese](./images/carp-flexible-analyses.png){ height=240px }

- Carp 2012
<!--   -->

Low Positive Predictive Value : P($H_A$ is true | test is significant) 
=================================================================================

![PPV = f(power)](./images/ppv-func-of-pwr-or-02-alph-20.png){ height=250px }

<!--   -->


A possibly quite dire situation 
=================================================================================

![Bishop, 2015](./images/harcking-hacking-bishop.png){ height=240px }
\vspace{-.2cm}
- D. Bishop 2015

<!-- strong suspicion that most studies are ...   -->


Solutions : sociological
=================================================================================
- Ban p-values  sounds a little extreme (BASP)
	- Btw: Nature editorial stated :  
	“The closer to zero the P value gets, the greater the chance the null hypothesis is false.”
\pause
- Registered Reports
	- Seems a good solution in many cases: can implement a culture shift: worth the paper work ! 
\pause
- Cobidas and reporting best practices
	- community education and publishing efforts
	- standards for easing reuse of data (INCF, BIDS)
	- Long list of checkboxes in nature publications - Cobidas
	- Nature statistician review

Solutions : Technical 
=================================================================================

- Redefine significance
\pause
- Use Bayesian framework ?
\pause
- Use Prediction framework ? 
\pause


<!-- Notes:
	- list of possible solutions : technical / social / techno-social
-->

Conclusion: Is machine learning (prediction / classification) going to save us? 
======================================================

- Yes: 
	Why ?
\pause
- No: 
	Why ?

Is machine learning (prediction / classification) going to save us? 
======================================================

![Varoquaux, 2019](./images/accuracy-prediction-sample-size.png){ height=320px }

Conclusion: rephrase reproducibility into generalizability 
======================================================

- What do I generalize on ? 
	- datasets ? 
	- software ? 
	- algorithms ? - initializations ? 
	- populations ?
	...

- Where is the biggest variation ? 

Conclusion: Ioannidis again
======================================================

* Young fields tend to have less stringent criteria 
* Ioannidis 2005: When are results more likely to be false? 
    - The smaller the studies ...
    - The smaller the effect size ...
    - The larger the number of tests ...
    - The more flexibility in the analyses
    - The more trendy ...
    - The more financial interest ...

Acknowledgements  
======================================================

* Repronim: D. Kennedy, S. Ghosh, Y. Halchenko, D. Keator, D. Jarecka, J. Grethe, M. Martone, etc...
* McGill: Peer Herholz, Lex Hutton, Celia Greenwood, Bettina Kemme, Samir Das, Shawn Brown, Alan Evans, Bratislav Misic
* Berkeley: M. D'Esposito, M. Brett, S. Van der Walt, J.Millman
* Pasteur: G. Dumas, R. Toro, T. Bourgeron, A. Beggiato
* Neurospin: B. Thirion, G. Varoquaux, V. Frouin, others
\vspace{ .5cm }
* **Hiring on reproducibility and neuroinformatics projects !**

Thank you for your attention - Questions ?
======================================================

<!--
Must contain
=======================================
- must contain: p-hacking, p-curve, pre-registration, reviewer blurb, 
- Dorothy Bishop slide


First slide 
======================================================

![\ ](./images/first-slide.png){ height=260px }
-->

<!-- Notes: 
Nope !
	- .005 will increase replicability - but will depend on power, prior,  
	- (49%) replication rate of studies with p ≤ .005 in the reproducibility project in psychology
	- We question the idea that the alpha level at which an error rate is
	  controlled should be based on the amount of relative evidence
	- H1 model dependant, BF arbitrary, H0 point null model dependant,
	  equating BF and p-value dangerous because H1 dependent
	- odds are hard to define !
	  Without stating the reference class for the “base-rate of true nulls”
	  (e.g., does this refer to all hypotheses in science, in a discipline,
	  or by a single researcher?), the concept of “prior odds that H1 is true” has
	  little meaning indicated by Bayes factors
	- may harm science: more cost, more false negative?


Computing Effect size: practice
================================

* First, compute the standard deviation of the data from the $\textrm{SDM}$ 
\pause
    - get $\sigma$ from $\textrm{SDM}$ : $\sigma = \sqrt{14-1}\times\textrm{SDM}$
    - Combine the $\sigma$ to have one estimation across the groups
        - formula easy to recompute or find
    - $\sigma = \sqrt{14-1}\times\textrm{SDM}$, $d = \frac{m_1 - m_2}{\sigma} = 1.05$ 
\pause
\vspace{.4cm}
    - What is the percentage of variance explained ? 
\pause
\vspace{.4cm}
    - Write the estimated model: $Y = [1 \ldots 1]^t [m_1-m_2] + \textrm{residual}$
    - Compute the total sum of square $Y^t Y$, then the proportion: 
\pause
\vspace{.2cm}
    - \Large{$V_e = \frac{(n_1 + n_2)(m_1-m_2)^2}{n_1 s_1^2 + n_2 s_2^2 + (n_1 + n_2)(m_1-m_2)^2} > 40\%$}



Solutions - technical - redefine significance
=================================================================================

- 70 prominent scientists worked on a google document ... 

\large{"We propose to change the default P-value threshold for
statistical significance for claims of new discoveries from 0.05 to 0.005."}

- move BF from **weak 2-3 to strong 12-26 evidence** (under many H1)

\hspace{.5cm}

\tiny{Daniel J. Benjamin 1 *, James O. Berger 2 , Magnus Johannesson 3 *, Brian A.  Nose k 4, 5 , E.  - J.  W agenma k er s 6 , Richard Ber k 7, 1 0 , K enneth A.  Bollen 8 , Björn Bremb s 9 , Lawrence Brown 10 , Colin Camerer 11 , David Cesarini 12, 13 , Christopher D. Chambers 14 , Merlise Clyde 2 , Thomas D. Cook 15,16 , Paul De Boeck 17 , Zoltan Dienes 18 , Anna Dreber 3 , Kenny Easwaran 19 , Charles Efferson 20 , Ernst Fehr 21 , Fiona Fidler 22 , Andy P.  Field 18 , Malcolm Forster 23 , Edward I. George 10 , Richard Gonzalez 24 , Steven Goodman 25 , Edwin Green 26 , Donald P.  Green 27 , Anthony Greenwald 28 , Jarrod D. Hadfield 29 , Larry V.  Hedges 30 , Leonhard Held 31 , Teck Hua Ho 32 , Herbert Hoijtink 33 , James Holland Jones 39,40 , Daniel J. Hruschka 34 , Kosuke Imai 35 , Guido I mbens 36 , John P.A.  Ioannidis 37 , Minjeong Jeon 38 , Michael Kirchler 41 , David Laibson 42 , John List 43 , Roderick Little 44 , Arthur Lupia 45 , Edouard Machery 46 , Scott E. Maxwell 47 , Michael McCarthy 48 , Don Moore 49 , Stephen L. Morgan 50 , Marcus Munafó 51, 52 , Shinichi Nakagawa 53 , Brendan Nyhan 54 , Timothy H. Parker 55 , Luis Pericchi 56 , Marco Perugini 57 , Jeff Rouder 58 , Judith Rousseau 59 , Victoria Savalei 60 , Felix D. Schönbrodt 61 , Thomas Sellke 62 , Betsy Sinclair 6 3 , Dustin Tingley 6 4 , Trisha Van Zandt 6 5 , Simine Vazire 6 6 , Dun can J. Watts 6 7 , Christopher Winship 6 8 , Robert L. Wolpert 2 , Yu Xie 69 , Cristobal Young 7 0 , Jonathan Zinman 7 1 , Valen E. Johnson 7 2 *
}


Notes: 
	* not the first effort: Seen Johnson PNAS 2013 
	* Sellke
	* you would think : at last, the community has reached a consensus !

Solutions: is it a solution, really? 
=======================================

- 88 non less prominent scientists declare that this is not a solution !

**Abstract:** In response to recommendations to redefine statistical significance
to p $\leq$ .005, we propose that researchers should transparently _report and
justify_ all choices they make when designing a study, _including the alpha
level_.
\pause

- results depend on power and prior
- results depend on H1
- priors are really hard to estimate
- may make science more costly and analyses lose sensitivity

# Original authors fight back !   
=======================================

![A solution?](./images/p-value-005-baysian-spectacles.png){ height=270px }

- Results do hold for many H1 !

Registered reports 
=======================================

\hspace{-.5cm}
\vspace{-.5cm}
![Arg1](./images/RR-against-arg1.png){ height=70px }

\pause
\hspace{-.5cm}
\vspace{-.15cm}
![Arg2](./images/RR-against-arg2.png){ height=70px }

\pause
\hspace{-.5cm}
\vspace{-.15cm}
![Sol1](./images/RR-solution-1.png){ height=70px }

Registered reports 
=======================================
\pause
\hspace{-.5cm}
\vspace{-.15cm}
![Sol2](./images/RR-solution-2.png){ height=70px }

\pause
\hspace{-.5cm}
\vspace{-.10cm}
![Sol2](./images/RR-solutionitis.png){ height=70px }

\pause
\hspace{-.5cm}
\vspace{-.10cm}
![Sol3](./images/RR-solution-3.png){ height=80px }

-->
