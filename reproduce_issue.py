import re

def add_generated_metadata_property(md_text, prop_name, generated_value):
    small_block_re = re.compile(r'(<small>)(.*?)(</small>)', re.DOTALL)
    match = small_block_re.search(md_text)
    
    # The property specific tag to check if it exists
    check_tag = f"_{prop_name}:"

    if match:
        before_tag = match.group(1)
        middle_block = match.group(2)
        after_tag = match.group(3)

        if check_tag in middle_block:
            return md_text

        existing_content = middle_block.strip()
        if existing_content:
            new_content = existing_content + f"\n* {check_tag} {generated_value}"
        else:
            new_content = f"* {check_tag} {generated_value}"

        updated_block = f"{before_tag}\n\n{new_content}\n\n{after_tag}"

        return (
            md_text[:match.start()] +
            updated_block +
            md_text[match.end():]
        )
    else:
        return md_text

# Test case
input_text = """# Problem 1

Some text.

<small>
* questionType: existing
</small>
"""

prop = "subdomain"
value = "DOM_AlgebraicOperations"

output = add_generated_metadata_property(input_text, prop, value)
print("--- OUTPUT ---")
print(output)
print("--------------")
