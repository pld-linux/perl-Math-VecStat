%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	VecStat
Summary:	Math::VecStat -- some basic statistics on vectors (min,max,average,....).
Name:		perl-Math-VecStat
Version:	0.06
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides some basic statistics on numerical vectors. All
the subroutines can take a reference to the vector to be operated on. In
some cases a copy of the vector is acceptable, but is not recommended
for efficiency.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Math/VecStat.pm
%{_mandir}/man3/*
