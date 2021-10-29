# lessons-pytorch

This is a collection of PyTorch notebooks that sets the stage for using PyTorch for deep learning development.  The web is full of excellent material on all things PyTorch.  I have tried to provide a link to the source material where warranted.

For questions please contact faisal.qureshi@ontariotechu.ca

## Setup

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




