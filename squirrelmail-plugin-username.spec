#
# Conditional build:
%bcond_with	admin_only	# disallow users changing plugin options
#
%define		_plugin	username
%define		mversion	1.0.0
Summary:	Plugin to show current username
Summary(pl.UTF-8):	Wtyczka wyświetlająca nazwę użytkownika
Name:		squirrelmail-plugin-%{_plugin}
Version:	2.3
Release:	3
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	c81670f5607835dc1e226653cf5c53b1
Patch0:		%{name}-admin_only.patch
Patch1:		%{name}-locale_support.patch
URL:		http://www.squirrelmail.org/plugin_view.php?id=35
Requires:	squirrelmail >= 1.4.6-2
Requires:	squirrelmail-compatibility >= 2.0.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}
%define		_sysconfdir	/etc/webapps/squirrelmail

%description
Plugin that shows current username above or below folder list and/or
as Message of the Day.

%description -l pl.UTF-8
Wtyczka wyświetlająca aktualną nazwę użytkownika nad lub pod listą
folderów i/lub jak Wiadomość Dnia.

%prep
%setup -q -n %{_plugin}
%{?with_admin_only:%patch0 -p1}
%patch1 -p0

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
