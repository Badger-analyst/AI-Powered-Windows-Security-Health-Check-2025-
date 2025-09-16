project that combines:

Cybersecurity (Cisco skills) → Windows firewall, antivirus, ACL checks, malware scan.

Machine Learning (Oracle ML) → Basic anomaly detection on system logs or processes.
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
This way, it’s not just another script — it’s a security tool with AI insights.
Project Features

✅ Check Windows 10/11 firewall, AV, malware scan (like we started).

✅ Export logs (processes, network connections, sign-ins).

✅ Feed logs into a simple ML model (Python, scikit-learn) to detect anomalies.

✅ Output a report in Markdown or CSV with:

Security posture (firewall, AV, MFA).

Any anomalies flagged by ML.
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Repo Structure

ai-windows-security-check-2025/
│── README.md                # Project description + how to run
│── security-check.ps1       # PowerShell script (collect system/security data)
│── analyze-logs.py          # Python script (ML anomaly detection)
│── sample-data/             # Example logs & outputs
│── requirements.txt         # Python dependencies (scikit-learn, pandas, matplotlib)
│── .gitignore
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Step 1. PowerShell Script (security-check.ps1)

This script collects firewall, AV, suspicious processes, and logs into a CSV for the ML part.
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
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Step 2. Python Script (analyze-logs.py)

Uses ML to detect unusual processes (e.g., memory/CPU spikes).
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
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Step 3. README.md
# 🛡️ AI-Powered Windows Security Health Check (2025)

This project combines **Cisco Cybersecurity Essentials skills** with **Oracle Machine Learning fundamentals** to create a hybrid security + AI audit tool.

## ✅ Features
- PowerShell script collects firewall, AV, and process logs.
- Python ML model (Isolation Forest) detects unusual processes.
- Outputs CSV/Markdown reports with anomalies flagged.

## 🚀 Usage
1. Clone repo:
   ```bash
   git clone https://github.com/YOUR-USERNAME/ai-windows-security-check-2025.git
   cd ai-windows-security-check-2025
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
2.Run PowerShell script:
.\security-check.ps1
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
3.Run Python analysis:
pip install -r requirements.txt
python analyze-logs.py
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
4.Review results:

#firewall-status.csv
#antivirus-status.csv
#anomalies.csv
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
MIT License

## 🔹 Step 4. Upload to GitHub (Step-by-Step)
1. **Create a repo** on GitHub → name: `ai-windows-security-check-2025`.  
   - Description: *AI + Cybersecurity project: Windows health check with ML anomaly detection*.  
   - Add MIT license, `.gitignore` (Python + Windows).  

2. **Clone repo locally**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/ai-windows-security-check-2025.git
   cd ai-windows-security-check-2025
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
step 4
git add README.md security-check.ps1 analyze-logs.py requirements.txt
git commit -m "Initial commit: AI-powered security check project"
git push origin main
