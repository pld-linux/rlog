#
# Conditional build:
%bcond_without	static_libs	# static library build
#
Summary:	Runtime Logging for C++
Summary(pl.UTF-8):	Logowanie w czasie działania programu dla C++
Name:		rlog
Version:	1.4
Release:	2
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: http://code.google.com/p/rlog/downloads/list
Source0:	http://rlog.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	c29f74e0f50d66b20312d049b683ff82
URL:		http://www.arg0.net/rlog
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RLog provides a flexible message logging facility for C++ programs and
libraries. It is meant to be fast enough to leave in production code.

%description -l pl.UTF-8
RLog dostarcza elastyczne ułatwienia do logowania komunikatów dla
programów i bibliotek w C++. Ma być wystarczająco szybki do
pozostawienia w kodzie produkcyjnym.

%package devel
Summary:	Header files for rlog
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki rlog
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
The header files are only needed for development of programs using the
rlog.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów przy użyciu rloga.

%package static
Summary:	Static rlog library
Summary(pl.UTF-8):	Statyczna biblioteka rlog
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static rlog library.

%description static -l pl.UTF-8
Statyczna biblioteka rlog.

%prep
%setup -q

%build
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/rlog

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/librlog.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librlog.so.5

%files devel
%defattr(644,root,root,755)
%doc docs/html/ docs/latex/refman.pdf
%attr(755,root,root) %{_libdir}/librlog.so
%{_libdir}/librlog.la
%{_includedir}/rlog
%{_pkgconfigdir}/librlog.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/librlog.a
%endif
