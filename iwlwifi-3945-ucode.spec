%define name iwlwifi-3945-ucode
%define version 2.14.1.5
%define release %mkrel 1

Summary: Intel PRO/Wireless 3945ABG/BG microcode
Name: %{name}
Epoch: 1
Version: %{version}
Release: %{release}
Source: http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-3945-ucode-%{version}.tgz
License: Proprietary
Group: System/Kernel and hardware
Url: http://intellinuxwireless.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
The file iwlwifi-3945-1.ucode provided in this package is required to be
present on your system in order for the Intel PRO/Wireless 3945ABG/BG Network
Connection Adapter driver for Linux (iwl3945) to be able to operate
on your system.

%prep
%setup -q
chmod -x *

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware
install -m644 *.ucode %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE.* README.*
/lib/firmware/*.ucode
