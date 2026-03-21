import os

# Delete the temporary write script
temp_file = r'd:\S.P.A.R.K\_tmp_write_landing.py'
if os.path.exists(temp_file):
    os.remove(temp_file)
    print(f"✓ Deleted {temp_file}")
else:
    print(f"File not found: {temp_file}")
