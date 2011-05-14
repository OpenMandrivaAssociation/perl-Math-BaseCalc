%define module Math-BaseCalc
%define version 1.016
%define release %mkrel 1

Summary:	%{module} perl module
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Math/%{module}-%{version}.tar.gz
URL:		http://search.cpan.org/dist/%{module}
Requires:	perl >= 5.0
Buildrequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Buildarch:	noarch

%description
This module facilitates the conversion of numbers between various
number bases.  You may define your own digit sets, or use any of
several predefined digit sets.

%prep
%setup -q -n %{module}-%{version}

%build

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot

%make PREFIX=%buildroot%{_prefix} install DESTDIR=%buildroot

%clean
rm -rf %buildroot

%files 
%defattr(-,root,root)
%doc Changes MANIFEST
%{perl_vendorlib}/Math/*
%{_mandir}/*/*

