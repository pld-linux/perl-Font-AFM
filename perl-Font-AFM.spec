%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary: 	Font-AFM perl module
Summary(pl):	Modu� perla Font-AFM
Name: 		perl-Font-AFM
Version: 	1.18
Release: 	3
Copyright: 	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Font/Font-AFM-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Font::AFM is an interface to Adobe Font Metrics files.

%description -l pl
Font::AFM jest interfejsem do plik�w metryk AFM (Adobe Font Metrics).

%prep
%setup -q -n Font-AFM-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Font/AFM
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz
%dir %{perl_sitelib}/Font/Metrics
%{perl_sitelib}/Font/Metrics/*.pm
%{perl_sitelib}/Font/*.pm
%{perl_sitearch}/auto/Font/AFM

%{_mandir}/man3/*
