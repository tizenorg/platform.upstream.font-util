#
# spec file for package font-util
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


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
%doc ChangeLog COPYING README
%{_bindir}/bdftruncate
%{_bindir}/ucs2any
%{_mandir}/man1/bdftruncate.1%{?ext_man}
%{_mandir}/man1/ucs2any.1%{?ext_man}
%{_datadir}/aclocal/fontutil.m4
%{_datadir}/fonts/util/
%{_libdir}/pkgconfig/fontutil.pc

%changelog
