import subprocess
import json
from pathlib import Path

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result.stdout.strip()

def adb(cmd):
    return run(f"adb {cmd}")

def main():
    print("🔍 Iniciando scan...")

    devices = adb("devices")
    if "device" not in devices:
        print("❌ Nenhum dispositivo conectado")
        return

    report = {}
    report["model"] = adb("shell getprop ro.product.model")
    report["android"] = adb("shell getprop ro.build.version.release")
    report["packages"] = adb("shell pm list packages")

    with open("output/report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("✅ michely puta!")

if __name__ == "__main__":
    main()
