from generate import start_copy_from_to, generate_pages_recursive

def main():

    start_copy_from_to("static", "public")

    generate_pages_recursive("content", "template.html", "public")
    

if __name__ == "__main__":
    main()
