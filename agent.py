from validator import validate_markdown

file_name = input("Enter markdown file name: ")
if not file_name.endswith(".md"):
    print("Please enter a markdown (.md) file only")
    exit()


issues = validate_markdown(file_name)

if issues:
    print("\nIssues Found:\n")
    for issue in issues:
        print(issue)

    # CREATE REPORT FILE
    with open("report.txt", "w", encoding="utf-8") as report:

        report.write("Markdown Validation Report\n")
        report.write("-------------------------\n")
        for issue in issues:
            report.write(issue + "\n")
        report.write(f"\nTotal Issues: {len(issues)}")

    print("\nReport saved as report.txt")

else:
    print("No issues found.")
