#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)
%bcond_with	apache		# build apache module

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		apxs	/usr/sbin/apxs
%define		apache	/usr/sbin/httpd
Summary:	Modules for Internet programming in OCaml
Summary(pl.UTF-8):	Moduły ułatwiające pisanie programów internetowych w OCamlu
Name:		ocaml-net
Version:	4.1.9
Release:	1
License:	GPL v2+ (nethttpd), LGPL v2+ (mod_netcgi), BSD-like (the rest)
Group:		Libraries
Source0:	http://download.camlcity.org/download/ocamlnet-%{version}.tar.gz
# Source0-md5:	3812d76b325903412bb27e5a656df689
Patch0:		%{name}-buildfix.patch
Patch1:		%{name}-lablgtk2.patch
Patch2:		%{name}-apache-link.patch
URL:		http://projects.camlcity.org/projects/ocamlnet.html
%if %{with apache}
BuildRequires:	%{apache}
BuildRequires:	%{apxs}
BuildRequires:	apache-devel >= 2.0
%endif
BuildRequires:	ncurses-devel
BuildRequires:	ocaml >= 1:3.09.2
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml-cryptokit-devel
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-lablgtk2-devel >= 2.14.2
BuildRequires:	ocaml-labltk-devel
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-ssl-devel
BuildRequires:	ocaml-zip-devel
BuildRequires:	rpm-build >= 4.6
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
Group:		Documentation
BuildArch:	noarch

%description doc
ocaml-net documentation.

%description doc -l pl.UTF-8
Dokumentacja dla pakietów ocaml-net.

%package netcgi
Summary:	Common Gateway Interface library
Summary(pl.UTF-8):	Biblioteka do tworzenia skryptów CGI
Group:		Libraries
License:	BSD-like
%requires_eq	ocaml-runtime
Conflicts:	ocaml-net-netcgi-devel < 4.1.9-1

%description netcgi
Common Gateway Interface library, part of Ocamlnet.

%description netcgi -l pl.UTF-8
Biblioteka do tworzenia skryptów CGI, część pakietu Ocamlnet.

%package netcgi-devel
Summary:	Common Gateway Interface library - development part
Summary(pl.UTF-8):	Biblioteka do tworzenia skryptów CGI - część programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netplex-devel = %{version}-%{release}
Requires:	%{name}-netstring-devel = %{version}-%{release}
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml
Obsoletes:	ocaml-net-cgi-devel < 3

%description netcgi-devel
Common Gateway Interface library, part of Ocamlnet. This package
contains files needed to develop OCaml programs using netcgi library.

%description netcgi-devel -l pl.UTF-8
Biblioteka do tworzenia skryptów CGI, część pakietu Ocamlnet. Ten
pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netcgi.

%package -n apache-mod_netcgi
Summary:	Apache mod_netcfg module
Summary(pl.UTF-8):	Moduł Apache'a mod_netcgi
License:	LGPL v2+
Group:		Networking/Daemons/HTTP
Requires:	apache(modules-api) = %apache_modules_api

%description -n apache-mod_netcgi
Apache mod_netcfg module.

%description -n apache-mod_netcgi -l pl.UTF-8
Moduł Apache'a mod_netcgi.

%package equeue
Summary:	Event queue library for OCaml
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń dla OCamla
Group:		Libraries
License:	BSD-like
%requires_eq	ocaml-runtime
Conflicts:	ocaml-net-equeue-devel < 4.1.9-1

%description equeue
Equeue provides a generic event queue module, and a specific module
for file descriptor events.

%description equeue -l pl.UTF-8
Equeue dostarcza ogólnego modułu obsługi kolejki zdarzeń jak również
modułu obsługi zdarzeń na deskryptorach plików.

%package equeue-devel
Summary:	Event queue library for OCaml - development part
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń dla OCamla - część programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml
Obsoletes:	ocaml-equeue-devel < 2.2

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

%package equeue-gtk2
Summary:	GTK2 event queue library for OCaml
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń GTK2 dla OCamla
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime
Conflicts:	ocaml-net-equeue-gtk2-devel < 4.1.9-1

%description equeue-gtk2
Equeue provides a generic event queue module, and a specific module
for file descriptor events.

