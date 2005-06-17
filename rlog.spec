Summary:	Runtime Logging for C++
Summary(pl):	Logowanie w czasie dzia³ania programu dla C++
Name:		rlog
Version:	1.3.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://arg0.net/users/vgough/download/%{name}-%{version}.tgz
# Source0-md5:	e918c6854529249f39eae37722719133
URL:		http://pobox.com/~vgough/rlog/
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RLog provides a flexible message logging facility for C++ programs and
libraries. It is meant to be fast enough to leave in production code.

%description -l pl
RLog dostarcza elastyczne u³atwienia do logowania komunikatów dla
programów i bibliotek w C++. Ma byæ wystarczaj±co szybki do
pozostawienia w kodzie produkcyjnym.

%package devel
Summary:	Header files for rlog
Summary(pl):	Pliki nag³ówkowe biblioteki rlog
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
The header files are only needed for development of programs using the
rlog.

%description devel -l pl
Pliki nag³ówkowe do tworzenia programów przy u¿yciu rloga.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/html/ docs/latex/refman.pdf
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%dir %{_includedir}/rlog
%{_includedir}/rlog/*.h
%{_pkgconfigdir}/*.pc
