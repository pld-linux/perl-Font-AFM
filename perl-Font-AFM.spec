%include	/usr/lib/rpm/macros.perl
%define	pdir	Font
%define	pnam	AFM
Summary:	Font::AFM perl module
Summary(pl):	Modu³ perla Font::AFM
Name:		perl-Font-AFM
Version:	1.18
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font::AFM is an interface to Adobe Font Metrics files.

%description -l pl
Font::AFM jest interfejsem do plików metryk AFM (Adobe Font Metrics).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Font/Metrics
%{perl_vendorlib}/Font/Metrics/*.pm
%{perl_vendorlib}/Font/*.pm
%{_mandir}/man3/*
