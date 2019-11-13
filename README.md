### Build the Gradescope grader

This is a grader for [Gradescope Autograder](https://gradescope-autograders.readthedocs.io/en/latest/). 
However, it is not for grading a specific assignment but a bridging grader
for running any made-for-Autolab grader.
Here is a [very brief introduction](https://github.com/xyzisinus/grader4AutolabProjectNeedingVM/blob/master/README.md) to Autolab.

This grader is particularly designed to work with `grader.py` in 
the [grader4AutolabProjectNeedingVM](https://github.com/xyzisinus/grader4AutolabProjectNeedingVM) repository.
`grader.py` runs any Autolab grader on a VM in the AWS cloud.  Please see 
the [README](https://github.com/xyzisinus/grader4AutolabProjectNeedingVM/blob/master/README.md) to understand how it works.

In this repository, the files for building the Gradescope grader are under the `source` directory:
```
source/grader.py  # copied from grader4AutolabProjectNeedingVM repository
source/config_defaults.yaml  # copied from grader4AutolabProjectNeedingVM repository
source/setup.sh
source/run_autograder
source/parseResults.py  # parse Autolab's output into Gradescope's results.json

source/Autolab_grader/autograde.tar  # Autolab grader for the specific assignment
source/Autolab_grader/Makefile  # Autolab grader's top Makefile
source/Autolab_grader/config.yaml  # explained in grader4AutolabProjectNeedingVM's README
source/Autolab_grader/aws-ssh-key.pem  # ssh key file for Autolab compatible grading VM
```
The files directly under `source` form a Gradescope grader. 
The files under `source/Autolab_grader` are specific for a Autolab project grader.
Together they are packaged into a `autograder.zip` file and uploaded to Gradescope:
```
cd source
zip -r <upload dir>/autograder.zip *
```
In Gradescope's grading container, the `run_autograder` script executes `grader.py` which creates an AWS VM, runs the
Autolab grader on the VM and copies the output file from the VM.  `run_autograder` then executes `parseResults.py` to
convert the scores in the output file to the format of `results.json`.  It also puts the content of 
the output file (maybe trimmed to fit Gradescope's output size limit) as the `output` property of
`results.json`. A couple of screenshots of Gradescope's results page can be found at the end of this README.

### Debug the grader

Suppose you are teaching staff porting your made-for-Autolab grader to Gradescope using this repository.
To test you grader, you can upload `autograder.zip` and test it using Gradescope's `Debug via SSH` feature.
For quick testing cycles you can also use this repository's docker files to build a Docker container that mimicks Gradescope's grading container:
```
mkdir /var/run/GradescopeGrader  # mounted inside the container as its data directory
cd <top of this repository>
mkdir submission
cp <student submission file> submission  # or "git clone <student submission repo> submission"
docker-compose build
docker-compose up
```
Then the grading progress can be monitored by watching the files, `grader.log`, `output`, and `results.json` under `/var/run/GradescopeGrader` on the host machine.  With that, much of trouble-shooting can be accomplished without having to dive into the container.

To help understand the file hierarchy in Gradescope's grading container, the files under /autograder in the container are kept
in this repository under `autograder`.  It reflects the post execution state of `run_autograder` for Demo Programming Assignment, Gradescope demo course 202.

### Screenshots of grading results

##### Top of the page

![Top of the page](https://github.com/xyzisinus/GradescopeGrader4Autolab/blob/master/screenshots/topOfResultsPage.png)

##### Middle of the page

![Middle of the page](https://github.com/xyzisinus/GradescopeGrader4Autolab/blob/master/screenshots/middleOfResultsPage.png)

##### Bottom of the page

![Bottom of the page](https://github.com/xyzisinus/GradescopeGrader4Autolab/blob/master/screenshots/bottomOfResultsPage.png)
