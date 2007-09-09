%define	major 0
%define libname %mklibname pslib %{major}
%define develname %mklibname pslib -d

Summary:	PSlib is a C-library for generating multi page PostScript documents
Name:		pslib
Version:	0.2.7
Release:	%mkrel 3
License:	LGPL
Group:		System/Libraries
URL:		http://pslib.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/pslib/pslib-%{version}.tar.bz2
Source1:	pslib-%{version}-manpages.tar.bz2
BuildRequires:	autoconf2.5
BuildRequires:	libtool
#BuildRequires:	docbook-utils
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libungif-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
PSlib is a C-library for generating multi page PostScript documents. There are
functions for drawing lines, arcs, rectangles, curves, etc. PSlib also provides
very sophisticated functions for text output including hyphenation and kerning.

%package -n	%{libname}
Summary:	PSlib is a C-library for generating multi page PostScript documents
Group:          System/Libraries

%description -n	%{libname}
PSlib is a C-library for generating multi page PostScript documents. There are
functions for drawing lines, arcs, rectangles, curves, etc. PSlib also provides
very sophisticated functions for text output including hyphenation and kerning.

%package -n	%{develname}
Summary:	Static library and header files for the PSlib library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-{release}
Provides:	lib%{name}-devel = %{version}-{release}
Obsoletes:	%{mklibname pslib 0 -d}

%description -n	%{develname}
PSlib is a C-library for generating multi page PostScript documents. There are
functions for drawing lines, arcs, rectangles, curves, etc. PSlib also provides
very sophisticated functions for text output including hyphenation and kerning.

This package contains the statis library and header files for the PSlib
library.

%prep

%setup -q -n %{name}-%{version} -a1

chmod 644 AUTHORS COPYING ChangeLog README

%build

%configure2_5x

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

install -d %{buildroot}%{_mandir}/man3
install -m0644 doc/man/*.3 %{buildroot}%{_mandir}/man3/

%find_lang %{name}


%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/libps
%{_includedir}/libps/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*
