%define		apxs	/usr/sbin/apxs
%define		apache	/usr/sbin/httpd
Summary:	Modules for Internet programming in OCaml
Summary(pl.UTF-8):	Moduły ułatwiające pisanie programów internetowych w OCamlu
Name:		ocaml-net
Version:	3.6
Release:	2
License:	GPL v2+ (nethttpd), LGPL v2+ (mod_caml), BSD-like (the rest)
Group:		Libraries
Source0:	http://download.camlcity.org/download/ocamlnet-%{version}.tar.gz
# Source0-md5:	c6a42744c456b3b336c7613f5481650a
Patch0:		%{name}-buildfix.patch
Patch1:		%{name}-lablgtk2.patch
Patch2:		%{name}-zip.patch
Patch3:		%{name}-apache-link.patch
URL:		http://projects.camlcity.org/projects/ocamlnet.html
BuildRequires:	%{apache}
BuildRequires:	%{apxs}
BuildRequires:	apache-devel >= 2.0
BuildRequires:	ncurses-devel
BuildRequires:	ocaml >= 1:3.09.2
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml-cryptgps-devel
BuildRequires:	ocaml-cryptokit-devel
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-lablgtk-devel
BuildRequires:	ocaml-lablgtk2-devel >= 2.14.2
BuildRequires:	ocaml-labltk-devel
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-ssl-devel
BuildRequires:	ocaml-zip-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_apachepkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_apachesysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)/conf.d

%description
Modules for Internet programming in OCaml.

%description -l pl.UTF-8
Moduły ułatwiające pisanie programów internetowych w OCamlu.

%package doc
Summary:	ocaml-net documentation
Summary(pl.UTF-8):	Dokumentacja dla pakietów ocaml-net
License:	BSD-like
Group:		Development/Libraries

%description doc
ocaml-net documentation.

%description doc -l pl.UTF-8
Dokumentacja dla pakietów ocaml-net.

%package netcgi-devel
Summary:	Common Gateway Interface library
Summary(pl.UTF-8):	Biblioteka do tworzenia skryptów CGI
License:	LGPL v2+ (mod_caml), BSD-like (the rest)
Group:		Development/Libraries
Requires:	%{name}-netplex-devel = %{version}-%{release}
Requires:	%{name}-netstring-devel = %{version}-%{release}
Requires:	%{name}-netsys-devel = %{version}-%{release}
Obsoletes:	ocaml-net-cgi-devel
%requires_eq	ocaml

%description netcgi-devel
Common Gateway Interface library, part of Ocamlnet. This package
contains files needed to develop OCaml programs using netcgi library.

%description netcgi-devel -l pl.UTF-8
Biblioteka do tworzenia skryptów CGI, część pakietu Ocamlnet. Ten
pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netcgi.

%package -n apache-mod_netcgi
Summary:	Apache module:
Summary(pl.UTF-8):	Moduł Apache'a:
Group:		Networking/Daemons/HTTP
Requires:	apache(modules-api) = %apache_modules_api

%description -n apache-mod_netcgi

%description -n apache-mod_netcgi -l pl.UTF-8

%package equeue-devel
Summary:	Event queue library for OCaml
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń dla OCamla
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml
Obsoletes:	ocaml-equeue-devel

%description equeue-devel
Equeue provides a generic event queue module, and a specific module
for file descriptor events.

This package contains files needed to develop OCaml programs using
equeue library.

%description equeue-devel -l pl.UTF-8
Equeue dostarcza ogólnego modułu obsługi kolejki zdarzeń jak również
modułu obsługi zdarzeń na deskryptorach plików.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki equeue.

%package equeue-gtk-devel
Summary:	GTK event queue library for OCaml
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń GTK dla OCamla
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	ocaml-lablgtk-devel
%requires_eq	ocaml

%description equeue-gtk-devel
Equeue provides a generic event queue module, and a specific module
for file descriptor events.

This package contains files needed to develop OCaml programs using GTK
equeue library.

