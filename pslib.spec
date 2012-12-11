%define	major 0
%define libname %mklibname pslib %{major}
%define develname %mklibname pslib -d

Summary:	C-library for generating multi page PostScript documents
Name:		pslib
Version:	0.4.5
Release:	2
License:	LGPL
Group:		System/Libraries
URL:		http://pslib.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/pslib/pslib-%{version}.tar.gz
Source1:	pslib-0.4.1-manpages.tar.gz
Patch0:		pslib-0.4.1-linkage_fix.diff
BuildRequires:	autoconf automake libtool
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	glib2-devel
#BuildRequires:	docbook-utils
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	ungif-devel
BuildRequires:	libtiff-devel
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


%changelog
* Sun May 06 2012 Oden Eriksson <oeriksson@mandriva.com> 0.4.5-2
+ Revision: 797102
- fix deps
- various fixes

* Mon Sep 26 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.4.5-1
+ Revision: 701279
- new version
- do autoreconf in %%prep
- clean out old rpm junk
- drop ambigious lib%%{name}-devel provides...
- fix bogus version

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-6mdv2011.0
+ Revision: 614624
- the mass rebuild of 2010.1 packages

* Sat Aug 22 2009 Funda Wang <fwang@mandriva.org> 0.4.1-5mdv2010.0
+ Revision: 419597
- fix build with glibc 2.10

* Tue Nov 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-5mdv2009.1
+ Revision: 302226
- more dep fixes...
- more dep fixes
- fix deps
- fix linkage
- rebuilt against new libxcb

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.4.1-3mdv2008.1
+ Revision: 171053
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Sun Feb 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-2mdv2008.1
+ Revision: 169574
- fix build on x86_64

* Sun Feb 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-1mdv2008.1
+ Revision: 169559
- 0.4.1
- regenerated the manpages

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.7-3mdv2008.0
+ Revision: 83633
- fix build deps (perl-XML-Parser)
- Import pslib



* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.7-3
- new devel naming

* Mon Aug 28 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.7-2
- provide the manpages generated on cooker

* Thu Aug 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.7-1mdv2007.0
- initial Mandriva package
