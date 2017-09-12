# Structure
The code is structured into two parts. The basis setup and the notebook setup. The basis setup is used to create a server with the basic tools installed such as CuDNN and Cuda. This can then be used as an Image in the notebook_setup. The notebook_setup is used to quickly setup configured servers with the newest code from github.

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
