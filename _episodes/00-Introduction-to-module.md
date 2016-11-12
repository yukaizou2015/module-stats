---
title: "An introduction to the Statistics in reproducibility module"
teaching: A fair bit of time.   
exercises: As many as possible. 
questions:
- "Who is this modulde for ?"
- "How can I get some help if I get stuck on solving for an exercise or a question ?"
- "How can I validate this module ?"
- "When and where are the future ReproNim training workshops ?"


objectives:
- "Teach (non statistician / applied math) neuroimagers about the statistical aspects of reproducibility "
- "Make this a collaborative enterprise: you can improve this module if you know how to do a pull request, which is taught to you in module 'the informatics basics of reproducibility (module 0)"
- "This module should give you a critical eye on most of the current literature and the knowledge to do solid work"


keypoints:
- This is in line with our overall goal of making science (including scientific training) more open.

---


### What is a ReproNim module ? 

A ReproNim module is a set of "steps" or "episodes", in which we have gathered material on the web to guide you through the acquisition of a concept or tool or technique. You will take this journey and for each episode, we try to then ask you a few questions or do some exercise so that you will have an idea of how much you feel comfortable with the material to be acquired. We are not providing the answers directly on this web site so that this can be taken as a real course, but we will be teaching workshops with the answers and we will have links to the answers.

### Who is this module for? 

The module is for you, if you are not a statistician or an applied mathematic researcher or student, is working with neuroimaging and you want to know about the statistical aspects of reproducibility.

### How much time this should take me? 

That really depends on your familiarity with statistical concepts and your capacity to play with a few formulas and some code. If you have no familiarity at all, this may take you a long time, for instance 5 to 7 full days. If you have good familiarity, some of the information will be already partially known and it may take you a full day to go in detail through this material.

### What are the episodes for this module? 

1. Statistical basis for reproducible neuroimaging
2. Effect sizes and effect sizes variation
3. Statistical power in neuroimaging and Statistical reproducibility: Positive predictive values
4. P-hacking "How *not* To"
5. Meta analyses in neuroimaging
6. Statistical methods in available software
7. Machine learning and prediction
8. Culture and ethical aspects: last but certainly not least. 

[//]: # Will I be done in 3 days ? No.
<!---
1.
2.
3.
4.
5.
6.
7.
8.
9.
--->

### Do I need to code ?  What language ? 

You can learn a lot without coding, but you will have the full benefice if you do code. So, yes, you should code. We have (mostly) adopted python for the language, it may not be your first choice but we think some knowledge of python coding will help you anyways. We will try to help as much as possible by providing tutorials, examples, and links to installation instructions.

### ReproNim is truly *open*

The ReproNim training events can only accommodate a limited number of participants.
Nevertheless, we are committed to openness and we are committed to providing our
materials in an open format, with liberal licenses, and through a publicly accessible website.
There are time to time an article we want you to read and is behind paywall. If your institution or university does not give you access to it, let us know and we can provide a private copy for your personal use.


~~~
import nibabel as nib
img = nib.load('my_file.nii.gz')
affine = img.affine
~~~
{: .python}


And this is our logo :

No logo !

<p><img src="https://raw.githubusercontent.com/ReproNim/artwork/master/logo/repronim-logo3.2_nobg_256x256.png" alt="our great logo should be seen in html" /></p>

<!---
<img src="https://github.com/ReproNim/artwork/blob/master/logo/repronim-logo3.2_nobg_256x256.png" alt="our great logo" >

![an image]({{site.root}}/fig/repronim-logo3.svg)
--->


> ### Exercises and challenges (click on the arrow to the right to open)
>
>  Boxes with "challenges" will be interleaved with the lesson materials.
>    - This helps participants stay engaged.
>    - It surfaces questions that learners have as they go along.
>    - It breaks up the instruction, providing a bit of a diversion.
>    - It gives people a chance to engage in peer instruction, which is
>    - It is [known to help learning](https://en.wikipedia.org/wiki/Peer_instruction).
{: .challenge}


> ### Callouts
> We sometimes will have box with a "callout", for extra material that is "optional".
{: .callout}
