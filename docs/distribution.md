# Distribution notes

This document records the current distribution plan for the Python bindings,
tec5 user-mode runtime, and Windows device drivers. It is planning guidance,
not a statement that redistribution permission has been granted.

## Current decision

The tec5 runtime, drivers, installers, SDK PDFs, and vendor manuals are outside
the scope of this repository. Developers keep locally obtained copies under the
ignored `.local/` directory and point the Python loader at the runtime. The Git
history must not contain these vendor-distributed files.

## Components with separate distribution concerns

Treat these as independent deliverables:

1. The original Python code in this repository.
2. The tec5 user-mode runtime, including `SDACQ64MP.dll`, `SDPROCCL64.dll`, and
   possibly `PDETH64.dll`.
3. The tec5 Windows device-driver package or installer.
4. Vendor manuals, SDK PDFs, headers, examples, and other documentation.

Permission to distribute one category does not imply permission to distribute
the others.

## Permission checklist

Before separately redistributing any vendor binary or document, obtain and
retain written confirmation covering:

- The exact runtime filenames and versions that may be redistributed.
- Whether redistribution through a public GitHub repository or GitHub Release
  is permitted.
- Whether redistribution may be worldwide and without access controls.
- Whether the vendor installer, INF driver package, and supporting files may be
  redistributed unchanged.
- Whether SDK headers, manuals, and other documentation may be published.
- Required license text, copyright notices, attribution, or click-through
  terms.
- Whether downstream users may further redistribute the files.
- Whether older versions must be removed when a new vendor version is issued.

No vendor binaries or documents will be distributed with this project. Do not
infer redistribution permission merely from having received or installed the
SDK.

## Recommended public repository

The preferred public repository should contain only material that is clearly
licensed for publication:

```text
tec5/
  src/tec5/              Python bindings
  scripts/               Hardware diagnostics
  tests/                 Hardware-independent tests
  docs/                  Original project documentation
  LICENSE                License for the original project code
  THIRD_PARTY.md         Third-party inventory and notices
  README.md
  pyproject.toml
```

Do not rely on `.gitignore` as a licensing boundary. It prevents new untracked
files from being added accidentally but does not remove files already committed
to history.

## Cleaning the existing repository

Vendor DLLs and PDFs are already present or have been present in the working
repository. Before publication:

1. Inventory every third-party file currently tracked and every such file in
   prior commits.
2. Decide which files have confirmed publication rights.
3. Make a complete backup of the private repository.
4. Either create a new public repository from an approved source snapshot or
   rewrite history to remove unauthorized files.
5. Reclone the proposed public repository into a clean directory.
6. Search both the working tree and Git object history for excluded filenames
   and file hashes.
7. Review generated source archives before publishing the first release.

Starting a new clean public history is usually easier to audit than rewriting a
repository that has never been public. Preserve the private repository as the
internal development record if appropriate.

## Python package

Keep the base `tec5` wheel free of vendor binaries by default. This produces a
normal pure-Python artifact and lets users point the loader at a separately
installed runtime.

Suggested artifacts:

```text
tec5-<version>-py3-none-any.whl
tec5-<version>.tar.gz
```

The loader supports:

1. An explicit DLL file or directory passed to `tec5.load()`.
2. The `TEC5_SDACQ_DLL` environment variable.
3. Normal Windows DLL discovery.

If a future build contains vendor DLLs, it must be identified as Windows- and
architecture-specific rather than `py3-none-any`.

## Optional runtime distribution

If redistribution permission is confirmed, prefer a separate, versioned
runtime artifact rather than committing binaries to the main source tree:

```text
tec5-runtime-<vendor-version>-win64.zip
  runtime/
    SDACQ64MP.dll
    SDPROCCL64.dll
    PDETH64.dll
    VENDOR-LICENSE.txt
    manifest.json
```

The manifest should record:

- Vendor and SDK/runtime version.
- Supported Windows architecture.
- Original filename and purpose of every file.
- SHA-256 digest of every file.
- Source and acquisition date.
- Required licensing and copyright notices.
- Required versus optional companion DLLs.
- Known compatible Python package versions.

GitHub Releases can hold tagged binary assets separately from normal source
history. Release assets are nevertheless public redistribution and require the
same vendor permission. See:

- <https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases>
- <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases>

An alternative is a separate `tec5-runtime` Windows wheel. Such a wheel must be
tagged for the applicable Windows architecture and must include the vendor
license and notices. It must not be emitted as a platform-independent wheel.

## Windows device drivers

Do not install a kernel driver as an import side effect or ordinary Python
package installation step.

Preferred order:

1. Direct users to an official tec5 download or installer.
2. If permitted, redistribute the original signed vendor installer unchanged.
3. If the vendor supplies a redistributable signed INF package, distribute the
   complete package unchanged and provide a separate, explicit installer.

A complete INF-based driver package may include INF, SYS, CAT, DLL, and other
supporting files. Do not edit signed package contents, because modifications can
invalidate the catalog signature.

Windows includes PnPUtil for driver-store management. An explicit elevated
installation command for an approved INF package can use:

```powershell
pnputil /add-driver "driver\*.inf" /subdirs /install
```

See Microsoft's documentation:

- <https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/pnputil-command-syntax>

Any project-provided driver installer should:

- Require an explicit user action and visible elevation request.
- Verify expected hashes and digital signatures before installation.
- Display the vendor, version, and target device.
- Capture and retain PnPUtil output.
- Report whether a reboot is required.
- Avoid silently removing or replacing other installed driver versions.
- Keep uninstallation separate and require confirmation.

Do not redistribute DevCon itself; use the Windows-provided PnPUtil unless the
vendor's original installer is available and preferred.

## Licenses and notices

Before publication, add:

- A `LICENSE` file covering the original Python code.
- A `THIRD_PARTY.md` inventory identifying all vendor material.
- Any vendor license or notices required alongside redistributed artifacts.
- A clear statement that tec5 names and trademarks belong to their respective
  owner and that the project is unofficial unless tec5 authorizes otherwise.

Do not place third-party files under the project's open-source license unless
the rights holder explicitly permits that relicensing.

## Release integrity

For every source or binary release:

- Build from a reviewed tag.
- Publish SHA-256 checksums.
- Record the vendor runtime and driver versions used for testing.
- Confirm that source archives do not contain excluded binaries or manuals.
- Confirm that pure-Python wheels contain no DLL, SYS, INF, CAT, or vendor PDF
  files.
- Test installation and DLL loading in a clean 64-bit Windows environment.
- Preserve a copy of the permission and license documents used for the release
  decision.

## Proposed release layout

If all required permissions are obtained:

```text
GitHub release vX.Y.Z
  tec5-X.Y.Z-py3-none-any.whl
  tec5-X.Y.Z.tar.gz
  tec5-runtime-<vendor-version>-win64.zip
  tec5-driver-<vendor-version>-original.exe  # only if explicitly permitted
  SHA256SUMS
  release notes
```

If runtime or driver redistribution is not permitted, publish only the source
and Python package, then link users to the official vendor installation source.

## Open decisions

- Which license to use for the original Python code.
- Whether tec5 grants public redistribution rights for each vendor component.
- Whether a source-only public repository should retain vendor-derived API
  documentation and constants.
- Whether to begin with a new clean public Git history.
- Whether runtime delivery should use a ZIP bundle, a separate Windows wheel,
  or only the official vendor installer.
