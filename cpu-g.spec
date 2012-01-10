Summary:	Shows some useful information about your hardware
Name:		cpu-g
Version:	0.9.0
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	http://dl.sourceforge.net/cpug/%{name}-%{version}.tar.gz
# Source0-md5:	51b35a75331dc1067c6ed79b4861d346
Patch0:		%{name}-datadir.patch
URL:		http://sourceforge.net/projects/cpug/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.586
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CPU-G is an application that shows useful information about your
hardware. It collects and displays information about your CPU, RAM,
Motherboard, some general information about your system and more. 

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}} \
	$RPM_BUILD_ROOT%{_desktopdir}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install doc/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{name} $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{name}.glade $RPM_BUILD_ROOT%{_datadir}/%{name}
install data/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

cp -R data $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/%{name}
%{_datadir}/%{name}/%{name}.glade
%{_datadir}/%{name}/data
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/*.1*
