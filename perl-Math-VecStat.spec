#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	VecStat
%include	/usr/lib/rpm/macros.perl
Summary:	Math::VecStat - some basic statistics on vectors (min,max,average,...)
Summary(pl.UTF-8):	Math::VecStat - podstawowe statystyki na wektorach (min,max,średnia,...)
Name:		perl-Math-VecStat
Version:	0.08
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3df23fb451f73bb49fd4ea344ba94020
URL:		http://search.cpan.org/dist/Math-VecStat/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides some basic statistics on numerical vectors. All
the subroutines can take a reference to the vector to be operated on.
In some cases a copy of the vector is acceptable, but is not
recommended for efficiency.

%description -l pl.UTF-8
Ten pakiet dostarcza kilku podstawowych statystyk na wektorach
liczbowych. Wszystkie funkcje mogą przyjąć referencję do wektora, na
którym mają operować. W niektóych przypadkach kopia wektora jest
akceptowalna, ale nie jest to zalecane ze względu na wydajność.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/VecStat.pm
%{_mandir}/man3/*
