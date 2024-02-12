import subprocess #subprocess class that allows me to use the Popen Constructor to run CMD processes
import shlex #shlex class parse Unix syntax 

def OsintAutomation(Domain_Name): 
    try:
        # whois 
        whois_command = f"whois {Domain_Name}" #fstring taking in an input for domain 
        whois_process = subprocess.Popen(shlex.split(whois_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE) # run a subprocess with shlex.split as an argument and the command with input embedded as the variable, 2nd and 3rd argument is to Pipe output and error information
        whois_output, _ = whois_process.communicate() #comma and _ is for .communicate since it returns a tuple, this caused me a lot of trouble to figure out do not remove

        # Nslookup 
        nslookup_command = f"nslookup {Domain_Name}"
        nslookup_process = subprocess.Popen(shlex.split(nslookup_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        nslookup_output, _ = nslookup_process.communicate() 

        # Dig
        dig_command = f"dig {Domain_Name}"
        dig_process = subprocess.Popen(shlex.split(dig_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        dig_output, _ = dig_process.communicate()

        # Save Investigation output to a file 
        with open("OsintInvestigation.txt", "w") as Osint_output_file:            #opens personal named file and 2nd perameter defines mode which is to write
            Osint_output_file.write(f"WHOIS Info:\n{whois_output.decode()}\n\n") # writes info to the file, decode is used due to subprocess converting info into bytes .decode turns it back into a string 
            Osint_output_file.write(f"NSLOOKUP Info:\n{nslookup_output.decode()}\n\n")
            Osint_output_file.write(f"DIG Info:\n{dig_output.decode()}\n")

        print(f"Information saved to OsintInvestigation.txt")
    except Exception as err: # If this doesn't run properly just exit and pass the err variable into print
        print(f"Error: {str(err)}")

# Main 
Domain_Name = input("Enter a domain name for intel ")
OsintAutomation(Domain_Name)

