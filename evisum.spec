%define	efl_version 1.26.1
Summary:	Enlightenment System Monitor
Name:		evisum
Version:	0.6.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Enlightenment
URL:		https://www.enlightenment.org/
Source:		https://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	e
BuildRequires:  meson
BuildRequires:	pkgconfig(efl) => %{efl_version}

Requires:	efl => %{efl_version}
Requires: e => 0.25.1

%description
Enlightenment System Monitor

%files
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/evisum.desktop
#{_datadir}/applications/evisum_cpu.desktop
#{_datadir}/applications/evisum_mem.desktop
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
