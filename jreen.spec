Summary:	Qt XMPP library
Name:		jreen
Version:	1.1.1
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		https://github.com/euroelessar/jreen
Source0:	http://mirror.yandex.ru/gentoo-distfiles/distfiles/jreen-%{version}.tar.gz

BuildRequires:	cmake >= 2.8.0
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(QtNetwork)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libidn)

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
Requires:	%{libjreen} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

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

