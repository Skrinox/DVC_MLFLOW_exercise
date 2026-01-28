import os
import json
import sys

ACCURACY_THRESHOLD = float(os.getenv("ACCURACY_THRESHOLD", "0.88"))

def main():
    if not sys.stdin.isatty():
        payload = sys.stdin.read().strip()
    else:
        payload = sys.argv[1]
        
    data = json.loads(payload)
    acc = float(data["accuracy"])
    
    passed = acc >= ACCURACY_THRESHOLD
    
    result = {
        "passed": passed,
        "accuracy": acc,
        "threshold": ACCURACY_THRESHOLD,
        "model_version": data["model_version"],
        "run_id": data["run_id"],
    }
    
    print(json.dumps(result))
    
    if not passed:
        sys.exit(1)

if __name__ == "__main__":
    main()