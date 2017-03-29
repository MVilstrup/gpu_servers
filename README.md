# Usage
## Start
In order to setup the servers one first has to run the command:
ansible-playbook start.yml
This starts the amount of servers specified in the ec2.yml file in the vars folder.
Ansible has some problems with python if the Anaconda package is used. In order to
get around these issues one can add the explicit location of the python interpreter
as an argument when running the command.
ansible-playbook start.yml --extra-vars "ansible_python_interpreter=/Path/To/Python/interpreter"

The IP-addresses of all the servers are written in the file named "ips"

## Setup
With all the servers started. The command:
ansible-playbook -i hosts setup.yml
Will setup and install Jupyter and the most common python packages used with it
along side several deep learning frameworks. This takes some time, since it has to
download CUDA.

## Termination
When the servers are no longer needed, 
ansible-playbook terminate.yml --extra-vars "ansible_python_interpreter=/Path/To/Python/interpreter"

## Regions


## Instance types
### Mini types
|    Type     |  CPU AMOUNT   | GPU  AMOUNT  | Memory (Gb)  |
 ------------ | :-----------: | -----------: | -----------: |
t2.nano       |    1          |       0      |  0,5         |
t2.micro	    |   1	          |       0      |  1           |
t2.small      |  1            |       0      |  2           |
t2.medium     |  2            |       0      |  4           |


Modèle GPU

vCPU

Mém. (Gio)

Mémoire GPU (Gio)

p2.xlarge

1

4

61

12

p2.8xlarge

8

32

488

96

p2.16xlarge

16

64

732

192
