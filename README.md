# 🕶️ DARKHEX
## DESCRIPTION
Darkhex is a low-level file inspection tool that identifies the **true file type** of a file by analyzing its **binary header signatures** (magic bytes).
This means that darkhex would be able to identify the true filetype even if someone tries to be sneaky by tampering with the file extensions.
## ⚙️ HOW DOES DARKHEX WORK?
Darkhex reads the first 512 bytes of a file, converts them to hexadecimal, and compares them against known binary signatures to identify the true filetype.
Darkhex does **not** rely or depend on:
- File extensions  
- Filenames  
- User-provided metadata

Instead, darkhex inspects files at the byte level and identifies its true filetype.
## 🚀 APPLICATIONS
Darkhex is designed to reveal the true type of files, even when extensions lie. It addresses several real-world problems in security, forensics, and automation:
### 🔐 Malware Detection & Security
Malware often disguises itself as harmless files to bypass security filters. Darkhex can inspect the file headers and reveal its true type, helping security teams detect disguised executables, scripts, or malicious payloads before they are opened or executed.
### 🧪 Forensic Analysis
During investigations, analysts often encounter files with missing or incorrect extensions in disk images, memory dumps, or network captures. Darkhex allows investigators to classify and identify these unknown files quickly, providing crucial insights for digital forensics and incident response.
### 🗃️ File Integrity & Compliance
Files shared across systems or uploaded by users may not always match their declared format. Darkhex can validate files by their actual content, ensuring compliance with organizational policies and reducing the risk of accidental or malicious misuse of incorrectly labeled files.
### ⚡ Software Development & Automation
Developers and system administrators can integrate darkhex into pipelines, scripts, or backend systems to automatically verify file types. This prevents errors or crashes caused by misidentified files and supports more robust and secure automation workflows.
## 🗂️ SUPPORTED FILETYPES
Darkhex currently supports multiple filetypes that can be categorized into 4 groups. Here is a full list of all filetypes that are currently supported: 
### 🖼️ Image Formats
| File Type            | Extension | Hex Signature                   |
| -------------------- | --------- | ------------------------------- |
| Bitmap               | `.bmp`    | `42 4D`                         |
| FITS                 | `.fits`   | `53 49 4D 50 4C 45`             |
| GIF                  | `.gif`    | `47 49 46 38`                   |
| GKS                  | `.gks`    | `47 4B 53 4D`                   |
| RGB                  | `.rgb`    | `01 DA`                         |
| ITC                  | `.itc`    | `F1 00 40 BB`                   |
| JPEG                 | `.jpg`    | `FF D8 FF E0`                   |
| NIF                  | `.nif`    | `49 49 4E 31`                   |
| PM                   | `.pm`     | `56 49 45 57`                   |
| PNG                  | `.png`    | `89 50 4E 47`                   |
| PostScript           | `.ps`     | `25 21`                         |
| Encapsulated PS      | `.eps`    | `25 21`                         |
| Sun Raster           | `.ras`    | `59 A6 6A 95`                   |
| TIFF (Big Endian)    | `.tif`    | `4D 4D 00 2A`                   |
| TIFF (Little Endian) | `.tif`    | `49 49 2A 00`                   |
| GIMP XCF             | `.xcf`    | `67 69 6D 70 20 78 63 66 20 76` |
| FIG                  | `.fig`    | `23 46 49 47`                   |
| XPM                  | `.xpm`    | `2F 2A 20 58 50 4D 20 2A 2F`    |
### 🗜️ Compression Formats
| File Type     | Extension | Hex Signature       |
| ------------- | --------- | ------------------- |
| Bzip          | `.bz`     | `42 5A`             |
| Unix Compress | `.Z`      | `1F 9D`             |
| Gzip          | `.gz`     | `1F 8B`             |
| Zip           | `.zip`    | `50 4B 03 04`       |
| Bzip2         | `.bz2`    | `42 5A 68`          |
| XZ (LZMA2)    | `.xz`     | `FD 37 7A 58 5A 00` |
| Lzip          | `.lz`     | `4C 5A 49 50`       |
### 📦 Archive Formats
| File Type     | Extension | Hex Signature                   |
| ------------- | --------- | ------------------------------- |
| 7-Zip         | `.7z`     | `37 7A BC AF 27 1C`             |
| RAR           | `.rar`    | `52 61 72 21 1A 07`             |
| Unix ar       | `.ar`     | `21 3C 61 72 63 68 3E 0A`       |
| Microsoft CAB | `.cab`    | `4D 53 43 46`                   |
| ISO 9660      | `.iso`    | `43 44 30 30 31` (offset 32769) |
### ⚡ Executables & Bytecode
| Platform                 | Identifier              | Hex Signature |
| ------------------------ | ----------------------- | ------------- |
| Windows PE               | `windows_executable`    | `4D 5A`       |
| Linux ELF                | `linux_executable`      | `7F 45 4C 46` |
| macOS Mach‑O (32‑bit BE) | `macos_executable_32be` | `FE ED FA CE` |
| macOS Mach‑O (32‑bit LE) | `macos_executable_32le` | `CE FA ED FE` |
| macOS Mach‑O (64‑bit BE) | `macos_executable_64be` | `FE ED FA CF` |
| macOS Mach‑O (64‑bit LE) | `macos_executable_64le` | `CF FA ED FE` |
| Java Bytecode            | `java_bytecode`         | `CA FE BA BE` |
## 📦 INSTALLATION
Clone the repository:
```bash
git clone https://github.com/ostrichwoddy/darkhex.git
cd darkhex
```
## 🧰 REQUIREMENTS
- Ensure that **Python 3** is installed. Darkhex currently only uses standard Python libraries and does not require any external dependencies.  
- Darkhex is compatible with **Windows, Linux, and macOS**.  
## 🧪 USAGE
### SYNTAX
```
python3 darkhex.py <path_to_file>
```
### EXAMPLE
```
python3 darkhex.py unknown.bin
```
Example Output:
```
linux_executable
```
## 🧩 PROJECT STRUCTURE
```commandline
darkhex/
├── darkhex.py
├── gethex.py
├── id_type.py
└── README.md
```
## 🧱 EXTENDING DARKHEX TO SUPPORT MORE FILETYPES
Darkhex is intentionally designed to be extended easily. If you want to extend darkhex to support more filetypes, simple add them along with their file signatures inside the appropriate dictionary (or create a new dictionary if needed) in [id_type.py](id_type.py)
## 📜 LICENSE
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
## 🤝  CONTRIBUTION GUIDELINES
If you wish to contribute to Darkhex, please follow the following steps. Note that all contributions fall under the Apache 2.0 license.
1. **Fork & clone** the repo:  

    ```bash
    git clone https://github.com/your-username/darkhex.git
    cd darkhex
    ```

2. **Create a branch** for your change:  

    ```bash
    git checkout -b feature-name
    ```

3. **Make changes** and test.  

4. **Commit with a clear message**:  

    ```bash
    git commit -m "Add support for new file signature"
    ```
5. **Push & open a pull request**.