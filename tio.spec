Summary:        Simple TTY terminal I/O application
Name:           tio
Version:        1.24
Release:        2%{?dist}
License:        GPLv2+
URL:            https://tio.github.io/
Source0:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1.gpg
BuildRequires:  gnupg2

%description
Tio is a simple TTY terminal application which features a straightforward
commandline interface to easily connect to TTY devices for basic input/output.

%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
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
* Sun Oct 01 2017 Robert Scheck <robert@fedoraproject.org> 1.24-2
- Changes to match with Fedora Packaging Guidelines (#1497549)

* Sun Oct 01 2017 Robert Scheck <robert@fedoraproject.org> 1.24-1
- Upgrade to 1.24
- Initial spec file for Fedora and Red Hat Enterprise Linux
