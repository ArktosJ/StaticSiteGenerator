import shutil
import os
from blocks import extract_title, markdown_to_html_node


def start_copy_from_to(from_dir, to_dir):
    start_path = "/home/arktosj/StaticSiteGenerator/StaticSiteGenerator"
    path_from_dir = start_path + "/" + from_dir
    path_to_dir = start_path + "/" + to_dir
    if os.path.exists(path_to_dir):
        shutil.rmtree(path_to_dir)
    os.mkdir(path_to_dir)
    copy_from_to(path_from_dir, path_to_dir)

def copy_from_to(from_dir, to_dir):
    if os.path.exists(from_dir):
        obj_in_dir = os.listdir(from_dir)
        for obj in obj_in_dir:
            obj_path = from_dir + "/" + obj
            if os.path.isfile(obj_path):
                shutil.copy(obj_path, to_dir)
            if os.path.isdir(obj_path):
                new_dir = to_dir + "/" + obj
                os.mkdir(new_dir)
                copy_from_to(obj_path, new_dir)
    else:
        raise Exception("No such path excists")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    start_path = "/home/arktosj/StaticSiteGenerator/StaticSiteGenerator"
    true_content_path = start_path + "/" + dir_path_content
    true_dest_path = start_path + "/" + dest_dir_path
    true_template_path = start_path + "/" + template_path
    recursive_call(true_content_path, true_template_path, true_dest_path)
    pass


def recursive_call(dir_path_content, template_path, dest_dir_path):
    print(f"looking at {dir_path_content}")
    if os.path.exists(dir_path_content):
        obj_in_dir = os.listdir(dir_path_content)
        for obj in obj_in_dir:
            obj_path = dir_path_content + "/" + obj
            if os.path.isfile(obj_path) and obj.endswith('.md'):
                generate_page(obj_path, template_path, dest_dir_path)
            if os.path.isdir(obj_path):
                new_dir =  dest_dir_path + "/" + obj
                os.mkdir(new_dir)
                recursive_call(obj_path, template_path, new_dir)
    else:
        raise Exception("No such path excists")



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f_from:
        from_file = f_from.read()
    with open(template_path, "r+") as f_template:
        template_file = f_template.read()
    total_html = template_file.replace("{{ Title }}", extract_title(from_file))
    total_html = total_html.replace("{{ Content }}", markdown_to_html_node(from_file).to_html())
    dest_list = os.path.dirname(dest_path).split('/')
    if not os.path.exists(os.path.dirname(dest_path)):
        start_path = "/home/arktosj/StaticSiteGenerator/StaticSiteGenerator" 
        for dir in dest_list:
            if os.path.exists(start_path + "/" + dir):
                start_path = start_path + "/" + dir
                continue  
            else:
                start_path = start_path + "/" + dir 
                os.mkdir(start_path)
    
    total_path = dest_path + "/" + "index.html"
    with open(total_path, "w") as f_dest:
        f_dest.write(total_html)
