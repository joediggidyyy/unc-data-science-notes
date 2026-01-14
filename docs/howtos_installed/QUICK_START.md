# CodeSentinel - Quick Start

## Installation (5 seconds)

**Windows**: Run `INSTALL_CODESENTINEL_GUI.bat`  
**macOS/Linux**: Run `bash INSTALL_CODESENTINEL_GUI.sh`  
**Any OS**: `pip install codesentinel`

## Get Started

```bash
codesentinel status        # Check your system
codesentinel --help        # See all commands
```

## Full Documentation

- **[Getting Started Guide](docs/guides/GETTING_STARTED_DETAILED.md)** - Complete walkthrough with examples
- **[Installation Guide](docs/installation/)** - Detailed installation for all platforms
- **[Architecture & Policies](docs/architecture/)** - How CodeSentinel works
- **[All Documentation](docs/)** - Complete documentation hub

## Packaging for SEAM-Central

If you need to prepare a release artifact for SEAM-Central (offline ingestion), use the helper:

```powershell
python tools/codesentinel/prepare_seam_package.py
```

This will build sdist/wheel into `dist/`, compute SHA256 checksums, and create companion `.sig` files (contains the checksum hex). The produced `dist/CHECKSUMS.txt` and `dist/manifest.json` are intended for automated ingestion and verification.
