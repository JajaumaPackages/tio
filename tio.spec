Summary:        Simple TTY terminal I/O application
Name:           tio
Version:        1.25
Release:        1%{?dist}
License:        GPLv2+
URL:            https://tio.github.io/
Source0:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  gcc

%description
Tio is a simple TTY terminal application which features a straightforward
commandline interface to easily connect to TTY devices for basic input/output.

%prep
%setup -q

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Oct 16 2017 Robert Scheck <robert@fedoraproject.org> 1.25-1
- Upgrade to 1.25

* Sun Oct 01 2017 Robert Scheck <robert@fedoraproject.org> 1.24-2
- Changes to match with Fedora Packaging Guidelines (#1497549)

* Sun Oct 01 2017 Robert Scheck <robert@fedoraproject.org> 1.24-1
- Upgrade to 1.24
- Initial spec file for Fedora and Red Hat Enterprise Linux