%description equeue-gtk2 -l pl.UTF-8
Equeue dostarcza ogólnego modułu obsługi kolejki zdarzeń jak również
modułu obsługi zdarzeń na deskryptorach plików.

%package equeue-gtk2-devel
Summary:	GTK2 event queue library for OCaml - development part
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń GTK2 dla OCamla - część programistyczna
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

%package equeue-tcl
Summary:	Event queue library for OCaml, Tcl support
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń dla OCamla, wsparcie dla Tcl
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime
%requires_eq	ocaml-labltk
Obsoletes:	ocaml-equeue-tcl < 2.2

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
%requires_eq	ocaml
%requires_eq	ocaml-labltk-devel
Obsoletes:	ocaml-equeue-tcl-devel < 2.2

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

%package netcamlbox
Summary:	Fast IPC mechanism for OCaml
Summary(pl.UTF-8):	Szybki mechanizm IPC dla OCamla
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime
Conflicts:	ocaml-net-netcamlbox-devel < 4.1.9-1

%description netcamlbox
Camlboxes are a fast IPC mechanism to send Ocaml values from one
process to another. Source and destination processes must run on the
same machine (no network). The Ocaml value is copied to a shared
memory object where it can be directly accessed by the receiver
without unmarshalling step. This means the sender writes the value
into the shared memory in a format that can immediately interpreted by
the receiver.

%description netcamlbox -l pl.UTF-8
Camlboksy są szybkim mechanizmem IPC do przesyłania danych Ocamla
pomiędzy procesami. Nadawca i odbiorca muszą być uruchomione na tej
samej maszynie. Dane Ocamla są kopiowane do segmentu pamięci
dzielonej, gdzie mogą byc bezpośrednio odczytywane przez odbiorcę.

%package netcamlbox-devel
Summary:	Fast IPC mechanism for OCaml - development part
Summary(pl.UTF-8):	Szybki mechanizm IPC dla OCamla - część programistyczna
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
Camlboksy są szybkim mechanizmem IPC do przesyłania danych Ocamla
pomiędzy procesami. Nadawca i odbiorca muszą być uruchomione na tej
samej maszynie. Dane Ocamla są kopiowane do segmentu pamięci
dzielonej, gdzie mogą byc bezpośrednio odczytywane przez odbiorcę.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netcamlbox.

%package netclient
Summary:	HTTP 1.1 client for OCaml
Summary(pl.UTF-8):	Klient HTTP 1.1 dla OCamla
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime
Conflicts:	ocaml-net-netclient-devel < 4.1.9-1

%description netclient
Implements much of HTTP/1.1. Implements the following advanced
features: chunked messages; persistent connections; connections in
pipelining mode ("full duplex" connections); modular authentication
methods, currently Basic and Digest; event-driven implementation;
allows concurrent service for several network connections.

%description netclient -l pl.UTF-8
Biblioteka netclient implementuje większość HTTP/1.1, a także
następujące zaawansowane właściwości: komunikaty w kawałkach;
połączenia stałe; połączenia w trybie "full duplex"; modularne metody
uwierzytelniania, obecnie Basic i Digest; implementacja oparta na
zdarzeniach; umożliwia jednoczesną obsługę kilku połączeń.

%package netclient-devel
Summary:	HTTP 1.1 client for OCaml - development part
Summary(pl.UTF-8):	Klient HTTP 1.1 dla OCamla - część programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	%{name}-netstring-devel = %{version}-%{release}
%requires_eq	ocaml
Obsoletes:	ocaml-netclient-devel < 1

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

%package netgss-system
Summary:	GSS-API generic definition
Summary(pl.UTF-8):	Biblioteka do obsługi protokołu GSSAPI
License:	GPL v2+
Group:		Libraries
Requires:	%{name}-netstring = %{version}-%{release}
Requires:	%{name}-netsys = %{version}-%{release}
%requires_eq	ocaml-runtime

%description netgss-system
GSSAPI library, part of Ocamlnet. This package contains the files
needed to develop OCaml programs using netgss-system library.

%description netgss-system -l pl.UTF-8
Biblioteka do obsługi protokołu GSSAPI, część pakietu Ocamlnet. Ten
pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netgss-system.

