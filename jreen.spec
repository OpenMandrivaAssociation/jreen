Summary:	Qt XMPP library
Name:		jreen
Version:	1.1.1
Release:	1
Source0:	http://mirror.yandex.ru/gentoo-distfiles/distfiles/jreen-%{version}.tar.gz
License:	GPLv2
Group:		System/Libraries
URL:		https://github.com/euroelessar/jreen
BuildRequires:	pkgconfig(QtNetwork)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	qt4-devel
BuildRequires:	cmake >= 2.8.0

%description
Qt XMPP library.

#---------------------------------------------------------------------
%define jreen_major 1
%define libjreen %mklibname jreen %{jreen_major}

%package -n %{libjreen}
Summary:	Qt XMPP library
Group:		System/Libraries

%description -n %{libjreen}
Qt XMPP library.

%files -n %{libjreen}
%{_libdir}/libjreen.so.%{jreen_major}*

#--------------------------------------------------------------------

%define develjreen %mklibname -d %{name}

%package -n %{develjreen}
Summary:	Devel files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libjreen} = %{version}-%{release}

%description -n %{develjreen}
Devel files for %{name}

%files -n %{develjreen}
%{_includedir}/%{name}/
%{_libdir}/libjreen.so
%{_libdir}/pkgconfig/libjreen.pc

#---------------------------------------------------------------------

%prep
%setup -q

%build
export PATH=$PATH:/usr/lib/qt4/bin/
%cmake
%make

%install
%makeinstall_std -C build


%changelog
* Fri Apr 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.0-1
+ Revision: 792513
- BR:qt4-devel
- PATH not in path
- version update 1.1.0

* Mon Apr 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.5-1
+ Revision: 789951
- version update 1.0.5

* Sun Mar 18 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.3-1
+ Revision: 785477
- version update 1.0.3

* Tue Mar 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.2-1
+ Revision: 784647
- version update 1.0.2

* Fri Nov 25 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.0.1-1
+ Revision: 733351
- imported package jreen

