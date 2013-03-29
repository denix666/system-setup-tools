system-setup-tools
==================

system-setup-tools - is a set of the scripts to easy setup, installation and configuration of various server services and daemons, desktop components, applications and utilities.

**List of scripts:**
- `system-setup-autologin` (Setup MDM autologin to system without password)
- `system-setup-dhcpd` (Setup DHCP server)
- `system-setup-dovecot` (Setup IMAP server)
- `system-setup-http` (Setup apachee server)
- `system-setup-jabber` (Install ejabberd XMPP server)
- `system-setup-java` (Install Oracle JRE)
- `system-setup-ltsp` (Install linux terminal server)
- `system-setup-mysql` (Setup MYSQL server)
- `system-setup-named` (Setup DNS server)
- `system-setup-openvpn` (Setup OpenVPN server)
- `system-setup-pptpd` (Setup PPTP server)
- `system-setup-proftpd` (Setup FTP server)
- `system-setup-samba` (Setup samba server)
- `system-setup-squirellmail` (Install squirellmail web interface)
- `system-setup-tftpd` (Setup TFTP boot server)
- `system-setup-virtualhost` (Add virtual host to apachee configuration)


Installation
============

**From yum repository:**

Fedora `17,18` - install the denix-x repo:

```vim
#rpm -ivh http://fedora.os.vc/yum/base/x1/i386/denix-x-repo-xx.x-xx.x1.noarch.rpm
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
