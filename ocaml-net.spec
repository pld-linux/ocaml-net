# TODO:
# - nethttpd needs to be packaged
# - apache stuff
# - lablgtk2 support
#
%define		ocaml_ver	1:3.09.2
Summary:	Modules for Internet programming in OCaml
Summary(pl.UTF-8):	Moduły ułatwiające pisanie programów internetowych w OCamlu
Name:		ocaml-net
Version:	2.2.9
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/ocamlnet/ocamlnet-%{version}.tar.gz
# Source0-md5:	3655e3be3bb2806e0a1f48bb7ce16fb3
URL:		http://ocamlnet.sourceforge.net/
BuildRequires:	ncurses-devel
BuildRequires:	ocaml >= %{ocaml_ver}
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-pcre-devel
#BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:	ocaml-ssl-devel
BuildRequires:	ocaml-labltk-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modules for Internet programming in OCaml.

%description -l pl.UTF-8
Moduły ułatwiające pisanie programów internetowych w OCamlu.

%package doc
Summary:	ocaml-net documentation
Summary(pl.UTF-8):	Dokumentacja dla pakietów ocaml-net
Group:		Development/Libraries

%description doc
ocaml-net documentation.

%description doc -l pl.UTF-8
Dokumentacja dla pakietów ocaml-net.

%package cgi-devel
Summary:	Common Gateway Interface library
Summary(pl.UTF-8):	Biblioteka do tworzenia skryptów CGI
Group:		Development/Libraries
Requires:	%{name}-netplex-devel = %{version}-%{release}
Requires:	%{name}-netstring-devel = %{version}-%{release}
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml

%description cgi-devel
Common Gateway Interface library, part of Ocamlnet. This package
contains files needed to develop OCaml programs using this library.

%description cgi-devel -l pl.UTF-8
Biblioteka do tworzenia skryptów CGI, część pakietu Ocamlnet. Pakiet
ten zawiera pliki niezbędne do tworzenia programów używających tej
biblioteki.

%package equeue-devel
Summary:	Event queue library for OCaml
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń dla OCamla
Group:		Development/Libraries
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml
Obsoletes:	ocaml-equeue-devel
Obsoletes:	ocaml-equeue-tcl
Obsoletes:	ocaml-equeue-tcl-devel

%description equeue-devel
Equeue provides a generic event queue module, and a specific module
for file descriptor events.

This package contains files needed to develop OCaml programs using
this library.

%description equeue-devel -l pl.UTF-8
Equeue dostarcza ogólnego modułu obsługi kolejki zdarzeń jak również
modułu obsługi zdarzeń na deskryptorach plików.

Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
tej biblioteki.

%package equeue-ssl
Summary:	Event queue library for OCaml, SSL support
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń dla OCamla, wsparcie dla SSL
Group:		Libraries
%requires_eq	ocaml-runtime

%description equeue-ssl
This package makes it possible to let Equeue cooperate with the event
queue implementation of SSL.

This package contains files needed to run bytecode executables using
this library.

%description equeue-ssl -l pl.UTF-8
Pakiet ten umożliwia współpracę Equeue z implementacją kolejki zdarzeń
w SSL.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających tej biblioteki.

%package equeue-ssl-devel
Summary:	Equeue SSL support - development part
Summary(pl.UTF-8):	Wsparcie dla SSL-a w equeue - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	%{name}-ssl = %{version}-%{release}
%requires_eq	ocaml-ssl-devel
%requires_eq	ocaml

%description equeue-ssl-devel
This package makes it possible to let Equeue cooperate with the event
queue implementation of SSL.

This package contains files needed to develop OCaml programs using
this library.

%description equeue-ssl-devel -l pl.UTF-8
Pakiet ten umożliwia współpracę Equeue z implementacją kolejki zdarzeń
w SSL.

Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
tej biblioteki.

%package equeue-tcl
Summary:	Event queue library for OCaml, Tcl support
Summary(pl.UTF-8):	Biblioteka obsługująca kolejkę zdarzeń dla OCamla, wsparcie dla Tcl
Group:		Libraries
%requires_eq	ocaml-runtime
%requires_eq	ocaml-labltk

