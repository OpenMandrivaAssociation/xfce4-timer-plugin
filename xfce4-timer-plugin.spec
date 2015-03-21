%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Timer plugin for the Xfce panel
Name:		xfce4-timer-plugin
Version:	1.6.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-timer-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-timer-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1)
BuildRequires:	perl(XML::Parser)

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
%{_datadir}/icons/hicolor/48x48/apps/xfce4-timer.png
