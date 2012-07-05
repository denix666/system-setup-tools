Name:		system-setup-tools
Version:	18.4
Release:	3%{?dist}
Summary:	Setup scripts by -=DeN=-
Group:		Scripts
License:	GPL
URL:		http://os.vc
Requires:	usermode denix-colors
Source0:        %{name}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

%description
Configuration scripts for DeniX systems.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
cp -r %{_builddir}/%{name} %{buildroot}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}

%files
%defattr(-,root,root,-)

%attr(0755,root,root) /usr/share/system-setup-tools/system-setup-dhcpd
%attr(0755,root,root) /usr/bin/system-setup-dhcpd
%attr(0644,root,root) /etc/pam.d/system-setup-dhcpd
%attr(0644,root,root) /etc/security/console.apps/system-setup-dhcpd

%attr(0755,root,root) /usr/share/system-setup-tools/system-setup-httpd
%attr(0755,root,root) /usr/bin/system-setup-httpd
%attr(0644,root,root) /etc/pam.d/system-setup-httpd
%attr(0644,root,root) /etc/security/console.apps/system-setup-httpd

%attr(0755,root,root) /usr/share/system-setup-tools/system-setup-java
%attr(0755,root,root) /usr/bin/system-setup-java
%attr(0644,root,root) /etc/pam.d/system-setup-java
%attr(0644,root,root) /etc/security/console.apps/system-setup-java

%attr(0755,root,root) /usr/share/system-setup-tools/system-setup-mysql
%attr(0755,root,root) /usr/bin/system-setup-mysql
%attr(0644,root,root) /etc/pam.d/system-setup-mysql
%attr(0644,root,root) /etc/security/console.apps/system-setup-mysql

%attr(0755,root,root) /usr/share/system-setup-tools/system-setup-named
%attr(0755,root,root) /usr/bin/system-setup-named
%attr(0644,root,root) /etc/pam.d/system-setup-named
%attr(0644,root,root) /etc/security/console.apps/system-setup-named

%attr(0755,root,root) /usr/share/system-setup-tools/system-setup-pptpd
%attr(0755,root,root) /usr/bin/system-setup-pptpd
%attr(0644,root,root) /etc/pam.d/system-setup-pptpd
%attr(0644,root,root) /etc/security/console.apps/system-setup-pptpd

%attr(0755,root,root) /usr/share/system-setup-tools/system-setup-proftpd
%attr(0755,root,root) /usr/bin/system-setup-proftpd
%attr(0644,root,root) /etc/pam.d/system-setup-proftpd
%attr(0644,root,root) /etc/security/console.apps/system-setup-proftpd

%attr(0755,root,root) /usr/share/system-setup-tools/system-setup-samba
%attr(0755,root,root) /usr/bin/system-setup-samba
%attr(0644,root,root) /etc/pam.d/system-setup-samba
%attr(0644,root,root) /etc/security/console.apps/system-setup-samba

%attr(0755,root,root) /usr/share/system-setup-tools/system-setup-squirrelmail
%attr(0755,root,root) /usr/bin/system-setup-squirrelmail
%attr(0644,root,root) /etc/pam.d/system-setup-squirrelmail
%attr(0644,root,root) /etc/security/console.apps/system-setup-squirrelmail

%attr(0755,root,root) /usr/share/system-setup-tools/system-setup-tftpd
%attr(0755,root,root) /usr/bin/system-setup-tftpd
%attr(0644,root,root) /etc/pam.d/system-setup-tftpd
%attr(0644,root,root) /etc/security/console.apps/system-setup-tftpd

%attr(0755,root,root) /usr/share/system-setup-tools/system-setup-virtualhost
%attr(0755,root,root) /usr/bin/system-setup-virtualhost
%attr(0644,root,root) /etc/pam.d/system-setup-virtualhost
%attr(0644,root,root) /etc/security/console.apps/system-setup-virtualhost

%attr(0755,root,root) /usr/share/system-setup-tools/system-setup-vpnpeer
%attr(0755,root,root) /usr/bin/system-setup-vpnpeer
%attr(0644,root,root) /etc/pam.d/system-setup-vpnpeer
%attr(0644,root,root) /etc/security/console.apps/system-setup-vpnpeer
