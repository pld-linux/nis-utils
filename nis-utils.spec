Summary:	Linux NIS+ utilities
Summary(pl.UTF-8):	Linuksowe narzędzia do NIS+
Name:		nis-utils
Version:	1.4.1
Release:	0.1
License:	GPL v2+
Group:		Networking/Utilities
Source0:	ftp://ftp.kernel.org/pub/linux/utils/net/NIS+/%{name}-%{version}.tar.bz2
# Source0-md5:	b4b38d8b006d5ed6cb3e72ce0f354dba
Patch0:		%{name}-glibc.patch
URL:		http://www.linux-nis.org/nisplus/nis-utils/
# because of __nisbind_create() change, handled by glibc patch
BuildRequires:	glibc-devel >= 6:2.6
BuildRequires:	gmp-bsd-devel
# __nisbind_create() was internal ABI change, not guarded by versioned exports
Requires:	glibc >= 6:2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_prefix}/lib/nis

%description
The NIS+ Utilities are a collection of NIS+ administration and testing
tools. They contain: nisaddcred, nisaddent, niscat, nischgrp,
nischmod, nischown, nischttl, nisdefaults, niserror, nisgrep,
nisgrpadm, nisinit, nislog, nisls nismatch, nismkdir, nispath,
nisping, nisrm, nisrmdir, nisshowcache, nisstat, nistbladm, nistest
and nisupdkeys.

With this, Linux could act as full NIS+ client. The shadow support
from nispasswd is missing, but the other parts works. There was a
first try to write a NIS+ Server, but the sources remained in
pre-alpha stage and don't work. It looks like there will be never a
NIS+ server for Linux.

%description -l pl.UTF-8
NIS+ Utilities to zestaw narzędzi administracyjnych i testowych NIS+
dla Linuksa. Składa się z programów: nisaddcred, nisaddent, niscat,
nischgrp, nischmod, nischown, nischttl, nisdefaults, niserror,
nisgrep, nisgrpadm, nisinit, nislog, nisls nismatch, nismkdir,
nispath, nisping, nisrm, nisrmdir, nisshowcache, nisstat, nistbladm,
nistest oraz nisupdkeys.

Z ich pomocą Linux może działać jako pełny klient NIS+. Brakuje
jeszcze obsługi shadow w nispasswd, ale wszystkie inne części
działają. Była pierwsza próba napisania serwera NIS+, ale źródła
pozostały w stadium pre-alpha i nie działają. Prawdopodobnie nigdy
nie będzie serwera NIS+ na Linuksa.

%package devel
Summary:	nisdb library
Summary(pl.UTF-8):	Biblioteka nisdb
Group:		Development/libraries
Requires:	glibc-devel >= 2.1.3
# doesn't require base (it's static-only)

%description devel
nisdb static library, headers and documentation.

%description devel -l pl.UTF-8
Biblioteka statyczna nisdb wraz z plikami nagłówkowymi i dokumentacją.

%prep
%setup -q
%patch0 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	usretcexecdir=%{_sbindir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/chkey
%attr(755,root,root) %{_bindir}/keylogin
%attr(755,root,root) %{_bindir}/keylogout
%attr(755,root,root) %{_bindir}/newkey
%attr(755,root,root) %{_bindir}/nis*
%attr(4754,root,root) %{_sbindir}/keyenvoy
%attr(755,root,root) %{_sbindir}/keyserv
%attr(755,root,root) %{_sbindir}/nis_cachemgr
%attr(755,root,root) %{_sbindir}/nisinit
%attr(755,root,root) %{_sbindir}/rpc.nisd
%attr(755,root,root) %{_sbindir}/rpc.nispasswdd
%dir %{_prefix}/lib/nis
%attr(755,root,root) %{_prefix}/lib/nis/nis*
%{_mandir}/man1/chkey.1*
%{_mandir}/man1/keylogin.1*
%{_mandir}/man1/keylogout.1*
%{_mandir}/man1/newkey.1*
%{_mandir}/man1/nis*.1*
%{_mandir}/man5/publickey.5*
%{_mandir}/man8/keyenvoy.8*
%{_mandir}/man8/keyserv.8*
%{_mandir}/man8/nis*.8*
%{_mandir}/man8/rpc.nisd.8*
%{_mandir}/man8/rpc.nispasswdd.8*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libnisdb.a
%{_libdir}/libnisdb.la
%{_includedir}/rpcsvc/nis_cache.h
%{_includedir}/rpcsvc/nis_cache.x
%{_includedir}/rpcsvc/nis_db.h
%{_includedir}/rpcsvc/nispasswd.h
%{_includedir}/rpcsvc/nispasswd.x
%{_mandir}/man3/db_*.3*
%{_mandir}/man3/getpublickey.3*
%{_mandir}/man3/getsecretkey.3*
%{_mandir}/man3/nis_db.3*
%{_mandir}/man3/publickey.3*