%package netgss-system-devel
Summary:	GSS-API generic definition - development part
Summary(pl.UTF-8):	Biblioteka do obsługi protokołu GSSAPI - część programistyczna
License:	GPL v2+
Group:		Development/Libraries
Requires:	%{name}-netgss-system-devel = %{version}-%{release}
Requires:	%{name}-netstring-devel = %{version}-%{release}
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml

%description netgss-system-devel
GSSAPI library, part of Ocamlnet. This package contains the files
needed to develop OCaml programs using netgss-system library.

%description netgss-system-devel -l pl.UTF-8
Biblioteka do obsługi protokołu GSSAPI, część pakietu Ocamlnet. Ten
pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netgss-system.

%package nethttpd
Summary:	HTTPd library
Summary(pl.UTF-8):	Biblioteka do obsługi protokołu HTTP
License:	GPL v2+
Group:		Libraries
%requires_eq	ocaml-runtime
Conflicts:	ocaml-net-nethttpd-devel < 4.1.9-1

%description nethttpd
HTTPd library, part of Ocamlnet.

%description nethttpd -l pl.UTF-8
Biblioteka do obsługi protokołu HTTP, część pakietu Ocamlnet.

%package nethttpd-devel
Summary:	HTTPd library - development part
Summary(pl.UTF-8):	Biblioteka do obsługi protokołu HTTP - część programistyczna
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

%package netmulticore
Summary:	Multi-processing for compute jobs
Summary(pl.UTF-8):	Obsługa wieloprocesorowych obliczeń
License:	GPL v2+
Group:		Libraries
%requires_eq	ocaml-runtime
Conflicts:	ocaml-net-netmulticore-devel < 4.1.9-1

%description netmulticore
Netmcore library, part of Ocamlnet.

%description netmulticore -l pl.UTF-8
Biblioteka do obsługi wieloprocesorowych obliczeń, część pakietu
Ocamlnet.

%package netmulticore-devel
Summary:	Multi-processing for compute jobs - development part
Summary(pl.UTF-8):	Obsługa wieloprocesorowych obliczeń - część programistyczna
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
%requires_eq	ocaml-labltk
%requires_eq	ocaml-runtime

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

%package netshm
Summary:	Shared memory support
Summary(pl.UTF-8):	Obsługa pamięci dzielonej
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime
Conflicts:	ocaml-net-netshm-devel < 4.1.9-1

%description netshm
Shared memory support.

%description netshm -l pl.UTF-8
Obsługa pamięci dzielonej.

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
%requires_eq	ocaml-pcre
%requires_eq	ocaml-runtime

%description netstring
String processing library, part of Ocamlnet.

%description netstring -l pl.UTF-8
Biblioteka do przetwarzania napisów, część pakietu Ocamlnet.

%package netstring-devel
Summary:	String processing library - development part
Summary(pl.UTF-8):	Biblioteka do przetwarzania napisów - część programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netstring = %{version}-%{release}
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml
%requires_eq	ocaml-pcre-devel

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

%package netunidata
Summary:	Unicode lookup tables
Summary(pl.UTF-8):	Tablice wyszukiwania Unicode
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime
Conflicts:	ocaml-net-netunidata-devel < 4.1.9-1

%description netunidata
Unicode lookup tables.

%description netunidata -l pl.UTF-8
Tablice wyszukiwania Unicode.

%package netunidata-devel
Summary:	Unicode lookup tables - development part
Summary(pl.UTF-8):	Tablice wyszukiwania Unicode - część programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netstring-devel = %{version}-%{release}
%requires_eq	ocaml

%description netunidata-devel
Unicode lookup tables.

This package contains files needed to develop OCaml programs using
netunidata library.

%description netunidata-devel -l pl.UTF-8
Tablice wyszukiwania Unicode.

Ten pakiet zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki netunidata.

%package netzip
Summary:	Gzip channels
Summary(pl.UTF-8):	Funkcje do kompresji kanałów
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime
Conflicts:	ocaml-net-netzip-devel < 4.1.9-1

%description netzip
Gzip channels functions.

%description netzip -l pl.UTF-8
Funkcje do kompresji kanałów.

