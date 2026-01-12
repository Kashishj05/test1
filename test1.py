# section B: Core Python & Data Handling (20%)
file_name=input("Enter the log file name: ")

log=[]

log_count={
    "INFO":0,
    "ERROR":0,
    "WARNING":0
}

with open(file_name,'r') as file:
    for line in file:
        line = line.strip()

        if line ==" ":
            continue
        part = line.split()

        records={
            "level":part[0],
            "message":" ".join(part[1:])
        }
        log.append(records)

        if records["level"]=="INFO":
            log_count["INFO"]+=1
        elif records["level"]=="ERROR":
            log_count["ERROR"]+=1
        elif records["level"]=="WARNING":
            log_count["WARNING"]+=1

print("Log Summary:")
print(f"Total INFO logs: {log_count['INFO']}")
print(f"Total ERROR logs: {log_count['ERROR']}")
print(f"Total WARNING logs: {log_count['WARNING']}")
print("\nLog Details:")
for entry in log:
    print(f"[{entry['level']}] {entry['message']}") 



