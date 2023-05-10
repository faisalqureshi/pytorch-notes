# lessons-pytorch

This is a collection of PyTorch notebooks that sets the stage for using PyTorch for deep learning development.  The web is full of excellent material on all things PyTorch.  I have tried to provide a link to the source material where warranted.

For questions please contact faisal.qureshi@ontariotechu.ca

## Setup (Using a local Windows box)

If you must, you can use a Windows machine to work on ML projects.  At some point, however, you will have to train and run models on a linux machine --- most GPU servers run linux-variants.

In order to use a Windows machine, obviously you'll need to install Python.  You have a couple of options: 1) install Python via [www.python.org](www.python.org), 2) install Python via Microsoft App Store, or 3) get [Anaconda](https://www.anaconda.com/) python distribution.  I have tried all these approaches, and I find that option (2) works better, especially if you also want to install [PyGame](https://www.pygame.org/news) package.  PyGame requires [SDL](https://www.libsdl.org/) libraries and I couldn't make it work when I install Python via option (1) above.  PyGame also didn't work with option (3).  Also, since I also use linux environments, I prefer to still use virtualenv and pip to manage my Python environments.  Hence I stick with option (2).

Obviously, I assume that we are dealing with a souped up Windows box, i.e., at least a gaming class machine that has NVIDIA GPU.

Okay, so now that you have installed Python, you will need to install the various Python packages, e.g., numpy, scipy, pytorch, etc.  As I mentioned earlier,  I prefer to use virtualenv and pip to manage my Python environments.  I also want to interact with Python via commandline.  On windows, I install [MSys2](https://www.msys2.org/), which provides me with a unix-like experience on Windows.  

Let's assume that the system ready for use.  Python is installed.  The relevant packages are also installed.  You can for example check if pytroch is is available as follows:

~~~
$ python
Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.is_available()
True
>>>
~~~

### Important (an issue with jupyter lab)

I often use `jupyter lab`.  I noticed that for windows jupyter lab only works if the command is executed on the same drive.  See below.  Here Python is installed on C drive and `jupyter lab` command is only available on C drive.

~~~
(ml) lamb :: ~ > pwd
/home/fzuba
(ml) lamb :: ~ > jupyter lab
[I 2023-05-10 09:22:48.231 ServerApp] jupyter_server_terminals | extension was successfully linked.
~~~

`jupyter lab` command is not available on D drive

~~~
(ml) lamb :: Dropbox/gits-on-desktop > pwd
/d/faisal/Dropbox/gits-on-desktop
(ml) lamb :: Dropbox/gits-on-desktop > jupyter notebook
zsh: command not found: jupyter
~~~

Now when the `jupyter lab` is executed on C drive, it is unable to access files on the D drive.  We can resolve this by specifying the drive at start time. 

~~~
(ml) lamb :: ~ > pwd
/home/fzuba
(ml) lamb :: ~ > jupyter lab --notebook-dir=D:/
[I 2023-05-10 09:25:43.836 ServerApp] jupyter_server_terminals | extension was successfully linked.
~~~

## Setup (Using Docker on a Linux machine)

Contains docker files needed to set up your system to run the lesson notebooks.

~~~
$ cd setup
~~~

If you have made any changes to the Dockerfile or requirements.txt files, or if you want to build the image for the very first time

~~~
$ docker-compose build
~~~

Now that the image is ready, we will create a container and attach it to the image.
The following will create/attach container "charlie_1".  Check out `docker-compose.yml` file for more information.

~~~
$ ./container-run.sh 
WARNING: Found orphan containers (setup_rr_1) for this project. If you removed or renamed this service in your compos
e file, you can run this command with the --remove-orphans flag to clean it up.
Starting charlie_1 ... done
Attaching to charlie_1
groups: cannot find name for group ID 1000
~~~

Now start the jupyter notebook server.  This will be bound to `localhost:8888`

~~~
$ ./container-jupyer.sh
~~~

Next, access the jupyter notebook from your desktop using SSH tunneling.  This assumes that the notebook is running on panther and that you have set up the .ssh config file appropriately.  The following maps localhost:8888 to remote host 11945 port.  You'll notice that within `docker-compose.yml` file port 8888 of container is mapped to port 11945 of host (which acts as remote below).

~~~
$ ssh panther -NL 8888:localhost:11945
~~~

We can now access the jupyter lab by going to `http://localhost:8888`.

## Lesson contents

### Lesson 1

- PyTorch basics
- Tensor visualization
- Solving system of linear equations

### Lesson 2

- Line fitting
- Linear regression
- Classification via logisitic regression

### Lesson 3

- Regression and classification with neural networks with 1 hidden layer

### Lesson 4

- Splitting datasets

### Lesson 5

- Mixture of Gaussians
- Vectorized computation using Einstein sum notation

### Lesson 6

- CIFAR10 classification using AlexNet

### Lesson 7

- Autoencoder
- Convolutional autoencoder
- Variational autoencoder

### Lesson 8

- Work in progress (stay tuned)




