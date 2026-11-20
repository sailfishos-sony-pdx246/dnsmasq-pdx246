# SPDX-FileCopyrightText: Johannes Meyer zum Alten Borgloh
# SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only

Name:       dnsmasq
Version:    2.93
Release:    1
Summary:    Lightweight DNS forwarder and DHCP server
License:    GPL-2.0-only OR GPL-3.0-only
URL:        https://thekelleys.org.uk/dnsmasq/doc.html
Source0:    %{name}-%{version}.tar.bz2

%description
dnsmasq provides a DNS forwarder and a DHCP server for small networks.

This build ships the program only, without a system service or a
configuration: Waydroid starts it on its container network.

%package doc
Summary:    Manual page for %{name}
Requires:   %{name} = %{version}-%{release}

%description doc
The manual page of %{name}.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
# The version is given to make: bld/get-version asks git, which the build
# environment may not have, and the binary would then report UNKNOWN. install
# rebuilds whatever was built with other flags, so it gets the same ones.
make %{?_smp_mflags} CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" \
    version="-DVERSION='\\\"%{version}\\\"'"

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} BINDIR=%{_sbindir} \
    MANDIR=%{_mandir} CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" \
    version="-DVERSION='\\\"%{version}\\\"'"

%files
%license COPYING COPYING-v3
%{_sbindir}/%{name}

%files doc
%{_mandir}/man8/%{name}.8*
