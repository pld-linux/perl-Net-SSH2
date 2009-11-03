#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	SSH2
Summary:	Net::SSH2 Perl module
Summary(cs.UTF-8):	Modul Net::SSH2 pro Perl
Summary(da.UTF-8):	Perlmodul Net::SSH2
Summary(de.UTF-8):	Net::SSH2 Perl Modul
Summary(es.UTF-8):	Módulo de Perl Net::SSH2
Summary(fr.UTF-8):	Module Perl Net::SSH2
Summary(it.UTF-8):	Modulo di Perl Net::SSH2
Summary(ja.UTF-8):	Net::SSH2 Perl モジュール
Summary(ko.UTF-8):	Net::SSH2 펄 모줄
Summary(nb.UTF-8):	Perlmodul Net::SSH2
Summary(pl.UTF-8):	Moduł Perla Net::SSH2
Summary(pt.UTF-8):	Módulo de Perl Net::SSH2
Summary(pt_BR.UTF-8):	Módulo Perl Net::SSH2
Summary(ru.UTF-8):	Модуль для Perl Net::SSH2
Summary(sv.UTF-8):	Net::SSH2 Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Net::SSH2
Summary(zh_CN.UTF-8):	Net::SSH2 Perl 模块
Name:		perl-Net-SSH2
Version:	0.28
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5d6a9c4b2256c34819c0d6f3a0163066
BuildRequires:	libssh2-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SSH2 is a perl interface to the libssh2 (http://www.libssh2.org)
library. It supports the SSH2 protocol (there is no support for SSH1)
with all of the key exchanges, ciphers, and compression of libssh2.

%description -l pl.UTF-8
Net::SSH - interfejs do biblioteki libssh2 (http://www.libssh2.org).

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
%doc Changes README TODO
%{perl_vendorarch}/Net/SSH2.pm
%{perl_vendorarch}/Net/SSH2
%dir %{perl_vendorarch}/auto/Net/SSH2
%{perl_vendorarch}/auto/Net/SSH2/autosplit.ix
%{perl_vendorarch}/auto/Net/SSH2/SSH2.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/SSH2/SSH2.so
%{_mandir}/man3/*
