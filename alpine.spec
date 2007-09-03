# TODO:
# - backport man-pages from pine.spec
# - alpine should obsolete pine, link pine -> alpine should be made
# - pine -> alpine config converter
# - review patches from pine:
#   - home_etc support
#   - ....many more
Summary:	University of Washington Pine mail user agent
Summary(pl.UTF-8):	Klient pocztowy Pine z Uniwersytetu w Waszyngtonie
Name:		alpine
Version:	0.999
Release:	0.4
Epoch:		1
License:	Apache License 2.0
Group:		Applications/Mail
Source0:	ftp://ftp.cac.washington.edu/alpine/%{name}-%{version}.tar.gz
# Source0-md5:	082de388a998c1faa2385ebdfd6800f5
Source1:	pico.desktop
# http://staff.washington.edu/chappa/alpine/info/all.html
Patch0:		http://staff.washington.edu/chappa/alpine/patches/%{name}-%{version}/all.patch.gz
URL:		http://www.washington.edu/alpine
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	krb5-devel
BuildRequires:	ncurses-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		alpineconfdir	/etc/%{name}

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

%package -n pico
Summary:        Simple text editor in the style of the Pine Composer
Summary(pl.UTF-8):      Prosty edytor tekstowy w stylu alpine
Summary(pt_BR.UTF-8):   Editor de textos para terminal simples e fácil de usar
Group:          Applications/Editors

%description -n pico
Pico is a simple, display-oriented text editor based on the Alpine
message system composer. As with Pine, commands are displayed at the
bottom of the screen, and context-sensitive help is provided. As
characters are typed they are immediately inserted into the text.

%description -n pico -l pl.UTF-8
Pico jest prostym, zorientowanym na wyświetlanie edytorem bazującym na
alpine. Tak jak w pine komendy są wyświetlane na dole ekranu oraz
dostępna jest pomoc konteksowa. Wpisywane znaki są natychmiast
włączane do tekstu.

%description -n pico -l pt_BR.UTF-8
Pico é um editor de texto baseado no compositor de mensagens do Alpine.
Assim como no Pine, comandos são mostrados na parte de baixo da tela,
e ajuda de acordo com o contexto está disponível.

%package -n pilot
Summary:        Simple file system browser in the style of the Alpine Composer
Summary(pl.UTF-8):      Prosta przeglądarka plików w stylu composera alpine
Summary(pt_BR.UTF-8):   Navegador de sistemas de arquivos no estilo do compositor do Alpine
Group:          Applications/Shells

%description -n pilot
Pilot is a simple, display-oriented file system browser based on the
Alpine message system composer. As with Alpine, commands are displayed at
the bottom of the screen, and context-sensitive help is provided.

%description -n pilot -l pl.UTF-8
Pilot jest prostą, zorientowaną na wyświetlanie przeglądarką plików w
stylu compsera pine. Podobnie jak w alpine polecenia sa wyświetlane na
dole ekranu oraz jest dostępna pomoc kontekstowa.

%description -n pilot -l pt_BR.UTF-8
Pilot é um navegador de sistemas de arquivos baseado no Pine. Assim
como no Pine, comandos são apresentados na parte de baixo da tela, e
ajuda de acordo com o contexto está disponível.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%{__aclocal} -I m4
%{__automake}
%configure \
	--enable-quotas \
	--with-smtp-msa=%{_libdir}/sendmail \
	--with-spellcheck-prog=aspell \
	--with-system-pinerc=%{alpineconfdir}/%{name}.conf \
	--with-system-fixed-pinerc=%{alpineconfdir}/%{name}.conf.fixed \
	--with-krb5-dir=%{_prefix} \
	--with-ldap-dir=%{_prefix} \
	--with-system-mail-directory=/var/mail
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{alpineconfdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/tech-notes.txt
%dir %{alpineconfdir}
%attr(755,root,root) %{_bindir}/alpine
%attr(755,root,root) %{_bindir}/rpload
%attr(755,root,root) %{_bindir}/rpdump
#%attr(755,root,root) %{_bindir}/mailutil
#%attr(2755,root,mail) %{_sbindir}/mlock
%{_mandir}/man1/alpine.1*
#%{_mandir}/man1/rpload.1*
#%{_mandir}/man1/rpdump.1*
#%{_mandir}/man1/mailutil.1*

%files -n pico
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pico
%{_desktopdir}/pico.desktop
%{_mandir}/man1/pico*

%files -n pilot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pilot
%{_mandir}/man1/pilot*
