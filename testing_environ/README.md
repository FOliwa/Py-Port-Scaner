# Testing Environ
Set up a test VM for your network port scanner using a popular Vagrant box based on Ubuntu

Remember, it's crucial to only test on systems and networks that you have explicit permission to access and scan. Unauthorized scanning can be considered malicious and can cause legal issues.


# Vagrant cheat sheet

- `vagrant up` - starts vagrant environment (also provisions only on the FIRST vagrant up)
- `vagrant status` - outputs status of the vagrant machine
- `vagrant ssh <boxname>` - connects to machine via SSH
- `vagrant halt` - stops the vagrant machine
- `vagrant global-status` - outputs status of the all vagrant machines runing on the host
- `vagrant halt <vm_id>` - as above but in case you are in other directory 
