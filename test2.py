#section c: Advanced Python Concepts (30%)

def err_msg(err_msg):
    with open("err_log.txt","a") as f:
        f.write(err_msg)

def read_logs(file_name):
    log=[]
    log_count={
        "INFO":0,
        "ERROR":0,
        "WARNING":0,
    }

    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()

                if line =="":
                    continue
                part = line.split()

                record={
                    "level":part[0],
                    "message":" ".join(part[1:])
                }

                log.append(record)

                if record["level"]=="INFO":
                    log_count["INFO"]+=1
                elif record["level"]=="ERROR":
                    log_count["ERROR"]+=1
                elif record["level"]=="WARNING":
                    log_count["WARNING"]+=1

        return log , log_count
    
    except FileNotFoundError as e:
            err_msg(f"File not found: {e}")
            return [], {}  

def display_summ(log , log_count):
    print("log_summary")
    print(f"Total INFO logs: {log_count.get('INFO', 0)}")
    print(f"Total ERROR logs: {log_count.get('ERROR', 0)}")
    print(f"Total WARNING logs: {log_count.get('WARNING', 0)}")

    print("LOG DETAILS")
    for entry in log:
        print(f"[{entry['level']}] {entry['message']}")

def main():
    file_name = input("enter the name of log file:")
    log , log_count= read_logs(file_name)
    if log_count:
        display_summ(log , log_count)

main()     
