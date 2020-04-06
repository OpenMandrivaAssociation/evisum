%define	efl_version 1.23.3
Summary:	Enlightenment System Monitor
Name:		evisum
Version:	0.3.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Enlightenment
URL:		https://www.enlightenment.org/
Source:		https://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.xz
# Non-devel packages are needed to compile themes
BuildRequires:	e
BuildRequires:  meson
BuildRequires:	pkgconfig(ecore) => %{efl_version}
BuildRequires:	pkgconfig(ecore-evas) => %{efl_version}
BuildRequires:	pkgconfig(ecore-file) => %{efl_version}
BuildRequires:	pkgconfig(ecore-imf) => %{efl_version}
BuildRequires:	pkgconfig(ecore-imf-evas) => %{efl_version}
BuildRequires:	pkgconfig(ecore-input) => %{efl_version}
BuildRequires:	pkgconfig(ecore-ipc) => %{efl_version}
BuildRequires:	pkgconfig(edje) => %{efl_version}
BuildRequires:	pkgconfig(eet) => %{efl_version}
BuildRequires:	pkgconfig(efreet) => %{efl_version}
BuildRequires:	pkgconfig(eina) => %{efl_version}
BuildRequires:	pkgconfig(eldbus) => %{efl_version}
BuildRequires:	pkgconfig(elementary) => 0.21.7
BuildRequires:	pkgconfig(emotion) => %{efl_version}
BuildRequires:	pkgconfig(ethumb_client) => %{efl_version}
BuildRequires:	pkgconfig(evas) => %{efl_version}
BuildRequires:	pkgconfig(efl) => %{efl_version}

Requires:	efl => %{efl_version}
Requires:	edje => %{efl_version}
Requires:	elementary => 0.21.7
Requires:	emotion => %{efl_version}
Requires:	ethumb => %{efl_version}

%description
Enlightenment System Monitor

%files
%doc AUTHORS COPYING
%{_bindir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q

%meson

%build
%meson_build

%install
%meson_install

%find_lang %{name}
