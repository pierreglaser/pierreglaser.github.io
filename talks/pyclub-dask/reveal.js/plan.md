# Who am I?
- A Gatsby first-year PhD student working on generative models and kernel methods
- Previous job: improving the performance of scientific computing in Python in a distributed setting
- Exposition to computational neuroscience: part of the Parietal INRIA team, that constructs numerical methods for neuroimaging data analysis.


# What is this talk about:

- I am going to present dask, a dynamic task scheduler written in Python
- Dask aims at porting both:
	  1. the python scientific ecosystem
	  2. programming workflows
  from a single core/machine to a distributed environments.
- 2 has been advertised in the abstract, and is something I use every time I want to run experiments. 1 is aimed at showing that dask can theoretically be used to scale up any piece of scientific software. I wanted this presentation to be conceptual, partly becasue I know very little about computational neuroscience and its software ecosystem outside of neuroimaging: instead of zooming in a specific use case, I'd also be happy if everyone of you had a high level understanding of why is distributed computing both complex and relevant to many scientists.

# Disclaimer
- This talk is an attempt of mine at describing a tool (that I use), and that you **may** find a use for too.
- I will not compare it to alternatives
- I will not argue whether or not jupyter notebooks is the right way to play with data.
- Everyone has their own use cases and problem characteristics: this talk
  attempt to make you adopt workflow X/library Y/language Z.


# Python

Python is a very unique programming language, that took over both scientific computing, and some of more traditional web and application programming:

## Examples of scientific projects

  - mars helicopter
  - black hole mission
  - reddit, youtube... software sucess is partly a reason of why python was the
    ground for so many distributed frameworks applications.


## Why is that so?

  - C-extensability enables bare-metal performance
  - Incredibly polyvalent: for instance, initial community is very networking-savvy. No apparent link with scientific computing initially: but distributed computing changed the game...
  - Ideal for data exploration, thanks its interpreted nature, and its REPL-style interfaces.
  - This potential was fully exploited thanks to many third party libraries building ON TOP of the Python standard library. Various layers of that, see picture.


## 21st century challenges

  1. Amount/size of data is drastically increasing: (-> need for out of core computations)
  2. Computing resources are expanding their capacity, often via computing
     clusters (not monolithic supercomputers, instead of network standard ones that can communicate with each other.
  3. Such situations are not addressed by the main Python scientific computing packages such as numpy and scipy.


# Out of core computations using Dask
  1. Dask is a dynamic task scheduler, used to drop-in replacements of python libraries that support out of core computations




- In theory, any python library could be parallelized using dask:

- task scheduling is both generic and crucial:
- Downstream usages of dask are already numerous, and theoretically

- tools that I use as part of my workflow as a
  scientist,
  as well as explain in which other contexts they can be used.
- "My workflow" is based on the jupyter environment, whose pros and cons I will not discuss.
- I know little about neuroscience and its softwae ecosystem:
