%define		_plugin	username
%define		mversion	1.0.0
Summary:	Plugin to show current username
Summary(pl):	Wtyczka wy�wietlaj�ca nazw� u�ytkownika
Name:		squirrelmail-plugin-%{_plugin}
Version:	2.3
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	c81670f5607835dc1e226653cf5c53b1
URL:		http://www.squirrelmail.org/
Requires:	squirrelmail >= 1.4.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}
%define		_sysconfdir	/etc/webapps/squirrelmail

%description
Plugin that shows current username above or below folder list and/or
as Message of the Day.

%description -l pl
Wtyczka wy�wietlaj�ca aktualn� nazw� u�ytkownika nad lub pod list�
folder�w i/lub jak Wiadomo�� Dnia.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir} $RPM_BUILD_ROOT%{_sysconfdir}

install *.php $RPM_BUILD_ROOT%{_plugindir}
mv config.php.sample $RPM_BUILD_ROOT%{_sysconfdir}/%{_plugin}_config.php
ln -s %{_sysconfdir}/%{_plugin}_config.php $RPM_BUILD_ROOT%{_plugindir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{_plugin}_config.php
%dir %{_plugindir}
%{_plugindir}/*.php