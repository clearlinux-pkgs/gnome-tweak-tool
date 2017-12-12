#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-tweak-tool
Version  : 3.26.4
Release  : 13
URL      : https://download.gnome.org/sources/gnome-tweak-tool/3.26/gnome-tweak-tool-3.26.4.tar.xz
Source0  : https://download.gnome.org/sources/gnome-tweak-tool/3.26/gnome-tweak-tool-3.26.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gnome-tweak-tool-bin
Requires: gnome-tweak-tool-python3
Requires: gnome-tweak-tool-data
Requires: gnome-tweak-tool-locales
Requires: gnome-tweak-tool-python
BuildRequires : meson
BuildRequires : ninja
BuildRequires : python3

%description
GNOME TWEAKS
================
BUILD
-----
The only build-time dependency is [meson](http://mesonbuild.com/).

%package bin
Summary: bin components for the gnome-tweak-tool package.
Group: Binaries
Requires: gnome-tweak-tool-data

%description bin
bin components for the gnome-tweak-tool package.


%package data
Summary: data components for the gnome-tweak-tool package.
Group: Data

%description data
data components for the gnome-tweak-tool package.


%package locales
Summary: locales components for the gnome-tweak-tool package.
Group: Default

%description locales
locales components for the gnome-tweak-tool package.


%package python
Summary: python components for the gnome-tweak-tool package.
Group: Default
Requires: gnome-tweak-tool-python3

%description python
python components for the gnome-tweak-tool package.


%package python3
Summary: python3 components for the gnome-tweak-tool package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gnome-tweak-tool package.


%prep
%setup -q -n gnome-tweak-tool-3.26.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513084524
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain  builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-tweak-tool

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-tweak-tool
/usr/libexec/gnome-tweak-tool-lid-inhibitor

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-tweak-tool.desktop
/usr/share/gnome-tweak-tool/shell.css
/usr/share/gnome-tweak-tool/shell.ui
/usr/share/icons/hicolor/16x16/apps/gnome-tweak-tool.png
/usr/share/icons/hicolor/22x22/apps/gnome-tweak-tool.png
/usr/share/icons/hicolor/24x24/apps/gnome-tweak-tool.png
/usr/share/icons/hicolor/256x256/apps/gnome-tweak-tool.png
/usr/share/icons/hicolor/32x32/apps/gnome-tweak-tool.png
/usr/share/icons/hicolor/48x48/apps/gnome-tweak-tool.png
/usr/share/icons/hicolor/scalable/apps/gnome-tweak-tool-symbolic.svg
/usr/share/metainfo/gnome-tweak-tool.appdata.xml

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f gnome-tweak-tool.lang
%defattr(-,root,root,-)

