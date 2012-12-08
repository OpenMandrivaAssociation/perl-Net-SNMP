%define upstream_name	 Net-SNMP
%define upstream_version 6.0.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Object oriented interface to SNMP for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-v%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-Crypt-DES => 2.03
BuildRequires:	perl-Digest-HMAC => 1.0

BuildArch:	noarch

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
%setup -q -n %{upstream_name}-v%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.1-5mdv2012.0
+ Revision: 765535
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 6.0.1-3
+ Revision: 667278
- mass rebuild

* Tue Mar 15 2011 Thomas Spuhler <tspuhler@mandriva.org> 6.0.1-2
+ Revision: 644850
- increasd rel for rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 6.0.1-1mdv2011.0
+ Revision: 587778
- new version

* Thu Sep 10 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.0.0-1mdv2011.0
+ Revision: 436570
- update to 6.0.0

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 5.2.0-7mdv2010.0
+ Revision: 423709
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 5.2.0-6mdv2009.0
+ Revision: 258107
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 5.2.0-5mdv2009.0
+ Revision: 246171
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 5.2.0-3mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 5.2.0-3mdv2008.0
+ Revision: 25199
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 5.2.0-2mdk
- Fix SPEC according to Perl Policy
	- Source URL

* Fri Nov 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 5.2.0-1mdk
- New release 5.2.0
- %%mkrel

* Fri Sep 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 5.1.0-1mdk
- New release 5.1.0
- spec cleanup
- fix source url for rpmbuildupdate

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.0.1-1mdk
- 5.0.1

* Thu Aug 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.0-1mdk
- 5.0.0

* Thu Nov 27 2003 Stefan van der Eijk <stefan@eijk.nu> 4.1.2-1mdk
- 4.1.2
- streamline BuildRequires

* Wed Aug 27 2003 François Pons <fpons@mandrakesoft.com> 4.1.0-1mdk
- 4.1.0.

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.0.3-2mdk
- rebuild for new auto{prov,req}

