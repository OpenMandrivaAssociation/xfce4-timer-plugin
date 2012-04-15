%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Timer plugin for the Xfce panel
Name:		xfce4-timer-plugin
Version:	0.6.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-timer-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-timer-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	libxfcegui4-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-timer-plugin

%description
Timer panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -rf  %{buildroot}%{_prefix}/doc

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc ChangeLog AUTHORS TODO README
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
