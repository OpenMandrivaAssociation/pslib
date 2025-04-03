%define	major 0
%define libname %mklibname pslib
%define devname %mklibname pslib -d
%define oldlibname %mklibname pslib 0

Summary:	C-library for generating multi page PostScript documents
Name:		pslib
Version:	0.4.8
Release:	1
License:	LGPL
Group:		System/Libraries
URL:		https://pslib.sourceforge.net/
Source0:	https://downloads.sourceforge.net/pslib/pslib-%{version}.tar.gz
BuildRequires:  docbook-to-man
BuildRequires:  docbook-utils
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:  perl(XML::Parser)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:	ungif-devel

%description
PSlib is a C-library for generating multi page PostScript documents. There are
functions for drawing lines, arcs, rectangles, curves, etc. PSlib also provides
very sophisticated functions for text output including hyphenation and kerning.

#---------------------------------------------------------------------------

%package -n	%{libname}
Summary:	C-library for generating multi page PostScript documents
Group:          System/Libraries
%rename %{oldlibname}

%description -n	%{libname}
PSlib is a C-library for generating multi page PostScript documents. There are
functions for drawing lines, arcs, rectangles, curves, etc. PSlib also provides
very sophisticated functions for text output including hyphenation and kerning.

%files -n %{libname} -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.%{major}*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

#---------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Static library and header files for the PSlib library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{name}-devel < %{EVRD}

%description -n	%{devname}
PSlib is a C-library for generating multi page PostScript documents. There are
functions for drawing lines, arcs, rectangles, curves, etc. PSlib also provides
very sophisticated functions for text output including hyphenation and kerning.

This package contains the statis library and header files for the PSlib
library.

%files -n %{devname}
%dir %{_includedir}/libps
%{_includedir}/libps/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*

#---------------------------------------------------------------------------

%prep
%autosetup -p0

%build
autoreconf -fiv
%configure #--disable-static

# brokiness
find -type f -name "Makefile" | xargs perl -pi -e "s|/usr/lib\b|%{_libdir}|g"

%make_build

%install
%make_install

# locales
%find_lang %{name}

