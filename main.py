import sys
import os

# Add the utils directory to the path to import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from file_utils import load_colleagues_from_file, create_sample_file
from openspace import Openspace

def main():
    print("Simple Openspace Seat Assignment")
    print("=" * 30)
    
    filepath = "colleagues.csv"
    
    # Create sample file if it doesn't exist
    if not os.path.exists(filepath):
        print("Creating sample CSV file...")
        create_sample_file(filepath)
    
    # Load colleagues
    colleagues = load_colleagues_from_file(filepath)
    
    if not colleagues:
        print("No colleagues found!")
        return
    
    # Create openspace and organize
    openspace = Openspace()
    openspace.organize(colleagues)
    
    # Display results
    openspace.display()
    
    print(f"\nTotal people: {len(colleagues)}")
    print(f"Total tables: {len(openspace.tables)}")

if __name__ == "__main__":
    main()