%description equeue-tcl
This package makes it possible to let Equeue cooperate with the event
queue implementation of Tcl.

This package contains files needed to run bytecode executables using
this library.

%description equeue-tcl -l pl.UTF-8
Pakiet ten umożliwia współpracę Equeue z implementacją kolejki zdarzeń
w Tcl.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających tej biblioteki.

%package equeue-tcl-devel
Summary:	Equeue Tcl support - development part
Summary(pl.UTF-8):	Wsparcie dla Tcl-a w equeue - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	%{name}-equeue-tcl = %{version}-%{release}
%requires_eq	ocaml-labltk-devel
%requires_eq	ocaml

%description equeue-tcl-devel
This package makes it possible to let Equeue cooperate with the event
queue implementation of Tcl.

This package contains files needed to develop OCaml programs using
this library.

%description equeue-tcl-devel -l pl.UTF-8
Pakiet ten umożliwia współpracę Equeue z implementacją kolejki zdarzeń
w Tcl.

Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
tej biblioteki.

%package netclient-devel
Summary:	HTTP 1.1 client for OCaml
Summary(pl.UTF-8):	Klient HTTP 1.1 dla OCamla
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
this library.

%description netclient-devel -l pl.UTF-8
Implementuje większość HTTP/1.1. Implementuje również następujące
zaawansowane własności: komunikaty w kawałkach; połączenia stałe;
połączenia w trybie "full duplex"; modularne metody autentykacji,
obecnie Basic i Digest; bazowna na zdarzeniach implementacja;
umożliwia jednoczesną obsługę kilku połączeń.

Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
tej biblioteki.

%package nethttpd-devel
Summary:	HTTPd library
Summary(pl.UTF-8):	Biblioteka do obsługi protokołu HTTP
Group:		Development/Libraries
Requires:	%{name}-cgi-devel = %{version}-%{release}
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	%{name}-netplex-devel = %{version}-%{release}
%requires_eq	ocaml-pcre-devel
%requires_eq	ocaml

%description nethttpd-devel
HTTPd library, part of Ocamlnet. This package contains the files
needed to develop OCaml programs using this library.

%description nethttpd-devel -l pl.UTF-8
Biblioteka do obsługi protokołu HTTP, część pakietu Ocamlnet. Pakiet
ten zawiera pliki niezbędne do tworzenia programów używających tej
biblioteki.

%package netplex
Summary:	Server framework
#Summary(pl.UTF-8):	
Group:		Libraries
%requires_eq	ocaml-runtime
%requires_eq	ocaml-labltk

%description netplex
Server framework.

This package contains files needed to run bytecode executables using
this library.

#%description netplex -l pl.UTF-8
#
#Pakiet ten zawiera binaria potrzebne do uruchamiania programów
#używających tej biblioteki.

%package netplex-devel
Summary:	Server framework - development part
#Summary(pl.UTF-8):	 - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name}-netplex = %{version}-%{release}
Requires:	%{name}-equeue-devel = %{version}-%{release}
Requires:	%{name}-netstring-devel = %{version}-%{release}
Requires:	%{name}-rpc-devel = %{version}-%{release}
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml

%description netplex-devel
Server framework.

This package contains files needed to develop OCaml programs using
this library.

#%description netplex-devel -l pl.UTF-8
#
#Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
#tej biblioteki.

%package netshm-devel
Summary:	Shared memory support - development part
#Summary(pl.UTF-8):	 - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml

%description netshm-devel
Shared memory support.

This package contains files needed to develop OCaml programs using
this library.

#%description netshm-devel -l pl.UTF-8
#
#Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
#tej biblioteki.

%package netstring-devel
Summary:	String processing library
Summary(pl.UTF-8):	Biblioteka do przetwarzania napisów
Group:		Development/Libraries
Requires:	%{name}-netsys-devel = %{version}-%{release}
%requires_eq	ocaml-pcre-devel
%requires_eq	ocaml

%description netstring-devel
String processing library, part of Ocamlnet. This package contains
files needed to develop OCaml programs using this library.

