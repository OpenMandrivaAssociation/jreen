Summary:	Qt XMPP library
Name:		jreen
Version:	1.2.1
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		https://github.com/euroelessar/jreen
Source0:	http://mirror.yandex.ru/gentoo-distfiles/distfiles/jreen-%{version}.tar.gz

BuildRequires:	cmake >= 2.8.0
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(QtNetwork)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libgsasl)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	speex-devel

%description
Qt XMPP library.

#---------------------------------------------------------------------
%define jreen_major 1
%define libjreen %mklibname jreen-qt5 %{jreen_major}

%package -n %{libjreen}
Summary:	Qt XMPP library
Group:		System/Libraries

%description -n %{libjreen}
Qt XMPP library.

%files -n %{libjreen}
%{_libdir}/libjreen-qt5.so.%{jreen_major}*

#--------------------------------------------------------------------

%define develjreen %mklibname -d %{name}

%package -n %{develjreen}
Summary:	Devel files for %{name}
Group:		Development/C
Requires:	%{libjreen} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develjreen}
Devel files for %{name}

%files -n %{develjreen}
%{_includedir}/%{name}-qt5/
%{_libdir}/libjreen-qt5.so
%{_libdir}/pkgconfig/libjreen-qt5.pc

#---------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