%package netzip-devel
Summary:	Gzip channels - development part
Summary(pl.UTF-8):	Funkcje do kompresji kanałów - cześć programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-netstring-devel = %{version}-%{release}
%requires_eq	ocaml

%description netzip-devel
Gzip channels functions.

This package contains files needed to develop OCaml programs using
netzip library.

%description netzip-devel -l pl.UTF-8
Funkcje do kompresji kanałów.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki netzip.

%package rpc
Summary:	Remote Procedure Call (RPC) libraries
Summary(pl.UTF-8):	Biblioteki do obsługi RPC
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime

%description rpc
Remote Procedure Call (RPC) libraries.

%description rpc -l pl.UTF-8
Biblioteki do obsługi RPC.

%package rpc-devel
Summary:	Remote Procedure Call (RPC) libraries - development part
Summary(pl.UTF-8):	Biblioteki do obsługi RPC - część programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-rpc = %{version}-%{release}
%requires_eq	ocaml

%description rpc-devel
Remote Procedure Call (RPC) libraries.

This package contains files needed to develop OCaml programs using rpc
library.

%description rpc-devel -l pl.UTF-8
Biblioteki do obsługi RPC.

Ten pakiet zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki rpc.

%package shell
Summary:	Unix shell functions
Summary(pl.UTF-8):	Funkcje powłoki uniksowej
License:	BSD-like
Group:		Libraries
%requires_eq	ocaml-runtime
Conflicts:	ocaml-net-shell-devel < 4.1.9-1

%description shell
Unix shell functions.

%description shell -l pl.UTF-8
Funkcje powłoki uniksowej.

%package shell-devel
Summary:	Unix shell functions - development part
Summary(pl.UTF-8):	Funkcje powłoki uniksowej - część programistyczna
License:	BSD-like
Group:		Development/Libraries
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml

%description shell-devel
Unix shell functions.

This package contains files needed to develop OCaml programs using
shell library.

%description shell-devel -l pl.UTF-8
Funkcje powłoki uniksowej.

Ten pakiet zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki shell.

%prep
%setup -q -n ocamlnet-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# no %%configure, please
./configure \
	-datadir %{_datadir}/%{name} \
	-disable-gtk \
	-enable-gtk2 \
	-enable-zip \
	-enable-gssapi \
%if %{with apache}
	-enable-apache \
%else
	-disable-apache \
%endif
	-enable-tcl \
	-equeue-tcl-libs "-ltcl" \
	-with-nethttpd \
	-apxs %{apxs} \
	-apache %{apache}

%{__make} -j1 all %{?with_ocaml_opt:opt}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/ocaml/stublibs,%{_apachepkglibdir},%{_apachesysconfdir}}

%{__make} -j1 install \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with apache}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/netcgi2-apache/500netcgi_apache.info
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
%endif

# GPL
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/nethttpd/LICENSE
# useless in rpm
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs/*.so.owner

# not sure about *.o
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/*/*.mli

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-{netcgi,equeue,netcamlbox,netmulticore,netclient,nethttpd,rpc}-%{version}
cp -pr examples/camlbox/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-netcamlbox-%{version}
cp -pr examples/cgi/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-netcgi-%{version}
cp -pr examples/equeue/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-equeue-%{version}
cp -pr examples/multicore/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-netmulticore-%{version}
cp -pr examples/netclient/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-netclient-%{version}
cp -pr examples/nethttpd/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-nethttpd-%{version}
cp -pr examples/rpc/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-rpc-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files doc
%defattr(644,root,root,755)
%doc LICENSE* ChangeLog RELNOTES doc/html-main

