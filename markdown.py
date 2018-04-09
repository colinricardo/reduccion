import re

# ![](https://cdn.vox-cdn.com/thumbor/-SmppV2xOkTKbVXopm2Ftrd6OJw=/0x0:3000x2000/1200x800/filters:focal\(1315x220:1795x700\)/cdn.vox-cdn.com/uploads/chorus_image/image/59035787/shutterstock_272424740.0.jpg)


def fixImages(markdown):
    print(markdown)
    imgPattern = r'!\[([^\]]*)\]\((.*)\)'
    repl = r'<center><img src="\2" alt="\1" height="300" width="600"></cemter>'
    return re.sub(imgPattern, repl, markdown)


def removeDoubleTitles(lines):
    fourth = lines[3]
    if fourth.startswith('#'):
        return lines[2:]
    return lines


def removeLeadingImage(lines):
    second = lines[1]
    pattern = r'\!\[.*\](.*)'
    if re.match(pattern, second):
        lines[1] = ''
    return lines


def process(lines):
    a = removeDoubleTitles(lines)
    b = removeLeadingImage(a)
    c = '\n'.join(b)
    return c
