Summary:	Qt XMPP library
Name:		jreen
Version:	1.1.0
Release:	1
Source0:	jreen-%{version}.tar.bz2
License:	GPLv2
Group:		System/Libraries
URL:		https://github.com/euroelessar/jreen
BuildRequires:	pkgconfig(QtNetwork) 
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	cmake >= 2.8.0

%description
Qt XMPP library.

#---------------------------------------------------------------------
%define jreen_major 1
%define libjreen %mklibname jreen %jreen_major

%package -n %libjreen
Summary:	Qt XMPP library
Group:		System/Libraries

%description -n %libjreen
Qt XMPP library.

%files -n %libjreen

%{_libdir}/libjreen.so.%{jreen_major}*

#--------------------------------------------------------------------

%define develjreen %mklibname -d jreen

%package -n %develjreen
Summary: Devel files for %name
Group: Development/C
Provides:	%name-devel = %version-%release
Provides:	lib%{name}-devel = %version-%release
Requires:	%libjreen = %version-%release


%description -n %develjreen
Devel files for %name

%files -n %develjreen
%{_includedir}/%name/
%{_libdir}/libjreen.so
%{_libdir}/pkgconfig/libjreen.pc

#---------------------------------------------------------------------

%prep
%setup -q -n libjreen-%{version}

%build
%cmake
%make

%install
%makeinstall_std -C build
