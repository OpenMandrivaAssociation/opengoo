%define		oname	OpenGOO

Name:		opengoo
Version:	0.0.1
Release:	%mkrel 1
Summary:	Free and open clone of World of GOO
Group:		Games/Puzzles
License:	GPLv3+
URL:		http://mandarancio.github.com/OpenGOO/
# fetched from git
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel
BuildRequires:	box2d-devel

%description
Free and open clone of World of GOO.
Done with qt4 (and opengl module) and box2d

%prep
%setup -q

%build
%qmake_qt4
%make

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_libdir}/%{name}
%__cp %{oname} %{buildroot}%{_libdir}/%{name}/%{name}
%__cp *.level %{buildroot}%{_libdir}/%{name}/
%__cp menu.index %{buildroot}%{_libdir}/%{name}/

# wrapper script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash

cd %{_libdir}/%{name}
./%{name}
EOF
%__chmod 755 %{buildroot}%{_bindir}/%{name}

# menu-entry
%__mkdir_p  %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=OpenGOO
Comment=World of GOO clone
Exec=%{name}
Icon=amusement_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;LogicGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc LICENSE README
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop




%changelog
* Sun Mar 11 2012 Andrey Bondrov <abondrov@mandriva.org> 0.0.1-1mdv2011.0
+ Revision: 784117
- imported package opengoo

