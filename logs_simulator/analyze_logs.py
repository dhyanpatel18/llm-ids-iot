import pandas as pd

# Load logs
logs = pd.read_json("data/iot_logs.jsonl", lines=True)

# Basic stats
print(f"Total logs: {len(logs)}")
print(f"Attack rate: {logs['is_attack'].mean():.2%}")
print("\nAttack Types Distribution:")
print(logs[logs['is_attack']]['attack_type'].value_counts())