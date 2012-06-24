%include	/usr/lib/rpm/macros.perl
Summary:	Math-VecStat perl module
Summary(pl):	Modu� perla Math-VecStat
Name:		perl-Math-VecStat
Version:	0.04
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Math-VecStat-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-VecStat perl module.

%description -l pl
Modu� perla Math-VecStat.

%prep
%setup -q -n Math-VecStat-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT


gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Math/VecStat.pm
%{perl_sitearch}/auto/Math/VecStat

%{_mandir}/man3/*
