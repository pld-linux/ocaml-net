Summary:	Modules for Internet programming in OCaml
Summary(pl):	Modu³y u³atwiaj±ce pisanie programów internetowych w OCamlu
Name:		ocaml-net
Version:	0.98.1
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/ocamlnet/ocamlnet-%{version}.tar.gz
# Source0-md5:	991a004ab8137b50eb42d035570250a4
Patch0:		%{name}-DESTDIR.patch
URL:		http://ocamlnet.sourceforge.net/
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml >= 3.04-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modules for Internet programming in OCaml.

%description -l pl
Modu³y u³atwiaj±ce pisanie programów internetowych w OCamlu.

%package netstring-devel
Summary:	String processing library
Summary(pl):	Biblioteka do przetwarzania napisów
Group:		Development/Libraries
%requires_eq	ocaml-pcre-devel
%requires_eq	ocaml

%description netstring-devel
String processing library, part of Ocamlnet. This package contains
files needed to develop OCaml programs using this library.

%description netstring-devel -l pl
Biblioteka do przetwarzania napisów, czê¶æ pakietu Ocamlnet. Pakiet
ten zawiera pliki niezbêdne do tworzenia programów u¿ywaj±cych tej
biblioteki.

%package cgi-devel
Summary:	Common Gateway Interface library
Summary(pl):	Biblioteka do tworzenia skryptów CGI
Group:		Development/Libraries
Requires:	%{name}-netstring-devel = %{version}-%{release}
%requires_eq	ocaml

%description cgi-devel
Common Gateway Interface library, part of Ocamlnet. This package
contains files needed to develop OCaml programs using this library.

%description cgi-devel -l pl
Biblioteka do tworzenia skryptów CGI, czê¶æ pakietu Ocamlnet. Pakiet
ten zawiera pliki niezbêdne do tworzenia programów u¿ywaj±cych tej
biblioteki.

%package pop3-devel
Summary:	Post Office Protocol (POP3) library
Summary(pl):	Biblioteka do obs³ugi POP3
Group:		Development/Libraries
Requires:	%{name}-netstring-devel = %{version}-%{release}
%requires_eq	ocaml

%description pop3-devel
Post Office Protocol (POP3) library, part of Ocamlnet. This package
contains files needed to develop OCaml programs using this library.

%description pop3-devel -l pl
Biblioteka do obs³ugi POP3, czê¶æ pakietu Ocamlnet. Pakiet ten zawiera
pliki niezbêdne do tworzenia programów u¿ywaj±cych tej biblioteki.

%prep
%setup -q -n ocamlnet-%{version}
%patch0 -p1

%build
cd src
# no %%configure, please
./configure \
	-enable-findlib \
	-with-netstring \
	-with-cgi \
        -with-pop

sed -e 's/-g//' Makefile.rules > Makefile.rules.tmp
mv -f Makefile.rules.tmp Makefile.rules
%{__make} all opt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml

cd src
%{__make} install OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

for f in cgi pop netstring ; do
	install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/$f
	mv $RPM_BUILD_ROOT%{_libdir}/ocaml/$f/META \
		$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/$f/
	echo "directory = \"+$f\"" \
		>> $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/$f/META
done
cd ..
# not sure about *.o
rm $RPM_BUILD_ROOT%{_libdir}/ocaml/*/*.mli

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-{pop3,cgi}-%{version}
cp -r examples/{cgi,jserv} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-cgi-%{version}
cp -r examples/pop/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-pop3-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files netstring-devel
%defattr(644,root,root,755)
%doc LICENSE README doc/intro/html
%dir %{_libdir}/ocaml/netstring
%{_libdir}/ocaml/netstring/*.cm[ixao]*
%{_libdir}/ocaml/netstring/*.a
%{_libdir}/ocaml/site-lib/netstring

%files cgi-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/cgi
%{_libdir}/ocaml/cgi/*.cm[ixao]*
%{_libdir}/ocaml/cgi/*.a
%{_libdir}/ocaml/site-lib/cgi
%{_examplesdir}/%{name}-cgi-%{version}

%files pop3-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/pop
%{_libdir}/ocaml/pop/*.cm[ixao]*
%{_libdir}/ocaml/pop/*.a
%{_libdir}/ocaml/site-lib/pop
%{_examplesdir}/%{name}-pop3-%{version}
