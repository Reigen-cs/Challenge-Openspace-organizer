import pandas as pd

def load_colleagues_from_file(filepath):
    try:
        # Read CSV file
        df = pd.read_csv(filepath)
        
        # Get names from 'Name' column
        names = df['Name'].tolist()
        
        # Remove empty values
        names = [name for name in names if str(name) != 'nan']
        
        print(f"Loaded {len(names)} colleagues")
        return names
        
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def create_sample_file(filepath):
    sample_names = [
        "Random 1", "Random 2", "Random 3", "Random 4", "Random 5", "Random 6",
        "Random 7", "Random 8", "Random 9", "Random 10", "Random 11", "Random 12",
        "Random 13", "Random 14", "Random 15", "Random 16", "Random 17", "Random 18",
        "Random 19", "Random 20", "Random 21", "Random 22", "Random 23", "Random 24",
        "Random 25", "Random 26", "Random 27", "Random 28", "Random 29", "Random 30"
    ]
    
    df = pd.DataFrame({"Name": sample_names})
    df.to_csv(filepath, index=False)
    print(f"Created sample file with {len(sample_names)} names")