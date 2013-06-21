%define module Math-BaseCalc
%define upstream_version 1.016
Summary:	%{module} perl module
Name:		perl-%{module}
Version:	%perl_convert_version 1.016
Release:	1
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.cpan.org:21/pub/CPAN/modules/by-module/Math/Math-BaseCalc-1.016.tar.gz
URL:		http://search.cpan.org/dist/%{module}
Requires:	perl >= 5.0
Buildrequires:	perl-devel
Buildarch:	noarch

%description
This module facilitates the conversion of numbers between various
number bases.  You may define your own digit sets, or use any of
several predefined digit sets.

%prep
%setup -q -n %{module}-%{upstream_version}

%build

CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%make PREFIX=%buildroot%{_prefix} install DESTDIR=%buildroot

%files 
%doc Changes MANIFEST
%{perl_vendorlib}/Math/*
%{_mandir}/*/*



%changelog
* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.016-1mdv2011.0
+ Revision: 674665
- update to new version 1.016

* Sun Mar 06 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.014-1
+ Revision: 642234
- new version
- add missing %%check section
- fix buildroot
- use macros (%%make)
- use tar.gz given by upstream

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.013-2mdv2011.0
+ Revision: 440611
- rebuild

* Sun Jan 18 2009 Jérôme Quelin <jquelin@mandriva.org> 1.013-1mdv2009.1
+ Revision: 330873
- update to new version 1.013

* Fri Jun 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.012-1mdv2009.0
+ Revision: 229474
- update to new version 1.012

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.011-8mdv2008.0
+ Revision: 86552
- rebuild


* Thu May 11 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.011-7mdk
- Fix Build
- Fix Source URL
- Fix URL
- use mkrel

* Mon Jun 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.011-6mdk
- rebuild for new Perl

* Tue Aug 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.011-5mdk
- rebuild

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.011-4mdk
- rebuild for new auto{prov,req}



