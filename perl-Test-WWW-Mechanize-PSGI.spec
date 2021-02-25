#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	WWW-Mechanize-PSGI
Summary:	Test::WWW::Mechanize::PSGI - Test PSGI programs using WWW::Mechanize
Name:		perl-Test-WWW-Mechanize-PSGI
Version:	0.39
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	75fde422172f4a098ac14d39fa06ee57
URL:		https://metacpan.org/release/Test-WWW-Mechanize-PSGI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Plack
BuildRequires:	perl-Test-WWW-Mechanize
BuildRequires:	perl-Try-Tiny
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PSGI is a specification to decouple web server environments from web
application framework code. Test::WWW::Mechanize is a subclass of
WWW::Mechanize that incorporates features for web application testing.
The Test::WWW::Mechanize::PSGI module meshes the two to allow easy
testing of PSGI applications.

Testing web applications has always been a bit tricky, normally
requiring starting a web server for your application and making real
HTTP requests to it. This module allows you to test PSGI web
applications but does not require a server or issue HTTP requests.
Instead, it passes the HTTP request object directly to PSGI. Thus you
do not need to use a real hostname: "http://localhost/" will do.
However, this is optional. The following two lines of code do exactly
the same thing:

$mech->get_ok('/action'); $mech->get_ok('http://localhost/action');

This makes testing fast and easy. Test::WWW::Mechanize provides
functions for common web testing scenarios. For example:

$mech->get_ok( $page ); $mech->title_is( "Invoice Status", "Make sure
we're on the invoice page" ); $mech->content_contains( "Andy Lester",
"My name somewhere" ); $mech->content_like( qr/(cpan|perl)\.org/,
"Link to perl.org or CPAN" );

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL
%{perl_vendorlib}/Test/WWW/Mechanize/*.pm
%{_mandir}/man3/*
