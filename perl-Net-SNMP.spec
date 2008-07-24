%define module	Net-SNMP
%define name	perl-%{module}
%define version 5.2.0
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Object oriented interface to SNMP for perl
License:        GPL or Artistic
Group:          Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:  perl-Crypt-DES => 2.03
BuildRequires:  perl-Digest-HMAC => 1.0
Requires:	perl-Crypt-DES => 2.03
Requires:	perl-Digest-HMAC => 1.0
Requires:	perl-Digest-SHA1 => 1.02
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Net::SNMP module implements an object oriented interface to the Simple
Network Management Protocol.  Perl applications can use the module to retrieve
or update information on a remote host using the SNMP protocol.  The module
supports SNMP version-1, SNMP version-2c (Community-Based SNMPv2), and SNMP
version-3.
The Net::SNMP module assumes that the user has a basic understanding of the
Simple Network Management Protocol and related network management concepts.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/snmpkey
%{perl_vendorlib}/Net
%{_mandir}/*/*

