%define		kdeappsver	21.08.0
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kalarmcal
Summary:	Kalarmcal
Name:		ka5-%{kaname}
Version:	21.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d478fc3fcd9893b5ee05d6157547f377
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcalendarcore-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kholidays-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Client library to access and handling of KAlarm calendar data.

%description -l pl.UTF-8
Biblioteka kliencka do dostępu i obługi danych kalendarzowych KAlarm.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF5AlarmCalendar.so.5
%attr(755,root,root) %{_libdir}/libKF5AlarmCalendar.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi_serializer_kalarm.so
%{_datadir}/akonadi/plugins/serializer/akonadi_serializer_kalarm.desktop
%{_datadir}/qlogging-categories5/kalarmcal.categories
%{_datadir}/qlogging-categories5/kalarmcal.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KAlarmCal
%{_includedir}/KF5/kalarmcal_version.h
%{_libdir}/cmake/KF5AlarmCalendar
%{_libdir}/libKF5AlarmCalendar.so
%{_libdir}/qt5/mkspecs/modules/qt_KAlarmCal.pri
