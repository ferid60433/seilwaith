# Infrastructure for Developing Welsh Language Speech Recognition
[click here](README.md) for the Welsh version of this page

## Introduction 
This project provides the infrastructure used by the Language Technologies Unit at Bangor University to train acoustic and language models for Welsh language speech recognition. 

All of the usual intricate steps and complexities involved in training models have been simplified and encapsulated into an easy to use Docker environment so that developers and other researcher may easily re-use and replicate.

The Docker based infrastructure provide means to:

 - download the Paldaruo speech corpus from the Welsh National Language Technologies Resources Portal. (*Paldaruo is an un-edited, crowd sourced speech corpus, see http://techiaith.cymru/corpora/paldaruo/?lang=en*)
 - sanitize, assess and analyse every contribution to the Paldaruo
 - filter best recordings for acoustic models training
 - train acoustic models with one, a subset or every person's contributions to the Paldarup corpus
 - simple methods for testing acoustic models. 
 - package acoustic models for use in Julius-cy (*see https://github.com/techiaith/julius-cy*)
 

## Getting Started...
You will need a computer with a Linux operating system such as Ubuntu or RedHat. You will need to have installed git, wget, make and Docker before hand. Start off in your home directory (i.e. $HOME)

```
~$ mkdir src
~$ cd src
~/src$ git clone --recursive https://github.com/techiaith/seilwaith.git
~/src$ cd seilwaith
```

The infrastructure uses the HTK Speech Recognition Toolkit (see http://htk.eng.cam.ac.uk/). You need to obtain its source code seperately by first registering on the HTK website for a username and password and then using: 

`$ wget --user <your HTK username> --ask-password http://htk.eng.cam.ac.uk/ftp/software/HTK-3.4.1.tar.gz`

`$ wget --user <your HTK username> --ask-password http://htk.eng.cam.ac.uk/ftp/software/HTK-samples-3.4.1.tar.gz`

You will be prompted for your password. 

Both files zip files will reside in your 'seilwaith' directrory:

```
~/src/seilwaith $ ls
Dockerfile  HTK-3.4.1.tar.gz  HTK-samples-3.4.1.tar.gz  Makefile  README.md  srdk
```

The next step for constructing the Docker environment is to simply type:

`~/src/seilwaith $ make`

This will create a base image with the built HTK tools used for the Welsh language speech recognition training. It also runs the HTK installation tests within a Docker container instance. When they have completed you will have a command prompt within the Docker container. You should simply type 'exit' at this point:

`$ exit`
 
The next step is to enter the 'srdk' sub-directory 

`~/src/seilwaith $ cd srdk`

and follow the instructions in the [README_en.md](srdk/README_en.md)