%description equeue-gtk-devel -l pl.UTF-8
Equeue dostarcza ogólnego modułu obsługi kolejki zdarzeń jak również
modułu obsługi zdarzeń na deskryptorach plików.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki equeue GTK.

%package equeue-gtk2-devel
Summary:	GTK2 event queue library for OCaml
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń GTK2 dla OCamla
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	ocaml-lablgtk2-devel
%requires_eq	ocaml

%description equeue-gtk2-devel
Equeue provides a generic event queue module, and a specific module
for file descriptor events.

This package contains files needed to develop OCaml programs using
GTK2 equeue library.

%description equeue-gtk2-devel -l pl.UTF-8
Equeue dostarcza ogólnego modułu obsługi kolejki zdarzeń jak również
modułu obsługi zdarzeń na deskryptorach plików.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki equeue GTK2.

%package equeue-ssl
Summary:	Event queue library for OCaml, SSL support
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń dla OCamla, wsparcie dla SSL
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime

%description equeue-ssl
This package makes it possible to let Equeue cooperate with the event
queue implementation of SSL.

This package contains files needed to run bytecode executables using
equeue-ssl library.

%description equeue-ssl -l pl.UTF-8
Pakiet ten umożliwia współpracę Equeue z implementacją kolejki zdarzeń
w SSL.

Ten pakiet zawiera moduł potrzebny do uruchamiania programów
używających biblioteki equeue-ssl.

%package equeue-ssl-devel
Summary:	Equeue SSL support - development part
Summary(pl.UTF-8):	Wsparcie dla SSL-a w equeue - cześć programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	%{name}-equeue-ssl = %{version}-%{release}
%requires_eq	ocaml-ssl-devel
%requires_eq	ocaml

%description equeue-ssl-devel
This package makes it possible to let Equeue cooperate with the event
queue implementation of SSL.

This package contains files needed to develop OCaml programs using
equeue-ssl library.

%description equeue-ssl-devel -l pl.UTF-8
Pakiet ten umożliwia współpracę Equeue z implementacją kolejki zdarzeń
w SSL.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki equeue-ssl.

%package equeue-tcl
Summary:	Event queue library for OCaml, Tcl support
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń dla OCamla, wsparcie dla Tcl
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime
%requires_eq	ocaml-labltk
Obsoletes:	ocaml-equeue-tcl

%description equeue-tcl
This package makes it possible to let Equeue cooperate with the event
queue implementation of Tcl.

This package contains files needed to run bytecode executables using
equeue-tcl library.

%description equeue-tcl -l pl.UTF-8
Pakiet ten umożliwia współpracę Equeue z implementacją kolejki zdarzeń
w Tcl.

Ten pakiet zawiera moduły potrzebne do uruchamiania programów
używających biblioteki equeue-tcl.

%package equeue-tcl-devel
Summary:	Equeue Tcl support - development part
Summary(pl.UTF-8):	Wsparcie dla Tcl-a w equeue - cześć programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	%{name}-equeue-tcl = %{version}-%{release}
%requires_eq	ocaml-labltk-devel
%requires_eq	ocaml
Obsoletes:	ocaml-equeue-tcl-devel

%description equeue-tcl-devel
This package makes it possible to let Equeue cooperate with the event
queue implementation of Tcl.

This package contains files needed to develop OCaml programs using
this library.

%description equeue-tcl-devel -l pl.UTF-8
Pakiet ten umożliwia współpracę Equeue z implementacją kolejki zdarzeń
w Tcl.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki equeue-tcl.

%package netcamlbox-devel
Summary:	Fast IPC mechanism for OCaml
Summary(pl.UTF-8):	Szybki mechanizm IPC dla OCamla
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml

%description netcamlbox-devel
Camlboxes are a fast IPC mechanism to send Ocaml values from one
process to another. Source and destination processes must run on the
same machine (no network). The Ocaml value is copied to a shared
memory object where it can be directly accessed by the receiver
without unmarshalling step. This means the sender writes the value
into the shared memory in a format that can immediately interpreted by
the receiver.

