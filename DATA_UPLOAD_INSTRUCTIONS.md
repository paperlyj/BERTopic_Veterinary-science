# Data upload instructions

The original raw CSV is too large for direct upload to a GitHub repository through the web interface. Use one of the following options.

## Recommended option: GitHub Release asset
Upload `export_veterinary_science_scopus_2010_2025.csv.gz` as a Release asset instead of committing it directly to the repository.

Suggested repository structure:

```text
README.md
requirements.txt
notebooks/Veterinary-Science_GitHub_ready.ipynb
data/README_data.md
```

Then include the Release download link in `data/README_data.md` and in the main `README.md`.

## Alternative option: split files for web upload
If you must upload through the GitHub web interface, upload all split files below:

```text
export_veterinary_science_scopus_2010_2025.csv.gz.part00
export_veterinary_science_scopus_2010_2025.csv.gz.part01
export_veterinary_science_scopus_2010_2025.csv.gz.part02
```

To reconstruct the original `.csv.gz` file:

### macOS/Linux/Git Bash

```bash
cat export_veterinary_science_scopus_2010_2025.csv.gz.part* > export_veterinary_science_scopus_2010_2025.csv.gz
```

### Windows PowerShell

```powershell
Get-Content -Encoding Byte export_veterinary_science_scopus_2010_2025.csv.gz.part* | Set-Content -Encoding Byte export_veterinary_science_scopus_2010_2025.csv.gz
```

Then read the file in Python:

```python
import pandas as pd

df = pd.read_csv("export_veterinary_science_scopus_2010_2025.csv.gz", compression="gzip", encoding="utf-8-sig")
print(df.shape)
```

Expected shape:

```text
(12937, 24)
```

## Checksum
Use `SHA256SUMS.txt` to verify file integrity if needed.
