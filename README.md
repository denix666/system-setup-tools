system-setup-tools
==================

system-setup-tools - is a set of the scripts to easy setup, installation and configuration of various server services and daemons, desktop components, applications and utilities.

**List of scripts:**
- system-setup-dhcp
- system-setup-http
- system-setup-java
- system-setup-mysql
- system-setup-named
- system-setup-pptpd
- system-setup-proftpd
- system-setup-samba
- system-setup-squirellmail
- system-setup-tftpd
- system-setup-virtualhost
- system-setup-vpnpeer


Installation
============

**From yum repository:**

Fedora `16,17` - install the denix-x repo:

```vim
#rpm -ivh http://fedora.os.vc/yum/base/x1/i386/denix-repo-1.1-2.x1.noarch.rpm
```
and then install the package as regular:

```vim
#yum install system-setup-tools
```


**Manual RPM installation:**

If you want to install this package manualy, download the latest version from one of my mirrors:

http://mirror.os.vc/denix-repo/yum/base/x1

and install it by using this command as root:

```vim
#rpm -ivh system-setup-tools.xx.x-xx.x1.noarch.rpm
```


**Howto build RPM from source:**

Clone my git repository and run the build script:

```vim
$mkdir git-repos
$cd git-repos
$git clone https://github.com/denix666/system-setup-tools.git
$cd system-setup-tools
$./build_system-setup-tools.sh
```
