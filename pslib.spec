%define	major 0
%define libname %mklibname pslib %{major}
%define devname %mklibname pslib -d

Summary:	C-library for generating multi page PostScript documents
Name:		pslib
Version:	0.4.6
Release:	1
License:	LGPL
Group:		System/Libraries
URL:		http://pslib.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/pslib/pslib-%{version}.tar.gz
#Source1:	pslib-0.4.1-manpages.tar.gz
Patch0:		pslib-0.4.1-linkage_fix.diff
#Patch1:		pslib-0.4.5-giflib5.patch
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
%autosetup -p0 #-a1
#patch0 -p0

#chmod 644 AUTHORS COPYING ChangeLog README


%build
autoreconf -fiv
%configure # --disable-static

# borkiness
find -type f -name "Makefile" | xargs perl -pi -e "s|/usr/lib\b|%{_libdir}|g"

%make_build

# the docbook stuff is a bit borked...
#pushd doc
#mkdir -p man
#for i in *.sgml; do
#    REAL_NAME=`echo $i | sed -e 's/\.sgml//'`
#    BORKED_NAME=`echo $REAL_NAME | sed -e 's/^PS_//' | tr a-z A-Z`
#    perl -pi -e "s|\&trade| \(tm\)|g" $i
#    docbook2man $i >/dev/null 2>&1
#    if [ -f PS_${BORKED_NAME}.3 ]; then
#	mv PS_${BORKED_NAME}.3 man/$REAL_NAME.3
#    fi
#done

%install
%make_install

# manpage
#install -d %{buildroot}%{_mandir}/man3
#install -m0644 doc/man/*.3 %{buildroot}%{_mandir}/man3/

# remove static
#find %{buildroot} -name '*.la' -delete

# locales
%find_lang %{name}
