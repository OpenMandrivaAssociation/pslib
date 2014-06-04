%define	major 0
%define libname %mklibname pslib %{major}
%define develname %mklibname pslib -d

Summary:	C-library for generating multi page PostScript documents
Name:		pslib
Version:	0.4.5
Release:	4
License:	LGPL
Group:		System/Libraries
URL:		http://pslib.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/pslib/pslib-%{version}.tar.gz
Source1:	pslib-0.4.1-manpages.tar.gz
Patch0:		pslib-0.4.1-linkage_fix.diff
Patch1:		pslib-0.4.5-giflib5.patch
BuildRequires:	autoconf automake libtool
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	glib2-devel
#BuildRequires:	docbook-utils
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	ungif-devel
BuildRequires:	tiff-devel
BuildRequires:	perl-XML-Parser

%description
PSlib is a C-library for generating multi page PostScript documents. There are
functions for drawing lines, arcs, rectangles, curves, etc. PSlib also provides
very sophisticated functions for text output including hyphenation and kerning.

%package -n	%{libname}
Summary:	C-library for generating multi page PostScript documents
Group:          System/Libraries

%description -n	%{libname}
PSlib is a C-library for generating multi page PostScript documents. There are
functions for drawing lines, arcs, rectangles, curves, etc. PSlib also provides
very sophisticated functions for text output including hyphenation and kerning.

%package -n	%{develname}
Summary:	Static library and header files for the PSlib library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname pslib 0 -d}

%description -n	%{develname}
PSlib is a C-library for generating multi page PostScript documents. There are
functions for drawing lines, arcs, rectangles, curves, etc. PSlib also provides
very sophisticated functions for text output including hyphenation and kerning.

This package contains the statis library and header files for the PSlib
library.

%prep
%setup -q -a1
%patch0 -p0
%patch1 -p1

chmod 644 AUTHORS COPYING ChangeLog README

autoreconf -fis

%build
%configure2_5x

# borkiness
find -type f -name "Makefile" | xargs perl -pi -e "s|/usr/lib\b|%{_libdir}|g"

%make

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
%makeinstall_std

install -d %{buildroot}%{_mandir}/man3
install -m0644 doc/man/*.3 %{buildroot}%{_mandir}/man3/

%find_lang %{name}

rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname} -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.%{major}*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%files -n %{develname}
%dir %{_includedir}/libps
%{_includedir}/libps/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*