This package contains files needed to develop OCaml programs using
netcamlbox library.

%description netcamlbox-devel -l pl.UTF-8
Camlboxy są szybkim mechanizmem IPC do przesyłania danych Ocamla
pomiędzy procesami. Nadawca i odbiorca muszą być uruchomione na tej
samej maszynie. Dane Ocamla są kopiowane do segmentu pamięci
dzielonej, gdzie mogą byc bezpośrednio odczytywane przez odbiorcę.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netcamlbox.

%package netclient-devel
Summary:	HTTP 1.1 client for OCaml
Summary(pl.UTF-8):	Klient HTTP 1.1 dla OCamla
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	%{name}-netstring-devel = %{version}-%{release}
%requires_eq	ocaml
Obsoletes:	ocaml-netclient-devel

%description netclient-devel
Implements much of HTTP/1.1. Implements the following advanced
features: chunked messages; persistent connections; connections in
pipelining mode ("full duplex" connections); modular authentication
methods, currently Basic and Digest; event-driven implementation;
allows concurrent service for several network connections.

This package contains files needed to develop OCaml programs using
netclient library.

%description netclient-devel -l pl.UTF-8
Biblioteka netclient implementuje większość HTTP/1.1, a także
następujące zaawansowane właściwości: komunikaty w kawałkach;
połączenia stałe; połączenia w trybie "full duplex"; modularne metody
uwierzytelniania, obecnie Basic i Digest; implementacja oparta na
zdarzeniach; umożliwia jednoczesną obsługę kilku połączeń.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netclient.

%package netgssapi-devel
Summary:	GSS-API generic definition
Summary(pl.UTF-8):	Biblioteka do obsługi protokołu GSSAPI
License:	GPL v2+
Group:		Development/Libraries
Requires:	%{name}-netstring-devel = %{version}-%{release}
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml

%description netgssapi-devel
GSSAPI library, part of Ocamlnet. This package contains the files
needed to develop OCaml programs using netgssapi library.

%description netgssapi-devel -l pl.UTF-8
Biblioteka do obsługi protokołu GSSAPI, część pakietu Ocamlnet. Ten
pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netgssapi.

%package nethttpd-devel
Summary:	HTTPd library
Summary(pl.UTF-8):	Biblioteka do obsługi protokołu HTTP
License:	GPL v2+
Group:		Development/Libraries
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	%{name}-netcgi-devel = %{version}-%{release}
Requires:	%{name}-netplex-devel = %{version}-%{release}
%requires_eq	ocaml-pcre-devel
%requires_eq	ocaml

%description nethttpd-devel
HTTPd library, part of Ocamlnet. This package contains the files
needed to develop OCaml programs using nethttpd library.

%description nethttpd-devel -l pl.UTF-8
Biblioteka do obsługi protokołu HTTP, część pakietu Ocamlnet. Ten
pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki nethttpd.

%package netmech-scram-devel
Summary:	SCRAM mechanism for authentication
Summary(pl.UTF-8):	Mechanizm autentykacji SCRAM
License:	GPL v2+
Group:		Development/Libraries
Requires:	%{name}-netcamlbox-devel = %{version}-%{release}
Requires:	%{name}-netplex-devel = %{version}-%{release}
%requires_eq	ocaml

%description netmech-scram-devel
Netmech-scram library, part of Ocamlnet. This package contains the
files needed to develop OCaml programs using netmech-scram library.

%description netmech-scram-devel -l pl.UTF-8
Biblioteka do obsługi wieloprocesorowych obliczeń, część pakietu
Ocamlnet. Ten pakiet zawiera pliki niezbędne do tworzenia programów
używających biblioteki netmech-scram.

%package netmulticore-devel
Summary:	Multi-processing for compute jobs
Summary(pl.UTF-8):	Obsługa wieloprocesorowych obliczeń
License:	GPL v2+
Group:		Development/Libraries
Requires:	%{name}-netcamlbox-devel = %{version}-%{release}
Requires:	%{name}-netplex-devel = %{version}-%{release}
%requires_eq	ocaml

