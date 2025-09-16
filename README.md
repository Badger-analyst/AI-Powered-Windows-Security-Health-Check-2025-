# AI-Powered-Windows-Security-Health-Check-2025-
1)Cybersecurity (Cisco skills) → Windows firewall, antivirus, ACL checks, malware scan. 
2)`Machine Learning (Oracle ML) → Basic anomaly detection on system logs or processes.

ai-windows-security-check-2025/
│── README.md                # Project description + how to run
│── security-check.ps1       # PowerShell script (collect system/security data)
│── analyze-logs.py          # Python script (ML anomaly detection)
│── sample-data/             # Example logs & outputs
│── requirements.txt         # Python dependencies (scikit-learn, pandas, matplotlib)
│── .gitignore

# 🛡️ AI-Powered Windows Security Health Check (2025)

This project combines **Cisco Cybersecurity Essentials skills** with **Oracle Machine Learning fundamentals** to create a hybrid security + AI audit tool.

## ✅ Features
- PowerShell script collects firewall, AV, and process logs.
- Python ML model (Isolation Forest) detects unusual processes.
- Outputs CSV/Markdown reports with anomalies flagged.

This script collects firewall, AV, suspicious processes, and logs into a CSV for the ML part.
🔹 Step 1. PowerShell Script (security-check.ps1)
<# 
.SYNOPSIS
  Windows Security Health Check + Log Export
.DESCRIPTION
  Collects firewall, AV, suspicious processes, and logs for ML analysis.
#>

Write-Host "=== AI-Powered Security Check (2025) ===" -ForegroundColor Cyan

# Firewall
$firewallProfiles = Get-NetFirewallProfile
$firewallProfiles | Select-Object Name, Enabled |
    Export-Csv ".\firewall-status.csv" -NoTypeInformation

# Antivirus
$av = Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct 2>$null
$av | Select-Object displayName, productState |
    Export-Csv ".\antivirus-status.csv" -NoTypeInformation

# Processes (for anomaly detection)
Get-Process | Select-Object ProcessName, Id, CPU, WS, Path |
    Export-Csv ".\process-logs.csv" -NoTypeInformation

Write-Host "Logs exported: firewall-status.csv, antivirus-status.csv, process-logs.csv"

Step 2. Python Script (analyze-logs.py)
import pandas as pd
from sklearn.ensemble import IsolationForest

# Load process logs
df = pd.read_csv("process-logs.csv")

# Clean numeric features
features = df[["CPU", "WS"]].fillna(0)

# Train Isolation Forest for anomaly detection
model = IsolationForest(contamination=0.05, random_state=42)
df["anomaly"] = model.fit_predict(features)

# Save anomalies
anomalies = df[df["anomaly"] == -1]
anomalies.to_csv("anomalies.csv", index=False)

print("✅ Analysis complete. Found", len(anomalies), "suspicious processes.")
print("Results saved in anomalies.csv")


Uses ML to detect unusual processes (e.g., memory/CPU spikes).

## 🚀 Usage
1. Clone repo:
   ```bash
   git clone https://github.com/YOUR-USERNAME/ai-windows-security-check-2025.git
   cd ai-windows-security-check-2025

Run PowerShell script:
.\security-check.ps1

Run Python analysis:
pip install -r requirements.txt
python analyze-logs.py

Review results:

firewall-status.csv

antivirus-status.csv

anomalies.csv


---
MIT License
## 🔹 Step 4. Upload to GitHub (Step-by-Step)
1. **Create a repo** on GitHub → name: `ai-windows-security-check-2025`.  
   - Description: *AI + Cybersecurity project: Windows health check with ML anomaly detection*.  
   - Add MIT license, `.gitignore` (Python + Windows).  

2. **Clone repo locally**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/ai-windows-security-check-2025.git
   cd ai-windows-security-check-2025
