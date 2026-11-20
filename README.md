<!--
SPDX-FileCopyrightText: Johannes Meyer zum Alten Borgloh
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# dnsmasq for the Xperia 10 VI

[dnsmasq](https://thekelleys.org.uk/dnsmasq/doc.html) packaged for the
[Sailfish OS port for the Sony Xperia 10 VI](https://github.com/sailfishos-sony-pdx246/main)
(pdx246). Waydroid runs it on its container network, as the DHCP server and DNS forwarder of
the Android container. The package has no system service and no configuration of its own.

`upstream/` is dnsmasq's git repository at a release tag; `rpm/dnsmasq.spec` builds it with
dnsmasq's default compile options. The port's `scripts/build-packages-sdk.sh` (step `dnsmasq`)
builds it in the Sailfish OS Platform SDK from `hybris/mw/dnsmasq-pdx246`. The directory is
not called `dnsmasq` because the HADK's `build_packages.sh` looks in the Android tree's
`external/` first, which has AOSP's own dnsmasq.

## Licence

The packaging is under GPL-2.0-only OR GPL-3.0-only, like dnsmasq itself; this README is under
CC-BY-SA-4.0.
