Summary:	Timer plugin for the Xfce panel
Name:		xfce-timer-plugin
Version:	0.5.1
Release:	%mkrel 1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-timer-plugin
Source0:	http://goodies.xfce.org/_media/projects/panel-plugins/xfce4-timer-plugin-%{version}.tar.bz2
Patch1:		xfce4-timer-name.patch
Requires:	xfce-panel >= 4.3.0
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Timer panel plugin for the Xfce Desktop Environment.

%prep
%setup -qn xfce4-timer-plugin-%{version}
%patch1 -p1 -b .name

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf  %{buildroot}%{_prefix}/doc

%find_lang xfce4-timer-plugin

%clean
rm -rf %{buildroot}

%files -f xfce4-timer-plugin.lang
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS TODO
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
