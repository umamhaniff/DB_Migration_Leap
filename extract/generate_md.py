import re
from datetime import datetime

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

# Generate markdown
md_content = f"""# Database Schema Documentation

**Database**: dataleap_v5_example  
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary
- **Total Tables**: {len(tables)}
- **Total Rows**: {sum(table['row_count'] for table in tables.values())}

## Table of Contents
"""

# Generate TOC
for i, table_name in enumerate(sorted(tables.keys()), 1):
    md_content += f"\n{i}. [{table_name}](#{table_name})"

md_content += "\n\n---\n\n"

# Generate table documentation
for table_name in sorted(tables.keys()):
    table_info = tables[table_name]
    column_count = len(table_info['columns'])
    row_count = table_info['row_count']
    
    md_content += f"## {table_name}\n\n"
    md_content += f"| Property | Value |\n"
    md_content += f"|----------|-------|\n"
    md_content += f"| **Columns** | {column_count} |\n"
    md_content += f"| **Rows** | {row_count:,} |\n\n"
    
    md_content += f"### Columns ({column_count})\n\n"
    md_content += f"| # | Column Name |\n"
    md_content += f"|---|-------------|\n"
    for col_idx, column in enumerate(table_info['columns'], 1):
        md_content += f"| {col_idx} | `{column}` |\n"
    
    md_content += "\n"

# Write to markdown file
with open('DATABASE_SCHEMA.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print("✓ Database schema documentation generated successfully!")
print(f"✓ File saved as: DATABASE_SCHEMA.md")
print(f"✓ Total tables: {len(tables)}")
print(f"✓ Total rows: {sum(table['row_count'] for table in tables.values()):,}")
