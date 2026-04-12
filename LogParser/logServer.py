# Iterate through the file line by line.

# Identify only the lines that represent an ERROR.

# For those error lines, use string slicing and methods to extract only the timestamp (without the brackets) and the actual error message text (without the word "ERROR" and surrounding spaces).

# Print the extracted data to the console in this exact format using an f-string:
# Time: 2026-04-12 08:16:45 | Incident: Failed to connect to database at 192.168.1.5
with open("server.log", "r") as file:
    
    # Iterate through the file line by line
    for line in file:
        clean_log = line.strip() # Remove the hidden newline character
        
        # Identify only the lines that contain an ERROR
        if "ERROR" in clean_log:
            
            # Extract the timestamp (characters at index 1 through 19)
            time = clean_log[1:20]
            
            # Extract the message by splitting the string at "ERROR "
            # This gives us everything after the word ERROR
            parts = clean_log.split("ERROR ")
            incident_msg = parts[1].strip() 
            
            # Print the extracted data dynamically using our f-string
            log_msg = f"Time: {time} | Incident: {incident_msg}"
            print(log_msg)