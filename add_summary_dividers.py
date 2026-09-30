import os
import glob

def process_markdown_files():
    md_files = glob.glob("content/**/*.md", recursive=True)
    count = 0
    for filepath in md_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if "<!--more-->" in content:
            continue

        # Insert <!--more--> after the first H1 or first paragraph
        lines = content.splitlines()
        new_lines = []
        inserted = False

        for i, line in enumerate(lines):
            new_lines.append(line)
            # Find end of frontmatter or first paragraph/heading
            if not inserted and (line.startswith("# ") or line.startswith("**【") or line.startswith("【")):
                new_lines.append("\n<!--more-->\n")
                inserted = True

        if inserted:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(new_lines))
            count += 1

    print(f"Added <!--more--> divider to {count} markdown files.")

if __name__ == "__main__":
    process_markdown_files()
