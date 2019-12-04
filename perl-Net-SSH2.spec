#
# Conditional build:
%bcond_without	tests # do not perform "make test"

%define		pdir	Net
%define		pnam	SSH2
%include	/usr/lib/rpm/macros.perl
Summary:	Net::SSH2 Perl module - support for the SSH 2 protocol via libssh2
Summary(pl.UTF-8):	Moduł Perla Net::SSH2 - obsługa protokołu SSH 2 poprzez libssh2
Name:		perl-Net-SSH2
Version:	0.69
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94ed21d4557a6bbc3cb6bfd7c3479ef0
URL:		http://search.cpan.org/dist/Net-SSH2/
BuildRequires:	libssh2-devel >= 1.7.0
BuildRequires:	openssl-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SSH2 is a Perl interface to the libssh2 (http://www.libssh2.org/)
library. It supports the SSH 2 protocol (there is no support for SSH
1) with all of the key exchanges, ciphers, and compression of libssh2.

%description -l pl.UTF-8
Net::SSH to perlowy interfejs do biblioteki libssh2
(http://www.libssh2.org/). Obsługuje protokół SSH 2 (nie ma obsługi
SSH 1), w tym wymianę kluczy, szyfry i kompresję z libssh2.

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
%doc Changes README example/read.pl
%{perl_vendorarch}/Net/SSH2.pm
%{perl_vendorarch}/Net/SSH2
%dir %{perl_vendorarch}/auto/Net/SSH2
%attr(755,root,root) %{perl_vendorarch}/auto/Net/SSH2/SSH2.so
%{_mandir}/man3/Net::SSH2*.3pm*
