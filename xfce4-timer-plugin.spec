%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Timer plugin for the Xfce panel
Name:		xfce4-timer-plugin
Version:	1.0.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-timer-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-timer-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	pkgconfig(libxfcegui4-1.0)
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


%changelog
* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.4-1
+ Revision: 791185
- fix file list
- update to new version 0.6.4
- spec file clean

* Tue Jun 28 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-1
+ Revision: 687930
- update to new version 0.6.2

  + Matthew Dawkins <mattydaw@mandriva.org>
    - added missing BR

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.1-4mdv2010.1
+ Revision: 543441
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.6.1-3mdv2010.0
+ Revision: 446152
- rebuild

* Fri Mar 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.1-2mdv2009.1
+ Revision: 349482
- rebuild for xfce-4.6.0

* Fri Nov 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.1-1mdv2009.1
+ Revision: 305526
- update to new version 0.6.1
- fix url for source
- drop patch 1, useless imho

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6-5mdv2009.1
+ Revision: 295031
- rebuild for new Xfce4.6 beta1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.6-3mdv2009.0
+ Revision: 256984
- rebuild

* Wed Dec 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6-1mdv2008.1
+ Revision: 137828
- new version
- new license policy

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-3mdv2008.1
+ Revision: 110141
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING file
- add README file to the docs
- use upstream name
- spec file clean

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-1mdv2008.0
+ Revision: 30439
- update url
- spec file clean
- new version

