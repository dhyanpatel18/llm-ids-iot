import json
import random
from datetime import datetime
from faker import Faker
from tqdm import tqdm

# Initialize tools
fake = Faker()
devices = [f"device_{i:02d}" for i in range(1, 21)]  # 20 devices
attack_types = ["DDoS", "MQTT_Flood", "Brute_Force", "SQLi", "Port_Scan"]

def generate_log_entry():
    """Generate a single log entry with realistic IoT patterns"""
    log = {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f"),
        "device_id": random.choice(devices),
        "ip": fake.ipv4(),
        "protocol": random.choice(["MQTT", "CoAP", "HTTP"]),
        "payload_size": random.randint(10, 2048),
        "status": random.choice(["SUCCESS", "FAILED", "TIMEOUT"]),
    }
    
    # Simulate attacks (10% chance)
    if random.random() < 0.1:
        log.update({
            "is_attack": True,
            "attack_type": random.choice(attack_types),
            "payload": fake.text(max_nb_chars=50)  # Malicious payload
        })
    else:
        log.update({
            "is_attack": False,
            "payload": fake.text(max_nb_chars=20)  # Normal payload
        })
    
    return log

def generate_logs(num_entries=10000, output_file="data/iot_logs.jsonl"):
    """Generate synthetic logs"""
    with open(output_file, "w") as f:
        for _ in tqdm(range(num_entries), desc="Generating logs"):
            log_entry = generate_log_entry()
            f.write(json.dumps(log_entry) + "\n")

if __name__ == "__main__":
    generate_logs(num_entries=5000) 