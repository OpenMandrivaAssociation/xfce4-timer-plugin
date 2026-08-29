%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	Timer plugin for the Xfce panel
Name:		xfce4-timer-plugin
Version:	1.8.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-timer-plugin
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-timer-plugin/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	meson
BuildRequires:	make
BuildRequires:  intltool
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Timer panel plugin for the Xfce Desktop Environment.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

rm -rf  %{buildroot}%{_prefix}/doc

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS README*
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/apps/xfce4-timer-plugin.*
