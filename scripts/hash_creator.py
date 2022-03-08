import os
import pandas as pd
import xlsxwriter
import hashlib

evidenceName = []
MD5 = []
SHA1 = []

def evidence():
    # Loop through file in current direcory (if you want to use another directory change the '.').
    for filename in os.listdir('.'):
        # Get MD5 hash of file.
        md5 = hashlib.md5(open(filename,'rb').read()).hexdigest()
        # Get SHA1 hash of file.
        sha1 = hashlib.sha1(open(filename,'rb').read()).hexdigest()
        # Print filename and hash values to the terminal.
        print(filename + ': \n' + 'MD5: ' + md5 + '\n' + 'sha1: ' + sha1)
        print('-----------------------------------------')
        # Add filename and hash values to the corosponding array.
        evidenceName.append(filename)
        MD5.append(md5)
        SHA1.append(sha1)
        # Send array to the excelWrite function.
        excelWrite(evidenceName, MD5, SHA1)

def excelWrite(evidenceName, MD5, SHA1):
    # dataframe Name and Age columns
    df = pd.DataFrame({'evidence name': evidenceName,
                       'MD5': MD5,
                       'SHA1': SHA1
                       })
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('evidence.xlsx', engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='evidence', index=False)
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

def main():
    evidence()
    # excelCheck()

if __name__ == "__main__":
    main()
