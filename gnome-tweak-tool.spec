#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-tweak-tool
Version  : 3.24.0
Release  : 1
URL      : https://download.gnome.org/sources/gnome-tweak-tool/3.24/gnome-tweak-tool-3.24.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-tweak-tool/3.24/gnome-tweak-tool-3.24.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gnome-tweak-tool-bin
Requires: gnome-tweak-tool-python
Requires: gnome-tweak-tool-data
Requires: gnome-tweak-tool-locales
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(pygobject-3.0)

%description
GNOME TWEAK TOOL
----------------
* The first rule of gnome-tweak-tool is do not talk about gnome-tweak-tool

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

%description python
python components for the gnome-tweak-tool package.


%prep
%setup -q -n gnome-tweak-tool-3.24.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492047221
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1492047221
rm -rf %{buildroot}
%make_install
%find_lang gnome-tweak-tool

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-tweak-tool
/usr/libexec/gnome-tweak-tool-lid-inhibitor

%files data
%defattr(-,root,root,-)
/usr/share/appdata/gnome-tweak-tool.appdata.xml
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

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files locales -f gnome-tweak-tool.lang
%defattr(-,root,root,-)
