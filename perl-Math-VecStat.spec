%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	VecStat
Summary:	Math::VecStat - some basic statistics on vectors (min,max,average,...)
Summary(pl):	Math::VecStat - podstawowe statystyki na wektorach (min,max,¶rednia,...)
Name:		perl-Math-VecStat
Version:	0.08
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3df23fb451f73bb49fd4ea344ba94020
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides some basic statistics on numerical vectors. All
the subroutines can take a reference to the vector to be operated on.
In some cases a copy of the vector is acceptable, but is not
recommended for efficiency.

%description -l pl
Ten pakiet dostarcza kilku podstawowych statystyk na wektorach
liczbowych. Wszystkie funkcje mog± przyj±æ referencjê do wektora, na
którym maj± operowaæ. W niektóych przypadkach kopia wektora jest
akceptowalna, ale nie jest to zalecane ze wzglêdu na wydajno¶æ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/VecStat.pm
%{_mandir}/man3/*
