import requests

def validate_markdown(filename):
    issues = []

    with open(filename, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines, start=1):

        # Check bold syntax
        if line.count("**") % 2 != 0:
            issues.append(f"Line {i}: Bold syntax error → Suggestion: close **")

        # Check heading
        if line.startswith("#") and not line.startswith("# "):
            issues.append(f"Line {i}: Heading format wrong → Suggestion: add space after #")

        # Check links
        if "http" in line:
            try:
                r = requests.get(line.strip())
                if r.status_code != 200:
                    issues.append(f"Line {i}: Broken link → Suggestion: use valid URL")
            except:
                issues.append(f"Line {i}: Invalid link → Suggestion: correct URL")

    return issues