%description netstring-devel -l pl.UTF-8
Biblioteka do przetwarzania napisów, część pakietu Ocamlnet. Pakiet
ten zawiera pliki niezbędne do tworzenia programów używających tej
biblioteki.

%package netsys
Summary:	OS-specific functions
#Summary(pl.UTF-8):	
Group:		Libraries
%requires_eq	ocaml-runtime

%description netsys
OS-specific functions.

This package contains files needed to run bytecode executables using
this library.

#%description netsys -l pl.UTF-8
#
#Pakiet ten zawiera binaria potrzebne do uruchamiania programów
#używających tej biblioteki.

%package netsys-devel
Summary:	OS-specific functions - development part
#Summary(pl.UTF-8):	 - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name}-netsys = %{version}-%{release}
%requires_eq	ocaml

%description netsys-devel
OS-specific functions.

This package contains files needed to develop OCaml programs using
this library.

#%description netsys-devel -l pl.UTF-8
#
#Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
#tej biblioteki.

%package pop3-devel
Summary:	Post Office Protocol (POP3) library
Summary(pl.UTF-8):	Biblioteka do obsługi POP3
Group:		Development/Libraries
Requires:	%{name}-netstring-devel = %{version}-%{release}
%requires_eq	ocaml

%description pop3-devel
Post Office Protocol (POP3) library, part of Ocamlnet. This package
contains files needed to develop OCaml programs using this library.

%description pop3-devel -l pl.UTF-8
Biblioteka do obsługi POP3, część pakietu Ocamlnet. Pakiet ten zawiera
pliki niezbędne do tworzenia programów używających tej biblioteki.

%package rpc
Summary:	Remote Procedure Call (RPC) library
Summary(pl.UTF-8):	Biblioteka do obsługi RPC
Group:		Development/Libraries
Requires:	%{name}-equeue-ssl = %{version}-%{release}
%requires_eq	ocaml

%description rpc
Remote Procedure Call (RPC) library.

%description rpc -l pl.UTF-8
Biblioteka do obsługi RPC.

%package rpc-devel
Summary:	Remote Procedure Call (RPC) library
Summary(pl.UTF-8):	Biblioteka do obsługi RPC
Group:		Development/Libraries
Requires:	%{name}-equeue-ssl-devel = %{version}-%{release}
Requires:	%{name}-rpc = %{version}-%{release}
%requires_eq	ocaml

%description rpc-devel
Remote Procedure Call (RPC) library.

%description rpc-devel -l pl.UTF-8
Biblioteka do obsługi RPC.

%package shell-devel
Summary:	Unix shell functions
#Summary(pl.UTF-8):	
Group:		Development/Libraries
Requires:	%{name}-netsys-devel = %{version}-%{release}
Requires:	%{name}-equeue-devel = %{version}-%{release}
%requires_eq    ocaml

%description shell-devel
Unix shell functions.

#%description shell-devel -l pl.UTF-8

%package smtp-devel
Summary:	Simple Mail Transfer Protocol (SMTP) library
Summary(pl.UTF-8):	Biblioteka do obsługi SMTP
Group:		Development/Libraries
Requires:	%{name}-netstring-devel = %{version}-%{release}
%requires_eq    ocaml

%description smtp-devel
Interface for the Simple Mail Tranfer Protocol (SMTP) as specified by
RFC 2821.

%description smtp-devel -l pl.UTF-8
Interfejs dla protokołu SMTP wyszczególniony w RFC 2821.

%prep
%setup -q -n ocamlnet-%{version}

%build
# no %%configure, please
./configure \
	-disable-gtk \
	-disable-gtk2 \
	-enable-ssl \
	-enable-tcl \
	-equeue-tcl-libs "-ltcl" \
	-with-nethttpd

%{__make} -j1 all opt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml

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
# cgi is a special case
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/cgi
mv $RPM_BUILD_ROOT%{_libdir}/ocaml/cgi/META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/cgi/
cd ..

