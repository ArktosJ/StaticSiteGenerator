import sys
from generate import start_copy_from_to, generate_pages_recursive

def main():

    base_path = sys.argv[1]
    base = "/home/arktosj/StaticSiteGenerator/StaticSiteGenerator"
    start_copy_from_to("static", "docs", base_path)

    generate_pages_recursive("content", "template.html", "docs", base_path)
    

if __name__ == "__main__":
    main()
