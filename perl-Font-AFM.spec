%include	/usr/lib/rpm/macros.perl
Summary:	Font-AFM perl module
Summary(pl):	Modu³ perla Font-AFM
Name:		perl-Font-AFM
Version:	1.18
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Font/Font-AFM-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font::AFM is an interface to Adobe Font Metrics files.

%description -l pl
Font::AFM jest interfejsem do plików metryk AFM (Adobe Font Metrics).

%prep
%setup -q -n Font-AFM-%{version}

%build
perl Makefile.PL

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{perl_sitelib}/Font/Metrics
%{perl_sitelib}/Font/Metrics/*.pm
%{perl_sitelib}/Font/*.pm
%{_mandir}/man3/*