# not sure about *.o
rm $RPM_BUILD_ROOT%{_libdir}/ocaml/*/*.mli

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-{cgi,equeue,netclient,nethttpd,pop3,rpc}-%{version}
cp -r examples/cgi/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-cgi-%{version}
cp -r examples/equeue/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-equeue-%{version}
cp -r examples/netclient/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-netclient-%{version}
cp -r examples/nethttpd/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-nethttpd-%{version}
cp -r examples/pop/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-pop3-%{version}
cp -r examples/rpc/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-rpc-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files doc
%defattr(644,root,root,755)
%doc LICENSE* ChangeLog RELNOTES doc/html-main

%files cgi-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netcgi*
%{_libdir}/ocaml/netcgi*/*.cm[ixao]*
%{_libdir}/ocaml/netcgi*/*.a
%{_libdir}/ocaml/site-lib/*cgi*
%{_examplesdir}/%{name}-cgi-%{version}

%files equeue-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/equeue
%{_libdir}/ocaml/equeue/*.cm[ixao]*
%{_libdir}/ocaml/equeue/*.a
%{_libdir}/ocaml/equeue/*.o
%{_libdir}/ocaml/site-lib/equeue
%{_examplesdir}/%{name}-equeue-%{version}

%files equeue-ssl
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/equeue-ssl
%attr(755,root,root) %{_libdir}/ocaml/equeue-ssl/*.so

%files equeue-ssl-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/equeue-ssl/*.cm[ixao]*
%{_libdir}/ocaml/equeue-ssl/*.a
%{_libdir}/ocaml/site-lib/equeue-ssl

%files equeue-tcl
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/equeue-tcl
%attr(755,root,root) %{_libdir}/ocaml/equeue-tcl/*.so

%files equeue-tcl-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/equeue-tcl/*.cm[ixao]*
%{_libdir}/ocaml/equeue-tcl/*.a
%{_libdir}/ocaml/site-lib/equeue-tcl

%files netclient-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netclient
%{_libdir}/ocaml/netclient/*.cm[ixao]*
%{_libdir}/ocaml/netclient/*.a
%{_libdir}/ocaml/netclient/*.o
%{_libdir}/ocaml/site-lib/netclient
%{_examplesdir}/%{name}-netclient-%{version}

%files nethttpd-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/nethttpd-*
%{_libdir}/ocaml/nethttpd-*/*.cm[ixao]*
%{_libdir}/ocaml/nethttpd-*/*.a
%{_libdir}/ocaml/site-lib/nethttpd*
%{_examplesdir}/%{name}-nethttpd-%{version}

%files netplex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/netplex-admin

%files netplex-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netplex
%{_libdir}/ocaml/netplex/netplex-packlist
%{_libdir}/ocaml/netplex/*.cm[ixao]*
%{_libdir}/ocaml/netplex/*.a
%{_libdir}/ocaml/netplex/*.o
%{_libdir}/ocaml/site-lib/netplex

%files netshm-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netshm
%{_libdir}/ocaml/netshm/*.cm[ixao]*
%{_libdir}/ocaml/netshm/*.a
%{_libdir}/ocaml/site-lib/netshm

%files netstring-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netstring
%{_libdir}/ocaml/netstring/netdb-packlist
%{_libdir}/ocaml/netstring/*.cm[ixao]*
%{_libdir}/ocaml/netstring/*.a
%{_libdir}/ocaml/netstring/*.o
%attr(755,root,root) %{_libdir}/ocaml/netstring/*.so
%{_libdir}/ocaml/site-lib/netstring

%files netsys
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/netsys
%attr(755,root,root) %{_libdir}/ocaml/netsys/*.so

%files netsys-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/netsys/*.cm[ixao]*
%{_libdir}/ocaml/netsys/*.a
%{_libdir}/ocaml/site-lib/netsys

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
%dir %{_libdir}/ocaml/rpc-generator
%attr(755,root,root) %{_libdir}/ocaml/rpc-auth-local/dllrpc_auth_local.so

%files rpc-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/rpc
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
%{_libdir}/ocaml/shell/*.o
%{_libdir}/ocaml/site-lib/shell

%files smtp-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/smtp
%{_libdir}/ocaml/smtp/*.cm[ixao]*
%{_libdir}/ocaml/smtp/*.a
%{_libdir}/ocaml/site-lib/smtp
