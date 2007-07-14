Summary:	University of Washington Pine mail user agent
Summary(pl.UTF-8):	Klient pocztowy Pine z Uniwersytetu w Waszyngtonie
Name:		alpine
Version:	0.999
Release:	0.1
License:	Apache License
Group:		Applications/Mail
Source0:	ftp://ftp.cac.washington.edu/alpine/%{name}-%{version}.tar.gz
# Source0-md5:	082de388a998c1faa2385ebdfd6800f5
URL:		http://www.washington.edu/alpine
BuildRequires:	krb5-devel
BuildRequires:	ncurses-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alpine -- an Alternatively Licensed Program for Internet News & Email
-- is a tool for reading, sending, and managing electronic messages.
Alpine is the successor to Pine and was developed by Computing &
Communications at the University of Washington. Though originally
designed for inexperienced email users, Alpine supports many advanced
features, and an ever-growing number of configuration and
personal-preference options.

%description -l pl.UTF-8
Alpine, czyli Alternatively Licensed Program for Internet News & Email
(alternatywnie licencjonowany program do newsów i poczty internetowej)
to narzędzie do czytania, wysyłania i zarządzania wiadomościami
elektronicznymi. Alpine jest następcą Pine'a i został napisany przez
wydział Computing & Communications (Obliczeń i komunikacji) na
Uniwersytecie w Waszyngtonie. Mimo że Alpine pierwotnie został
zaprojektowany dla niedoświadczonych użytkowników poczty, obsługuje
wiele zaawansowanych możliwości, a liczba opcji konfiguracyjnych
ciągle rośnie.

%prep
%setup -q

%build
%configure \
	--enable-quotas \
	--with-smtp-msa=%{_libdir}/sendmail \
	--with-spellcheck-prog=aspell \
	--with-system-pinerc=/etc/alpine/alpine.conf \
	--with-system-fixed-pinerc=/etc/alpine/alpine.conf.fixed \
	--with-krb5-dir=%{_prefix} \
	--with-ldap-dir=%{_prefix} \
	--with-system-mail-directory=/var/mail
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE doc/tech-notes.txt
%attr(755,root,root) %{_bindir}/alpine
%attr(755,root,root) %{_bindir}/pico
%attr(755,root,root) %{_bindir}/pilot
%attr(755,root,root) %{_bindir}/rpload
%attr(755,root,root) %{_bindir}/rpdump
%attr(755,root,root) %{_bindir}/mailutil
%attr(2755,root,mail) %{_sbindir}/mlock
%{_mandir}/man1/alpine.1*
%{_mandir}/man1/pico.1*
%{_mandir}/man1/pilot.1*
%{_mandir}/man1/rpload.1*
%{_mandir}/man1/rpdump.1*
%{_mandir}/man1/mailutil.1*
