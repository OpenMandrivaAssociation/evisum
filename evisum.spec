%define	efl_version 1.29.0
Summary:	Enlightenment System Monitor
Name:		evisum
Version:	1.0.0
Release:	1
License:	GPLv22
Group:		Graphical desktop/Enlightenment
URL:		https://www.enlightenment.org/
Source:		https://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	e
BuildRequires:  meson
BuildRequires:	pkgconfig(efl) => %{efl_version}

Requires:	efl => %{efl_version}
Requires: e => 0.28.0

%description
Enlightenment System Monitor

%files
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/evisum.desktop
%{_datadir}/evisum/images/*.png
%{_iconsdir}/hicolor/*x*/apps/evisum.png
%{_datadir}/evisum/themes/evisum.edj
%{_iconsdir}/hicolor/*x*/apps/evisum_cpu.png
%{_iconsdir}/hicolor/*x*/apps/evisum_mem.png

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%meson

%build
%meson_build

%install
%meson_install
