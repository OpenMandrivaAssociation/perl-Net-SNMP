%define modname	Net-SNMP
%define modver	6.0.1

Summary:	Object oriented interface to SNMP for perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	13
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{modname}-v%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-Crypt-DES => 2.03
BuildRequires:	perl-Digest-HMAC => 1.0
Requires:	perl-Crypt-DES => 2.03
Requires:	perl-Digest-HMAC => 1.0
Requires:	perl-Digest-SHA1 => 1.02

%description
The Net::SNMP module implements an object oriented interface to the Simple
Network Management Protocol.  Perl applications can use the module to retrieve
or update information on a remote host using the SNMP protocol.  The module
supports SNMP version-1, SNMP version-2c (Community-Based SNMPv2), and SNMP
version-3.
The Net::SNMP module assumes that the user has a basic understanding of the
Simple Network Management Protocol and related network management concepts.

%prep
%setup -qn %{modname}-v%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/snmpkey
%{perl_vendorlib}/Net
%{_mandir}/man1/*
%{_mandir}/man3/*