%description netmulticore-devel
Netmcore library, part of Ocamlnet. This package contains the files
needed to develop OCaml programs using netmulticore library.

%description netmulticore-devel -l pl.UTF-8
Biblioteka do obsługi wieloprocesorowych obliczeń, część pakietu
Ocamlnet. Ten pakiet zawiera pliki niezbędne do tworzenia programów
używających biblioteki netmulticore.

%package netplex
Summary:	Server framework
Summary(pl.UTF-8):	Szkielet serwerowy
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime
%requires_eq	ocaml-labltk

%description netplex
Server framework.

This package contains files needed to run bytecode executables using
netplex library.

%description netplex -l pl.UTF-8
Szkielet serwerowy.

Ten pakiet zawiera moduły potrzebne do uruchamiania programów
używających biblioteki netplex.

%package netplex-devel
Summary:	Server framework - development part
Summary(pl.UTF-8):	Szkielet serwerowy - cześć programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	%{name}-netplex = %{version}-%{release}
Requires:	%{name}-netstring-devel = %{version}-%{release}
Requires:	%{name}-netsys-devel = %{version}-%{release}
Requires:	%{name}-rpc-devel = %{version}-%{release}
%requires_eq	ocaml

%description netplex-devel
Server framework.

This package contains files needed to develop OCaml programs using
netplex library.

%description netplex-devel -l pl.UTF-8
Szkielet serwerowy.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netplex.

%package netshm-devel
Summary:	Shared memory support - development package
Summary(pl.UTF-8):	Obsługa pamięci dzielonej - pakiet programistyczny
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml

%description netshm-devel
Shared memory support.

This package contains files needed to develop OCaml programs using
netshm library.

%description netshm-devel -l pl.UTF-8
Obsługa pamięci dzielonej.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netshm.

%package netstring
Summary:	String processing library
Summary(pl.UTF-8):	Biblioteka do przetwarzania napisów
License:	BSD-like
Group:		Libraries
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml-pcre-devel
%requires_eq	ocaml

%description netstring
String processing library, part of Ocamlnet.

%description netstring -l pl.UTF-8
Biblioteka do przetwarzania napisów, część pakietu Ocamlnet.

%package netstring-devel
Summary:	String processing library
Summary(pl.UTF-8):	Biblioteka do przetwarzania napisów
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netstring = %{version}-%{release}
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml-pcre-devel
%requires_eq	ocaml

%description netstring-devel
String processing library, part of Ocamlnet. This package contains
files needed to develop OCaml programs using netstring library.

%description netstring-devel -l pl.UTF-8
Biblioteka do przetwarzania napisów, część pakietu Ocamlnet. Ten
pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netstring.

%package netsys
Summary:	OS-specific functions
Summary(pl.UTF-8):	Funkcje specyficzne dla systemu operacyjnego
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime

%description netsys
OS-specific functions.

This package contains files needed to run bytecode executables using
netsys library.

%description netsys -l pl.UTF-8
Funkcje specyficzne dla systemu operacyjnego.

Ten pakiet zawiera moduły potrzebne do uruchamiania programów
używających biblioteki netsys.

%package netsys-devel
Summary:	OS-specific functions - development part
Summary(pl.UTF-8):	Funkcje specyficzne dla systemu operacyjnego - cześć programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netsys = %{version}-%{release}
%requires_eq	ocaml

%description netsys-devel
OS-specific functions.

This package contains files needed to develop OCaml programs using
netsys library.

%description netsys-devel -l pl.UTF-8
Funkcje specyficzne dla systemu operacyjnego.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netsys.

%package netzip-devel
Summary:	Gzip channels - development part
Summary(pl.UTF-8):	Funkcje do kompresji kanałow - cześć programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netstring-devel = %{version}-%{release}
%requires_eq	ocaml

%description netzip-devel
Gzip channels functions.

This package contains files needed to develop OCaml programs using
netzip library.

