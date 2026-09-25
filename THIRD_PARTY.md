# Third-party software and materials

This repository contains independently maintained Python bindings for the tec5
SDACQ API. It is not an official tec5 product and is not endorsed by or
affiliated with tec5 AG.

## tec5 runtime and drivers

The repository and Python package do not include tec5 runtime libraries,
Windows device drivers, installers, SDK manuals, or other vendor-distributed
files. In particular, users must obtain files such as the following from tec5
or another authorized source:

- `SDACQ64MP.dll`
- `SDPROCCL64.dll`
- `PDETH64.dll`, when required for Ethernet hardware
- The applicable signed Windows device driver or vendor installer

Those files remain subject to their vendor's copyright, license, support, and
redistribution terms. The MIT license in this repository does not apply to
them.

See the project README for instructions on pointing the Python loader at a
separately installed runtime.

## API names and interoperability declarations

The repository refers to tec5 API function names, constants, structures,
hardware names, and product names to provide interoperability with software
and hardware installed by the user. All associated third-party copyrights and
trademarks remain the property of their respective owners.

## Documentation

Vendor PDF manuals and SDK documentation are intentionally excluded from the
repository. Developers must obtain any needed documentation through an
authorized vendor channel and keep it outside the public source tree.
