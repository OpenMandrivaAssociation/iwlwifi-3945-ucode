Summary: Intel PRO/Wireless 3945ABG/BG microcode
Name: iwlwifi-3945-ucode
Epoch: 1
Version: 15.32.2.9
Release: 2
Source0: http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-3945-ucode-%{version}.tgz
Source1: http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-3945-ucode-15.28.1.8.tgz
License: Proprietary
Group: System/Kernel and hardware
Url: http://intellinuxwireless.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
The file iwlwifi-3945-*.ucode provided in this package is required to be
present on your system in order for the Intel PRO/Wireless 3945ABG/BG Network
Connection Adapter driver for Linux (iwl3945) to be able to operate
on your system.

%prep
%setup -q -a 1

# provide old firmware with ucode_api=1 for compatibility with older kernels
cp iwlwifi-3945-ucode-15.28.1.8/iwlwifi-3945-1.ucode .
cp iwlwifi-3945-ucode-15.28.1.8/README.iwlwifi-3945-ucode \
   README.iwlwifi-3945-ucode-1
mv README.iwlwifi-3945-ucode README.iwlwifi-3945-ucode-2

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware
install -m644 *.ucode %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc LICENSE.* README.*
/lib/firmware/*.ucode
