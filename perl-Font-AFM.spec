#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Font
%define		pnam	AFM
Summary:	Font::AFM - interface to Adobe Font Metrics files
Summary(pl.UTF-8):	Font::AFM - interfejs do plików metryk fontów Adobe (AFM)
Name:		perl-Font-AFM
Version:	1.19
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f72a12a20656c41b29a79c985bd231c9
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font::AFM is an interface to Adobe Font Metrics files.

%description -l pl.UTF-8
Font::AFM jest interfejsem do plików metryk fontów Adobe (AFM - Adobe
Font Metrics).

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
%doc Changes README
%dir %{perl_vendorlib}/%{pdir}/Metrics
%{perl_vendorlib}/%{pdir}/Metrics/*.pm
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
