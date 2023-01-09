import re

_img_link_pattern = re.compile(r"\[imglink\]([A-z-_0-9]+)\[\/imglink\]")


def handle_bb_image_links(image_links, content):
    return _img_link_pattern.sub(lambda x: image_links[x.group(1)], content)
