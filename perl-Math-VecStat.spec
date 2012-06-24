%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	VecStat
Summary:	Math::VecStat - some basic statistics on vectors (min,max,average,...)
Summary(pl):	Math::VecStat - podstawowe statystyki na wektorach (min,max,�rednia,...)
Name:		perl-Math-VecStat
Version:	0.06
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides some basic statistics on numerical vectors. All
the subroutines can take a reference to the vector to be operated on.
In some cases a copy of the vector is acceptable, but is not
recommended for efficiency.

%description -l pl
Ten pakiet dostarcza kilku podstawowych statystyk na wektorach
liczbowych. Wszystkie funkcje mog� przyj�� referencj� do wektora, na
kt�rym maj� operowa�. W niekt�ych przypadkach kopia wektora jest
akceptowalna, ale nie jest to zalecane ze wzgl�du na wydajno��.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