%description netzip-devel -l pl.UTF-8
Funkcje do kompresji kanałow.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netzip.

%package pop3-devel
Summary:	Post Office Protocol (POP3) library
Summary(pl.UTF-8):	Biblioteka do obsługi POP3
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netstring-devel = %{version}-%{release}
%requires_eq	ocaml

%description pop3-devel
Post Office Protocol (POP3) library, part of Ocamlnet. This package
contains files needed to develop OCaml programs using pop library.

%description pop3-devel -l pl.UTF-8
Biblioteka do obsługi POP3, część pakietu Ocamlnet. Ten pakiet zawiera
pliki niezbędne do tworzenia programów używających biblioteki pop.

%package rpc
Summary:	Remote Procedure Call (RPC) libraries
Summary(pl.UTF-8):	Biblioteki do obsługi RPC
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-equeue-ssl = %{version}-%{release}
%requires_eq	ocaml

%description rpc
Remote Procedure Call (RPC) libraries.

%description rpc -l pl.UTF-8
Biblioteki do obsługi RPC.

%package rpc-devel
Summary:	Remote Procedure Call (RPC) libraries - development part
Summary(pl.UTF-8):	Biblioteki do obsługi RPC - część programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-equeue-ssl-devel = %{version}-%{release}
Requires:	%{name}-rpc = %{version}-%{release}
%requires_eq	ocaml

%description rpc-devel
Remote Procedure Call (RPC) libraries - development part.

%description rpc-devel -l pl.UTF-8
Biblioteki do obsługi RPC - część programistyczna.

%package shell-devel
Summary:	Unix shell functions
Summary(pl.UTF-8):	Funkcje powłoki uniksowej
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq    ocaml

%description shell-devel
Unix shell functions.

%description shell-devel -l pl.UTF-8
Funkcje powłoki uniksowej.

%package smtp-devel
Summary:	Simple Mail Transfer Protocol (SMTP) library
Summary(pl.UTF-8):	Biblioteka do obsługi SMTP
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netstring-devel = %{version}-%{release}
%requires_eq    ocaml

%description smtp-devel
Interface for the Simple Mail Tranfer Protocol (SMTP) as specified by
RFC 2821.

%description smtp-devel -l pl.UTF-8
Interfejs dla protokołu SMTP opisanego w RFC 2821.

%prep
%setup -q -n ocamlnet-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# no %%configure, please
./configure \
	-enable-gtk \
	-enable-gtk2 \
	-enable-ssl \
	-enable-zip \
	-enable-crypto \
	-enable-apache \
	-with-rpc-auth-dh \
	-enable-tcl \
	-equeue-tcl-libs "-ltcl" \
	-with-nethttpd \
	-apxs %{apxs} \
	-apache %{apache}

%{__make} -j1 all opt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/ocaml/stublibs,%{_apachepkglibdir},%{_apachesysconfdir}}

%{__make} -j1 install \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	DESTDIR=$RPM_BUILD_ROOT

cd src
for f in e* n* p* r* shell smtp ; do
	[ -d $RPM_BUILD_ROOT%{_libdir}/ocaml/$f ] || continue
	install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/$f
	mv $RPM_BUILD_ROOT%{_libdir}/ocaml/$f/META \
		$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/$f/
	echo "directory = \"+$f\"" \
		>> $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/$f/META
done
cd ..

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/netcgi_apache/500netcgi_apache.info
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/netcgi_apache/META
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs/mod_netcgi_apache.so*

install -p src/netcgi2-apache/mod_netcgi_apache.so $RPM_BUILD_ROOT%{_apachepkglibdir}/mod_netcgi.so
cat <<EOF >$RPM_BUILD_ROOT%{_apachesysconfdir}/90_mod_netcgi.conf
LoadModule netcgi_module     modules/mod_netcgi.so

