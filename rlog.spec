# TODO:
# - make devel subpackage
Summary:	Runtime Logging for C++
Name:		rlog
Version:	1.3.6
Release:	0.1
License:	LGPL
Group:		Development/Libraries/C and C++
######		Unknown group!
Source0:	http://arg0.net/users/vgough/download/%{name}-%{version}.tgz
# Source0-md5:	e918c6854529249f39eae37722719133
URL:		http://pobox.com/~vgough/rlog
BuildRequires:	pkgconfig
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RLog provides a flexible message logging facility for C++ programs and
libraries. It is meant to be fast enough to leave in production code.

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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README docs/html/ docs/latex/refman.pdf
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/*.la
%{_pkgconfigdir}/*.pc
%dir %{_includedir}/rlog
%{_includedir}/rlog/*.h