%files netcgi
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netcgi2
%{_libdir}/ocaml/netcgi2/META
%{_libdir}/ocaml/netcgi2/*.cma
%dir %{_libdir}/ocaml/netcgi2-plex
%{_libdir}/ocaml/netcgi2-plex/META
%{_libdir}/ocaml/netcgi2-plex/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/netcgi2/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/netcgi2-plex/*.cmxs
%endif

%files netcgi-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netcgi2/*.cmi
%{_libdir}/ocaml/netcgi2-plex/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/netcgi2/*.a
%{_libdir}/ocaml/netcgi2/*.cmxa
%{_libdir}/ocaml/netcgi2-plex/*.a
%{_libdir}/ocaml/netcgi2-plex/*.cmxa
%endif
%{_examplesdir}/%{name}-netcgi-%{version}

%if %{with apache}
%files -n apache-mod_netcgi
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_apachesysconfdir}/*_mod_netcgi.conf
%attr(755,root,root) %{_apachepkglibdir}/mod_netcgi.so
%endif

%files equeue
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/equeue
%{_libdir}/ocaml/equeue/META
%{_libdir}/ocaml/equeue/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/equeue/*.cmxs
%endif

%files equeue-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/equeue/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/equeue/*.a
%{_libdir}/ocaml/equeue/*.cmxa
%endif
%{_examplesdir}/%{name}-equeue-%{version}

%files equeue-gtk2
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/equeue-gtk2
%{_libdir}/ocaml/equeue-gtk2/META
%{_libdir}/ocaml/equeue-gtk2/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/equeue-gtk2/*.cmxs
%endif

%files equeue-gtk2-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/equeue-gtk2/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/equeue-gtk2/*.a
%{_libdir}/ocaml/equeue-gtk2/*.cmxa
%endif

%files equeue-tcl
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/equeue-tcl
%{_libdir}/ocaml/equeue-tcl/META
%{_libdir}/ocaml/equeue-tcl/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/equeue-tcl/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllequeue_tcl.so

%files equeue-tcl-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/equeue-tcl/*.cmi
%{_libdir}/ocaml/equeue-tcl/libequeue_tcl*.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/equeue-tcl/*.cmxa
%{_libdir}/ocaml/equeue-tcl/equeue_tcl*.a
%endif

%files netcamlbox
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netcamlbox
%{_libdir}/ocaml/netcamlbox/META
%{_libdir}/ocaml/netcamlbox/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/netcamlbox/*.cmxs
%endif

%files netcamlbox-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netcamlbox/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/netcamlbox/*.a
%{_libdir}/ocaml/netcamlbox/*.cmxa
%endif
%{_examplesdir}/%{name}-netcamlbox-%{version}

%files netclient
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netclient
%{_libdir}/ocaml/netclient/META
%{_libdir}/ocaml/netclient/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/netclient/*.cmxs
%endif

%files netclient-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netclient/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/netclient/*.a
%{_libdir}/ocaml/netclient/*.cmxa
%endif
%{_examplesdir}/%{name}-netclient-%{version}

%files netgss-system
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netgss-system
%{_libdir}/ocaml/netgss-system/META
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllnetgss-system.so
%{_libdir}/ocaml/netgss-system/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/netgss-system/*.cmxs
%endif

%files netgss-system-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netgss-system/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/netgss-system/*.cmxa
%{_libdir}/ocaml/netgss-system/netgss-system*.a
%endif
%{_libdir}/ocaml/netgss-system/libnetgss-system*.a

%files nethttpd
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/nethttpd
%{_libdir}/ocaml/nethttpd/META
%{_libdir}/ocaml/nethttpd/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/nethttpd/*.cmxs
%endif

%files nethttpd-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/nethttpd/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/nethttpd/*.a
%{_libdir}/ocaml/nethttpd/*.cmxa
%endif
%{_examplesdir}/%{name}-nethttpd-%{version}

%files netmulticore
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netmulticore
%{_libdir}/ocaml/netmulticore/META
%{_libdir}/ocaml/netmulticore/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/netmulticore/*.cmxs
%endif

%files netmulticore-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netmulticore/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/netmulticore/*.a
%{_libdir}/ocaml/netmulticore/*.cmxa
%endif
%{_examplesdir}/%{name}-netmulticore-%{version}

%files netplex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/netplex-admin
%dir %{_libdir}/ocaml/netplex
%{_libdir}/ocaml/netplex/META
%{_libdir}/ocaml/netplex/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/netplex/*.cmxs
%endif

%files netplex-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netplex/netplex-packlist
%{_libdir}/ocaml/netplex/*.cmi
%{_libdir}/ocaml/netplex/*.cmo
%if %{with ocaml_opt}
%{_libdir}/ocaml/netplex/*.a
%{_libdir}/ocaml/netplex/*.cmx
%{_libdir}/ocaml/netplex/*.cmxa
%{_libdir}/ocaml/netplex/*.o
%endif

%files netshm
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netshm
%{_libdir}/ocaml/netshm/META
%{_libdir}/ocaml/netshm/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/netshm/*.cmxs
%endif

%files netshm-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netshm/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/netshm/*.a
%{_libdir}/ocaml/netshm/*.cmxa
%endif

%files netstring
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netstring
%{_libdir}/ocaml/netstring/META
%{_libdir}/ocaml/netstring/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/netstring/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllnetaccel_c.so

%files netstring-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netstring/*.cmi
%{_libdir}/ocaml/netstring/*.cmo
%{_libdir}/ocaml/netstring/libnetaccel_c.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/netstring/*.cmx
%{_libdir}/ocaml/netstring/*.cmxa
%{_libdir}/ocaml/netstring/*.o
%{_libdir}/ocaml/netstring/netstring*.a
%endif

%files netsys
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netsys
%{_libdir}/ocaml/netsys/META
%{_libdir}/ocaml/netsys/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/netsys/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllnetsys.so

%files netsys-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netsys/*.cmi
%{_libdir}/ocaml/netsys/*.cmo
%{_libdir}/ocaml/netsys/libnetsys*.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/netsys/*.cmx
%{_libdir}/ocaml/netsys/*.cmxa
%{_libdir}/ocaml/netsys/*.o
%{_libdir}/ocaml/netsys/netsys*.a
%endif
%{_libdir}/ocaml/netsys/netsys_c_event.h

%files netunidata
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netunidata
%{_libdir}/ocaml/netunidata/META
%{_libdir}/ocaml/netunidata/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/netunidata/*.cmxs
%endif
%dir %{_datadir}/ocaml-net
%{_datadir}/ocaml-net/cmap*.*.netdb

%files netunidata-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netunidata/*.cmi
%{_libdir}/ocaml/netunidata/*.cmo
%if %{with ocaml_opt}
%{_libdir}/ocaml/netunidata/*.a
%{_libdir}/ocaml/netunidata/*.cmx
%{_libdir}/ocaml/netunidata/*.cmxa
%{_libdir}/ocaml/netunidata/*.o
%endif

%files netzip
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netzip
%{_libdir}/ocaml/netzip/META
%{_libdir}/ocaml/netzip/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/netzip/*.cmxs
%endif

%files netzip-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netzip/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/netzip/*.a
%{_libdir}/ocaml/netzip/*.cmxa
%endif

%files rpc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ocamlrpcgen
%dir %{_libdir}/ocaml/rpc
%{_libdir}/ocaml/rpc/META
%{_libdir}/ocaml/rpc/*.cma
%dir %{_libdir}/ocaml/rpc-auth-local
%{_libdir}/ocaml/rpc-auth-local/META
%{_libdir}/ocaml/rpc-auth-local/*.cma
%dir %{_libdir}/ocaml/rpc-generator
%{_libdir}/ocaml/rpc-generator/META
%{_libdir}/ocaml/rpc-generator/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/rpc/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/rpc-auth-local/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/rpc-generator/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllrpc_auth_local.so

%files rpc-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/rpc/*.cmi
%{_libdir}/ocaml/rpc-auth-local/*.cmi
%{_libdir}/ocaml/rpc-auth-local/librpc_auth_local*.a
%{_libdir}/ocaml/rpc-generator/rpcgen-packlist
%{_libdir}/ocaml/rpc-generator/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/rpc/rpc*.a
%{_libdir}/ocaml/rpc/rpc*.cmxa
%{_libdir}/ocaml/rpc-auth-local/rpc*.a
%{_libdir}/ocaml/rpc-auth-local/rpc*.cmxa
%{_libdir}/ocaml/rpc-generator/rpc*.a
%{_libdir}/ocaml/rpc-generator/rpc*.cmxa
%endif
%{_examplesdir}/%{name}-rpc-%{version}

%files shell
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/shell
%{_libdir}/ocaml/shell/META
%{_libdir}/ocaml/shell/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/shell/*.cmxs
%endif

%files shell-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/shell/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/shell/*.a
%{_libdir}/ocaml/shell/*.cmxa
%endif
