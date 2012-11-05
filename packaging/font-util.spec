Name:           font-util
Version:        1.3.0
Release:        0
License:        MIT
Summary:        X
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Fonts
Source:         %{name}-%{version}.tar.bz2
Source1:        http://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP932.TXT
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
This package provides utilities for X.Org font package
creation/installation.

%prep
%setup -q
# see Bug 194720 for details
cp %{SOURCE1} map-JISX0201.1976-0

%build
%configure --with-mapdir=%{_datadir}/fonts/util

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/bdftruncate
%{_bindir}/ucs2any
%{_mandir}/man1/bdftruncate.1%{?ext_man}
%{_mandir}/man1/ucs2any.1%{?ext_man}
%{_datadir}/aclocal/fontutil.m4
%{_datadir}/fonts/util/
%{_libdir}/pkgconfig/fontutil.pc

%changelog
