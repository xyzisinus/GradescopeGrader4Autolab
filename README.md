This is a grader for [Gradescope Autograder](https://gradescope-autograders.readthedocs.io/en/latest/). 
However, it is not for grading a specific assignment but
for running any made-for-Autolab grader.
Here is a [very brief introduction](https://github.com/xyzisinus/grader4AutolabProjectNeedingVM/blob/master/README.md) to Autolab.

This grader is particularly designed to work with grader.py in 
the [grader4AutolabProjectNeedingVM](https://github.com/xyzisinus/grader4AutolabProjectNeedingVM) repository.
grader.py runs any Autolab grader on a VM in the AWS cloud.  Please read 
the [README](https://github.com/xyzisinus/grader4AutolabProjectNeedingVM/blob/master/README.md) to understand how it works.

To use grader.py, do the following standing at the top directory of this repository.
```
cp <grader4AutolabProjectNeedingVM>/grader.py source
cp <grader4AutolabProjectNeedingVM>/config_defaults.yaml source
```
