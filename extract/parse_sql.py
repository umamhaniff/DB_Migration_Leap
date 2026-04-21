import re

# Read the SQL file
with open('dataleap_v5_example-202604211322.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# Dictionary to store table info
tables = {}

# Find all CREATE TABLE statements
create_table_pattern = r'CREATE TABLE `(\w+)` \(([\s\S]*?)\) ENGINE'
matches = re.finditer(create_table_pattern, content)

for match in matches:
    table_name = match.group(1)
    columns_text = match.group(2)
    
    # Extract column names (from CREATE TABLE statements)
    column_pattern = r'`(\w+)`\s+\w+'
    columns = re.findall(column_pattern, columns_text)
    
    # Count rows in INSERT statements
    insert_pattern = r'INSERT INTO `' + table_name + r'` VALUES'
    insert_match = re.search(insert_pattern, content)
    
    row_count = 0
    if insert_match:
        start = insert_match.end()
        # Find next UNLOCK or end of file
        next_unlock = content.find('UNLOCK TABLES', start)
        if next_unlock == -1:
            end = len(content)
        else:
            end = next_unlock
        
        insert_section = content[start:end]
        # Count rows - each row starts with newline followed by (
        row_count = insert_section.count('\n(')
    
    tables[table_name] = {
        'columns': columns,
        'row_count': row_count
    }

# Print results
for table_name in sorted(tables.keys()):
    print(f"Table: {table_name}")
    print(f"  Columns: {', '.join(tables[table_name]['columns'])}")
    print(f"  Row Count: {tables[table_name]['row_count']}")
    print()
