Summary:	Timer plugin for the Xfce panel
Name:		xfce4-timer-plugin
Version:	0.5.1
Release:	%mkrel 3
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-timer-plugin
Source0:	http://goodies.xfce.org/_media/projects/panel-plugins/%{name}-%{version}.tar.bz2
Patch1:		xfce4-timer-name.patch
Requires:	xfce-panel >= 4.3.0
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-timer-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Timer panel plugin for the Xfce Desktop Environment.

%prep
%setup -q
%patch1 -p1 -b .name

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf  %{buildroot}%{_prefix}/doc

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS TODO README
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
