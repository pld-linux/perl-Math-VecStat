%include	/usr/lib/rpm/macros.perl
Summary:	Math-VecStat perl module
Summary(pl):	Modu³ perla Math-VecStat
Name:		perl-Math-VecStat
Version:	0.05
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Math-VecStat-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-VecStat perl module.

%description -l pl
Modu³ perla Math-VecStat.

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
%doc *.gz
%{perl_sitelib}/Math/VecStat.pm
%{_mandir}/man3/*