<IfModule netcgi_module>
	NetcgiLoad pcre/pcre.cma
	NetcgiLoad netsys/netsys.cma
	NetcgiLoad netstring/netstring.cma
	NetcgiLoad str.cma
	NetcgiLoad netcgi2/netcgi.cma
	NetcgiLoad netcgi2-apache/netcgi_apache.cma

	NetcgiHandler Netcgi_apache.bytecode
	AddHandler ocaml-bytecode .cma

#	Alias /caml-bin/ /path/to/your/scripts/
#	<Location /caml-bin>
#		SetHandler ocaml-bytecode
#		NetcgiHandler Netcgi_apache.bytecode
#		Options ExecCGI
#		Allow from all
#	</Location>
</IfModule>
EOF

# not sure about *.o
rm $RPM_BUILD_ROOT%{_libdir}/ocaml/*/*.mli

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-{netcgi,equeue,netcamlbox,netmulticore,netclient,nethttpd,pop3,rpc}-%{version}
cp -r examples/camlbox/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-netcamlbox-%{version}
cp -r examples/cgi/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-netcgi-%{version}
cp -r examples/equeue/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-equeue-%{version}
cp -r examples/multicore/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-netmulticore-%{version}
cp -r examples/netclient/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-netclient-%{version}
cp -r examples/nethttpd/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-nethttpd-%{version}
cp -r examples/pop/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-pop3-%{version}
cp -r examples/rpc/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-rpc-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files doc
%defattr(644,root,root,755)
%doc LICENSE* ChangeLog RELNOTES doc/html-main

%files netcgi-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netcgi*
%{_libdir}/ocaml/netcgi*/*.cm[ixao]*
%{_libdir}/ocaml/netcgi*/*.a
%{_libdir}/ocaml/site-lib/*cgi*
%{_examplesdir}/%{name}-netcgi-%{version}

%files -n apache-mod_netcgi
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_apachesysconfdir}/*_mod_netcgi.conf
%attr(755,root,root) %{_apachepkglibdir}/mod_netcgi.so

%files equeue-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/equeue
%{_libdir}/ocaml/equeue/*.cm[ixao]*
%{_libdir}/ocaml/equeue/*.a
%{_libdir}/ocaml/site-lib/equeue
%{_examplesdir}/%{name}-equeue-%{version}

%files equeue-gtk-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/equeue-gtk1
%{_libdir}/ocaml/equeue-gtk1/*.cm[ixao]*
%{_libdir}/ocaml/equeue-gtk1/*.a
%{_libdir}/ocaml/site-lib/equeue-gtk1

%files equeue-gtk2-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/equeue-gtk2
%{_libdir}/ocaml/equeue-gtk2/*.cm[ixao]*
%{_libdir}/ocaml/equeue-gtk2/*.a
%{_libdir}/ocaml/site-lib/equeue-gtk2

%files equeue-ssl
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/equeue-ssl
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllequeue_ssl.so
%{_libdir}/ocaml/stublibs/dllequeue_ssl.so.owner

%files equeue-ssl-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/equeue-ssl/*.cm[ixao]*
%{_libdir}/ocaml/equeue-ssl/*.a
%{_libdir}/ocaml/site-lib/equeue-ssl

%files equeue-tcl
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/equeue-tcl
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllequeue_tcl.so
%{_libdir}/ocaml/stublibs/dllequeue_tcl.so.owner

%files equeue-tcl-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/equeue-tcl/*.cm[ixao]*
%{_libdir}/ocaml/equeue-tcl/*.a
%{_libdir}/ocaml/site-lib/equeue-tcl

%files netcamlbox-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netcamlbox
%{_libdir}/ocaml/netcamlbox/*.cm[ixao]*
%{_libdir}/ocaml/netcamlbox/*.a
%{_libdir}/ocaml/site-lib/netcamlbox
%{_examplesdir}/%{name}-netcamlbox-%{version}

%files netclient-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netclient
%{_libdir}/ocaml/netclient/*.cm[ixao]*
%{_libdir}/ocaml/netclient/*.a
%{_libdir}/ocaml/site-lib/netclient
%{_examplesdir}/%{name}-netclient-%{version}

%files netgssapi-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netgssapi
%{_libdir}/ocaml/netgssapi/*.cm[ixao]*
%{_libdir}/ocaml/netgssapi/*.a
%{_libdir}/ocaml/site-lib/netgssapi

%files nethttpd-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/nethttpd
%{_libdir}/ocaml/nethttpd/*.cm[ixa]*
%{_libdir}/ocaml/nethttpd/*.a
%{_libdir}/ocaml/site-lib/nethttpd
%{_examplesdir}/%{name}-nethttpd-%{version}

%files netmech-scram-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netmech-scram
%{_libdir}/ocaml/netmech-scram/*.cm[ixa]*
%{_libdir}/ocaml/netmech-scram/*.a
%{_libdir}/ocaml/site-lib/netmech-scram

%files netmulticore-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netmulticore
%{_libdir}/ocaml/netmulticore/*.cm[ixa]*
%{_libdir}/ocaml/netmulticore/*.a
%{_libdir}/ocaml/site-lib/netmulticore
%{_examplesdir}/%{name}-netmulticore-%{version}

%files netplex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/netplex-admin
%dir %{_libdir}/ocaml/netplex
%{_libdir}/ocaml/netplex/*.o

%files netplex-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netplex/netplex-packlist
%{_libdir}/ocaml/netplex/*.cm[ixao]*
%{_libdir}/ocaml/netplex/*.a
%{_libdir}/ocaml/site-lib/netplex

%files netshm-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netshm
%{_libdir}/ocaml/netshm/*.cm[ixao]*
%{_libdir}/ocaml/netshm/*.a
%{_libdir}/ocaml/site-lib/netshm

%files netstring
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netstring
%{_libdir}/ocaml/netstring/*.o
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllnetaccel_c.so
%{_libdir}/ocaml/stublibs/dllnetaccel_c.so.owner

%files netstring-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netstring/netdb-packlist
%{_libdir}/ocaml/netstring/*.cm[ixao]*
%{_libdir}/ocaml/netstring/*.a
%{_libdir}/ocaml/site-lib/netstring

%files netsys
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netsys
%{_libdir}/ocaml/netsys/*.o
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllnetsys.so
%{_libdir}/ocaml/stublibs/dllnetsys.so.owner

%files netsys-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netsys/*.cm[ixao]*
%{_libdir}/ocaml/netsys/*.a
%{_libdir}/ocaml/site-lib/netsys

%files netzip-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netzip
%{_libdir}/ocaml/netzip/*.cm[ixao]*
%{_libdir}/ocaml/netzip/*.a
%{_libdir}/ocaml/site-lib/netzip

%files pop3-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/pop
%{_libdir}/ocaml/pop/*.cm[ixao]*
%{_libdir}/ocaml/pop/*.a
%{_libdir}/ocaml/site-lib/pop
%{_examplesdir}/%{name}-pop3-%{version}

%files rpc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ocamlrpcgen
%dir %{_libdir}/ocaml/rpc-auth-local
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllrpc_auth_local.so
%{_libdir}/ocaml/stublibs/dllrpc_auth_local.so.owner

%files rpc-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/rpc
%dir %{_libdir}/ocaml/rpc-auth-dh
%dir %{_libdir}/ocaml/rpc-generator
%dir %{_libdir}/ocaml/rpc-ssl
%{_libdir}/ocaml/rpc-generator/rpcgen-packlist
%{_libdir}/ocaml/rpc*/*.cm[ixao]*
%{_libdir}/ocaml/rpc*/*.a
%{_libdir}/ocaml/site-lib/rpc*
%{_examplesdir}/%{name}-rpc-%{version}

%files shell-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/shell
%{_libdir}/ocaml/shell/*.cm[ixao]*
%{_libdir}/ocaml/shell/*.a
%{_libdir}/ocaml/site-lib/shell

%files smtp-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/smtp
%{_libdir}/ocaml/smtp/*.cm[ixao]*
%{_libdir}/ocaml/smtp/*.a
%{_libdir}/ocaml/site-lib/smtp
