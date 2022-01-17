# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: 25 minutes

### Prerequisites:
- A verified DigitalOcean account
### Create a Droplet
1. Create a Droplet with minimum storage and no extra features. It should cost $5/month.
2. Run `ssh key-gen` to create a key pair or use an existing ssh key.
3. Copy the contents of the public key. Paste it in the appropriate box.
4. Run `ssh root@<dropletipaddress>`. If it succeeds, well done. If not, try again.
### Disable sshing into root account
1. Log into the root account using ssh: `ssh root@<dropletipaddress>`
2. Create a new user: `adduser <username>`
3. Set a password. No other information is needed.
4. Give the user sudo privileges: `usermod -aG sudo <username>`
5. Allow SSH connections through the firewall: `ufw allow OpenSSH`
6. Enable the firewall: `ufw enable`
7. Copy the key from the root account to the new user account: `rsync --archive --chown=<username>:<username> ~/.ssh /home/<username>`
8. Check that the user account works properly: `ssh <username>@<dropletipaddress>`. Log into the root account once more.
9. Open the sshd_config file (located in /etc/ssh)
10. Find the line that says  `PermitRootLogin yes`. Change to `PermitRootLogin no`.
11. Restart ssh: `sudo service ssh restart`
12. You should now be unable to log into the root account.

### Set up Apache2
1. Install Apache2 using `sudo apt install apache2`.
2. Check the list of UFW application profiles using `sudo ufw app list`.
3. Allow traffic on port 80 using the Apache profile: `sudo ufw allow in "Apache"`
4. Check to see everything works on terminal by typing `sudo ufw status`. Note the firewall need to be enabled for this to work.
5. Test on browser by going to `http://<dropletipaddress>`. The default Apache page should show up.

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04
* https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
* https://www.digitalocean.com/community/questions/how-can-i-disable-ssh-login-for-a-root-user-i-am-the-account-owner
---

Accurate as of (last update): 2022-01-16

#### Contributors:  
Michael Borczuk, pd2  
Yuqing Wu, pd2  
