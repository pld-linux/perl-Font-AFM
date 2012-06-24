%include	/usr/lib/rpm/macros.perl
%define	pdir	Font
%define	pnam	AFM
Summary:	Font::AFM perl module
Summary(pl):	Modu� perla Font::AFM
Name:		perl-Font-AFM
Version:	1.18
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font::AFM is an interface to Adobe Font Metrics files.

%description -l pl
Font::AFM jest interfejsem do plik�w metryk AFM (Adobe Font Metrics).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_sitelib}/Font/Metrics
%{perl_sitelib}/Font/Metrics/*.pm
%{perl_sitelib}/Font/*.pm
%{_mandir}/man3/*
