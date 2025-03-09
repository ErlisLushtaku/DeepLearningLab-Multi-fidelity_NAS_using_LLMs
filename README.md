The paper ["Large Language Models to Enhance Bayesian Optimization" (LLAMBO)](
https://doi.org/10.48550/arXiv.2402.03921) explores the utilization of Large Language Models (LLMs) to improve the performance of Bayesian Optimization (BO) for Hyperparameter Optimization (HPO). The primary focus is on utilizing LLMs to generate better initialization points (warmstarting), to enhance surrogate modeling as well as candidate sampling. 

Building on the insights from this paper, our research aims to test the capabilities of **LLMs in Neural Architecture Search in a multi-fidelity setting**. For this purpose we use NASBench201 benchmark with CIFAR-10 dataset.

The LLAMBO codebase was adapted from its original use in HPO to focus on Neural Architecture Search (NAS).

We leveraged [Syne Tune library](https://syne-tune.readthedocs.io/en/latest/) to extend LLAMBO to work in a multi-fidelity setting by creating a custom searcher for Syne Tune and integrating it with the library's Synchronous Hyperband Scheduler. The custom searcher is used by the scheduler for warmstarting, to sample new configurations and to predict their mean performance and variance which are then used in the acquisition function."

Please check [Poster.pdf](https://github.com/ErlisLushtaku/DeepLearningLab-Multi-fidelity_NAS_using_LLMs/blob/main/Poster.pdf) for more details and the results.

To test the pipeline you can check the Jupyter Notebook [test.ipynb](https://github.com/ErlisLushtaku/DeepLearningLab-Multi-fidelity_NAS_using_LLMs/blob/main/test.ipynb).
