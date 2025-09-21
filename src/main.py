import sys
from generate import start_copy_from_to, generate_pages_recursive

def main():

    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"

    start_copy_from_to("static", "docs")

    generate_pages_recursive("content", "template.html", "docs", base_path)
    

if __name__ == "__main__":
    main()
