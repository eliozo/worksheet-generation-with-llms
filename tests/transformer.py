import csv

def read_problems(file_name):
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        problems = [row for row in reader]
    return problems

def build_levels(problems):
    levels = {}
    top_level_count = 1

    for problem in problems:
        topic_id = problem['TopicID']
        parent = problem['Parent']
        sibling = int(problem['Sibling'])
        
        if parent == "TOP":
            level = f"{top_level_count}.0.0.0.0.0.0"
            top_level_count += 1
        else:
            parent_level = levels.get(parent, "X.X.X.X.X.X.X")
            parts = parent_level.split('.')
            print(f"parts = {parts}")
            parts[parts.index('0')] = str(sibling)
            level = '.'.join(parts)
        
        levels[topic_id] = level
    
    return levels

def transform_problems(problems, levels):
    transformed = []

    for problem in problems:
        topic_id = problem['TopicID']
        
        row = {
            "Levels": levels[topic_id],
            "TopicID": problem['TopicID'],
            "Parent": problem['Parent'],
            "Sibling": problem['Sibling'],
            "Title": problem['Title'],
            "Description": problem['Description'],
            "Links": problem['Links']
        }
        transformed.append(row)
    
    # Sort by levels to ensure preorder DFS traversal
    transformed.sort(key=lambda x: list(map(int, x['Levels'].split('.'))))
    
    return transformed

def write_transformed(file_name, transformed):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Levels", "TopicID", "Parent", "Sibling", "Title", "Description", "Links"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in transformed:
            writer.writerow(row)

def main():
    input_file = 'problems.csv'
    output_file = 'problems_transformed.csv'

    problems = read_problems(input_file)
    levels = build_levels(problems)
    transformed = transform_problems(problems, levels)
    write_transformed(output_file, transformed)

if __name__ == "__main__":
    main()